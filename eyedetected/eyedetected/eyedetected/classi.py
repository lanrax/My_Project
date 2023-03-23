import torch
from PIL import Image
import torchvision.transforms as transforms
from filepath.settings import example_img
import torchvision.models as models


def prepare_input_from_uri(image_path, cuda=False):
    img_transforms = transforms.Compose(
        [transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor()]
    )

    img = Image.open(image_path)

    img = img_transforms(img)
    with torch.no_grad():
        # mean and std are not multiplied by 255 as they are in training script
        # torch dataloader reads data into bytes whereas loading directly
        # through PIL creates a tensor with floats in [0,1] range
        mean = torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1)
        std = torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1)
        img = img.float()
        if cuda:
            mean = mean.cuda()
            std = std.cuda()
            img = img.cuda()
        input = img.unsqueeze(0).sub_(mean).div_(std)

    return input


def run_cls(file_path=example_img, engine="Pytorch"):
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    print(f'Using {device} for inference')

    resnet50 = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_resnet50', pretrained=True)
    # resnet50 = models.resnet50(pretrained=False)
    # resnet50.load_state_dict(torch.load(''), strict=True)
    utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_convnets_processing_utils')

    resnet50.eval().to(device)
    paths = [file_path]
    batch = torch.cat(
        [prepare_input_from_uri(path) for path in paths]
    ).to(device)

    with torch.no_grad():
        output = torch.nn.functional.softmax(resnet50(batch), dim=1)

    results = utils.pick_n_best(predictions=output, n=3)
    for im, result in zip(paths, results):
        img = Image.open(im)
        img.thumbnail((256, 256), Image.ANTIALIAS)
    return result
