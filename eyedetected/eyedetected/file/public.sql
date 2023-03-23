create database eye with owner postgres;
\c eye

-- ----------------------------
-- Sequence structure for auth_group_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_group_id_seq";
CREATE SEQUENCE "public"."auth_group_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_group_permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_group_permissions_id_seq";
CREATE SEQUENCE "public"."auth_group_permissions_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_permission_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_permission_id_seq";
CREATE SEQUENCE "public"."auth_permission_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_user_groups_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_user_groups_id_seq";
CREATE SEQUENCE "public"."auth_user_groups_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_user_id_seq";
CREATE SEQUENCE "public"."auth_user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_user_user_permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_user_user_permissions_id_seq";
CREATE SEQUENCE "public"."auth_user_user_permissions_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_admin_log_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_admin_log_id_seq";
CREATE SEQUENCE "public"."django_admin_log_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_content_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_content_type_id_seq";
CREATE SEQUENCE "public"."django_content_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_migrations_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_migrations_id_seq";
CREATE SEQUENCE "public"."django_migrations_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for eye_detect_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."eye_detect_id_seq";
CREATE SEQUENCE "public"."eye_detect_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for eye_detectserver_detect_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."eye_detectserver_detect_id_seq";
CREATE SEQUENCE "public"."eye_detectserver_detect_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for eye_result_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."eye_result_id_seq";
CREATE SEQUENCE "public"."eye_result_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group";
CREATE TABLE "public"."auth_group" (
  "id" int4 NOT NULL DEFAULT nextval('auth_group_id_seq'::regclass),
  "name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group_permissions";
CREATE TABLE "public"."auth_group_permissions" (
  "id" int8 NOT NULL DEFAULT nextval('auth_group_permissions_id_seq'::regclass),
  "group_id" int4 NOT NULL,
  "permission_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_permission";
CREATE TABLE "public"."auth_permission" (
  "id" int4 NOT NULL DEFAULT nextval('auth_permission_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "content_type_id" int4 NOT NULL,
  "codename" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO "public"."auth_permission" VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO "public"."auth_permission" VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO "public"."auth_permission" VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO "public"."auth_permission" VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO "public"."auth_permission" VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO "public"."auth_permission" VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO "public"."auth_permission" VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO "public"."auth_permission" VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO "public"."auth_permission" VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO "public"."auth_permission" VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO "public"."auth_permission" VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO "public"."auth_permission" VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO "public"."auth_permission" VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO "public"."auth_permission" VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO "public"."auth_permission" VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO "public"."auth_permission" VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO "public"."auth_permission" VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO "public"."auth_permission" VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO "public"."auth_permission" VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO "public"."auth_permission" VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO "public"."auth_permission" VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO "public"."auth_permission" VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO "public"."auth_permission" VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO "public"."auth_permission" VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO "public"."auth_permission" VALUES (25, 'Can add detect server', 7, 'add_detectserver');
INSERT INTO "public"."auth_permission" VALUES (26, 'Can change detect server', 7, 'change_detectserver');
INSERT INTO "public"."auth_permission" VALUES (27, 'Can delete detect server', 7, 'delete_detectserver');
INSERT INTO "public"."auth_permission" VALUES (28, 'Can view detect server', 7, 'view_detectserver');
INSERT INTO "public"."auth_permission" VALUES (29, 'Can add detect type', 8, 'add_detecttype');
INSERT INTO "public"."auth_permission" VALUES (30, 'Can change detect type', 8, 'change_detecttype');
INSERT INTO "public"."auth_permission" VALUES (31, 'Can delete detect type', 8, 'delete_detecttype');
INSERT INTO "public"."auth_permission" VALUES (32, 'Can view detect type', 8, 'view_detecttype');
INSERT INTO "public"."auth_permission" VALUES (33, 'Can add picture', 9, 'add_picture');
INSERT INTO "public"."auth_permission" VALUES (34, 'Can change picture', 9, 'change_picture');
INSERT INTO "public"."auth_permission" VALUES (35, 'Can delete picture', 9, 'delete_picture');
INSERT INTO "public"."auth_permission" VALUES (36, 'Can view picture', 9, 'view_picture');
INSERT INTO "public"."auth_permission" VALUES (37, 'Can add result', 10, 'add_result');
INSERT INTO "public"."auth_permission" VALUES (38, 'Can change result', 10, 'change_result');
INSERT INTO "public"."auth_permission" VALUES (39, 'Can delete result', 10, 'delete_result');
INSERT INTO "public"."auth_permission" VALUES (40, 'Can view result', 10, 'view_result');
INSERT INTO "public"."auth_permission" VALUES (41, 'Can add detect', 11, 'add_detect');
INSERT INTO "public"."auth_permission" VALUES (42, 'Can change detect', 11, 'change_detect');
INSERT INTO "public"."auth_permission" VALUES (43, 'Can delete detect', 11, 'delete_detect');
INSERT INTO "public"."auth_permission" VALUES (44, 'Can view detect', 11, 'view_detect');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_user";
CREATE TABLE "public"."auth_user" (
  "id" int4 NOT NULL DEFAULT nextval('auth_user_id_seq'::regclass),
  "password" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "last_login" timestamptz(6),
  "is_superuser" bool NOT NULL,
  "username" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "first_name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "last_name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "email" varchar(254) COLLATE "pg_catalog"."default" NOT NULL,
  "is_staff" bool NOT NULL,
  "is_active" bool NOT NULL,
  "date_joined" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO "public"."auth_user" VALUES (1, 'pbkdf2_sha256$320000$npUPxNvYwEWfMRaQqzHsyV$Lfyz9AHxgYp0/VuHnL2yv1twu3oeghIP/h5WsjRQlzU=', NULL, 't', 'admin', '', '', '', 't', 't', '2022-08-30 09:46:23.922155+00');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_user_groups";
CREATE TABLE "public"."auth_user_groups" (
  "id" int8 NOT NULL DEFAULT nextval('auth_user_groups_id_seq'::regclass),
  "user_id" int4 NOT NULL,
  "group_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_user_user_permissions";
CREATE TABLE "public"."auth_user_user_permissions" (
  "id" int8 NOT NULL DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass),
  "user_id" int4 NOT NULL,
  "permission_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_admin_log";
CREATE TABLE "public"."django_admin_log" (
  "id" int4 NOT NULL DEFAULT nextval('django_admin_log_id_seq'::regclass),
  "action_time" timestamptz(6) NOT NULL,
  "object_id" text COLLATE "pg_catalog"."default",
  "object_repr" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "action_flag" int2 NOT NULL,
  "change_message" text COLLATE "pg_catalog"."default" NOT NULL,
  "content_type_id" int4,
  "user_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_content_type";
CREATE TABLE "public"."django_content_type" (
  "id" int4 NOT NULL DEFAULT nextval('django_content_type_id_seq'::regclass),
  "app_label" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "model" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO "public"."django_content_type" VALUES (1, 'admin', 'logentry');
INSERT INTO "public"."django_content_type" VALUES (2, 'auth', 'permission');
INSERT INTO "public"."django_content_type" VALUES (3, 'auth', 'group');
INSERT INTO "public"."django_content_type" VALUES (4, 'auth', 'user');
INSERT INTO "public"."django_content_type" VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO "public"."django_content_type" VALUES (6, 'sessions', 'session');
INSERT INTO "public"."django_content_type" VALUES (7, 'eye', 'detectserver');
INSERT INTO "public"."django_content_type" VALUES (8, 'eye', 'detecttype');
INSERT INTO "public"."django_content_type" VALUES (9, 'eye', 'picture');
INSERT INTO "public"."django_content_type" VALUES (10, 'eye', 'result');
INSERT INTO "public"."django_content_type" VALUES (11, 'eye', 'detect');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_migrations";
CREATE TABLE "public"."django_migrations" (
  "id" int8 NOT NULL DEFAULT nextval('django_migrations_id_seq'::regclass),
  "app" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "applied" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO "public"."django_migrations" VALUES (1, 'contenttypes', '0001_initial', '2022-08-30 01:49:17.410944+00');
INSERT INTO "public"."django_migrations" VALUES (2, 'auth', '0001_initial', '2022-08-30 01:49:17.541019+00');
INSERT INTO "public"."django_migrations" VALUES (3, 'admin', '0001_initial', '2022-08-30 01:49:17.587054+00');
INSERT INTO "public"."django_migrations" VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-08-30 01:49:17.600064+00');
INSERT INTO "public"."django_migrations" VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-08-30 01:49:17.614072+00');
INSERT INTO "public"."django_migrations" VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2022-08-30 01:49:17.649096+00');
INSERT INTO "public"."django_migrations" VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2022-08-30 01:49:17.663112+00');
INSERT INTO "public"."django_migrations" VALUES (8, 'auth', '0003_alter_user_email_max_length', '2022-08-30 01:49:17.67912+00');
INSERT INTO "public"."django_migrations" VALUES (9, 'auth', '0004_alter_user_username_opts', '2022-08-30 01:49:17.697131+00');
INSERT INTO "public"."django_migrations" VALUES (10, 'auth', '0005_alter_user_last_login_null', '2022-08-30 01:49:17.723149+00');
INSERT INTO "public"."django_migrations" VALUES (11, 'auth', '0006_require_contenttypes_0002', '2022-08-30 01:49:17.729155+00');
INSERT INTO "public"."django_migrations" VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2022-08-30 01:49:17.771147+00');
INSERT INTO "public"."django_migrations" VALUES (13, 'auth', '0008_alter_user_username_max_length', '2022-08-30 01:49:17.798166+00');
INSERT INTO "public"."django_migrations" VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2022-08-30 01:49:17.834192+00');
INSERT INTO "public"."django_migrations" VALUES (15, 'auth', '0010_alter_group_name_max_length', '2022-08-30 01:49:17.853206+00');
INSERT INTO "public"."django_migrations" VALUES (16, 'auth', '0011_update_proxy_permissions', '2022-08-30 01:49:17.868216+00');
INSERT INTO "public"."django_migrations" VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2022-08-30 01:49:17.88723+00');
INSERT INTO "public"."django_migrations" VALUES (18, 'eye', '0001_initial', '2022-08-30 01:49:17.997308+00');
INSERT INTO "public"."django_migrations" VALUES (19, 'sessions', '0001_initial', '2022-08-30 01:49:18.022325+00');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_session";
CREATE TABLE "public"."django_session" (
  "session_key" varchar(40) COLLATE "pg_catalog"."default" NOT NULL,
  "session_data" text COLLATE "pg_catalog"."default" NOT NULL,
  "expire_date" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for eye_detect
-- ----------------------------
DROP TABLE IF EXISTS "public"."eye_detect";
CREATE TABLE "public"."eye_detect" (
  "id" int8 NOT NULL DEFAULT nextval('eye_detect_id_seq'::regclass),
  "task" varchar(255) COLLATE "pg_catalog"."default",
  "update_time" timestamptz(6) NOT NULL,
  "create_time" timestamptz(6) NOT NULL,
  "detect_type_id" int4,
  "picture_name_id" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of eye_detect
-- ----------------------------

-- ----------------------------
-- Table structure for eye_detectserver
-- ----------------------------
DROP TABLE IF EXISTS "public"."eye_detectserver";
CREATE TABLE "public"."eye_detectserver" (
  "detect_id" int8 NOT NULL DEFAULT nextval('eye_detectserver_detect_id_seq'::regclass),
  "detect_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "detect_url" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of eye_detectserver
-- ----------------------------

-- ----------------------------
-- Table structure for eye_detecttype
-- ----------------------------
DROP TABLE IF EXISTS "public"."eye_detecttype";
CREATE TABLE "public"."eye_detecttype" (
  "detect_type" int4 NOT NULL,
  "detect_describe" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of eye_detecttype
-- ----------------------------

-- ----------------------------
-- Table structure for eye_picture
-- ----------------------------
DROP TABLE IF EXISTS "public"."eye_picture";
CREATE TABLE "public"."eye_picture" (
  "picture_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "path" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "task" int4 NOT NULL,
  "recognition" int4,
  "update_time" timestamptz(6) NOT NULL,
  "create_time" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of eye_picture
-- ----------------------------

-- ----------------------------
-- Table structure for eye_result
-- ----------------------------
DROP TABLE IF EXISTS "public"."eye_result";
CREATE TABLE "public"."eye_result" (
  "id" int8 NOT NULL DEFAULT nextval('eye_result_id_seq'::regclass),
  "x_min" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "y_min" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "x_max" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "y_max" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "confidence" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "classno" int4 NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "update_time" date,
  "create_time" date,
  "picture_name_id" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of eye_result
-- ----------------------------

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_group_id_seq"
OWNED BY "public"."auth_group"."id";
SELECT setval('"public"."auth_group_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_group_permissions_id_seq"
OWNED BY "public"."auth_group_permissions"."id";
SELECT setval('"public"."auth_group_permissions_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_permission_id_seq"
OWNED BY "public"."auth_permission"."id";
SELECT setval('"public"."auth_permission_id_seq"', 45, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_user_groups_id_seq"
OWNED BY "public"."auth_user_groups"."id";
SELECT setval('"public"."auth_user_groups_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_user_id_seq"
OWNED BY "public"."auth_user"."id";
SELECT setval('"public"."auth_user_id_seq"', 2, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_user_user_permissions_id_seq"
OWNED BY "public"."auth_user_user_permissions"."id";
SELECT setval('"public"."auth_user_user_permissions_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."django_admin_log_id_seq"
OWNED BY "public"."django_admin_log"."id";
SELECT setval('"public"."django_admin_log_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."django_content_type_id_seq"
OWNED BY "public"."django_content_type"."id";
SELECT setval('"public"."django_content_type_id_seq"', 12, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."django_migrations_id_seq"
OWNED BY "public"."django_migrations"."id";
SELECT setval('"public"."django_migrations_id_seq"', 20, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."eye_detect_id_seq"
OWNED BY "public"."eye_detect"."id";
SELECT setval('"public"."eye_detect_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."eye_detectserver_detect_id_seq"
OWNED BY "public"."eye_detectserver"."detect_id";
SELECT setval('"public"."eye_detectserver_detect_id_seq"', 15, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."eye_result_id_seq"
OWNED BY "public"."eye_result"."id";
SELECT setval('"public"."eye_result_id_seq"', 58, true);

-- ----------------------------
-- Indexes structure for table auth_group
-- ----------------------------
CREATE INDEX "auth_group_name_a6ea08ec_like" ON "public"."auth_group" USING btree (
  "name" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group
-- ----------------------------
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table auth_group
-- ----------------------------
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_group_permissions
-- ----------------------------
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "public"."auth_group_permissions" USING btree (
  "group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "public"."auth_group_permissions" USING btree (
  "permission_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id");

-- ----------------------------
-- Primary Key structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "public"."auth_permission" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename");

-- ----------------------------
-- Primary Key structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_user
-- ----------------------------
CREATE INDEX "auth_user_username_6821ab7c_like" ON "public"."auth_user" USING btree (
  "username" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_user
-- ----------------------------
ALTER TABLE "public"."auth_user" ADD CONSTRAINT "auth_user_username_key" UNIQUE ("username");

-- ----------------------------
-- Primary Key structure for table auth_user
-- ----------------------------
ALTER TABLE "public"."auth_user" ADD CONSTRAINT "auth_user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_user_groups
-- ----------------------------
CREATE INDEX "auth_user_groups_group_id_97559544" ON "public"."auth_user_groups" USING btree (
  "group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "public"."auth_user_groups" USING btree (
  "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_user_groups
-- ----------------------------
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id");

-- ----------------------------
-- Primary Key structure for table auth_user_groups
-- ----------------------------
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_user_user_permissions
-- ----------------------------
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "public"."auth_user_user_permissions" USING btree (
  "permission_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "public"."auth_user_user_permissions" USING btree (
  "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_user_user_permissions
-- ----------------------------
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id");

-- ----------------------------
-- Primary Key structure for table auth_user_user_permissions
-- ----------------------------
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table django_admin_log
-- ----------------------------
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "public"."django_admin_log" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "public"."django_admin_log" USING btree (
  "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Checks structure for table django_admin_log
-- ----------------------------
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_action_flag_check" CHECK (action_flag >= 0);

-- ----------------------------
-- Primary Key structure for table django_admin_log
-- ----------------------------
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");

-- ----------------------------
-- Primary Key structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table django_migrations
-- ----------------------------
ALTER TABLE "public"."django_migrations" ADD CONSTRAINT "django_migrations_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table django_session
-- ----------------------------
CREATE INDEX "django_session_expire_date_a5c62663" ON "public"."django_session" USING btree (
  "expire_date" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);
CREATE INDEX "django_session_session_key_c0390e0f_like" ON "public"."django_session" USING btree (
  "session_key" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table django_session
-- ----------------------------
ALTER TABLE "public"."django_session" ADD CONSTRAINT "django_session_pkey" PRIMARY KEY ("session_key");

-- ----------------------------
-- Indexes structure for table eye_detect
-- ----------------------------
CREATE INDEX "eye_detect_detect_type_id_7b1db9f7" ON "public"."eye_detect" USING btree (
  "detect_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "eye_detect_picture_name_id_bd23101e" ON "public"."eye_detect" USING btree (
  "picture_name_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "eye_detect_picture_name_id_bd23101e_like" ON "public"."eye_detect" USING btree (
  "picture_name_id" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table eye_detect
-- ----------------------------
ALTER TABLE "public"."eye_detect" ADD CONSTRAINT "eye_detect_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table eye_detectserver
-- ----------------------------
ALTER TABLE "public"."eye_detectserver" ADD CONSTRAINT "eye_detectserver_pkey" PRIMARY KEY ("detect_id");

-- ----------------------------
-- Primary Key structure for table eye_detecttype
-- ----------------------------
ALTER TABLE "public"."eye_detecttype" ADD CONSTRAINT "eye_detecttype_pkey" PRIMARY KEY ("detect_type");

-- ----------------------------
-- Indexes structure for table eye_picture
-- ----------------------------
CREATE INDEX "eye_picture_picture_name_aa6ca872_like" ON "public"."eye_picture" USING btree (
  "picture_name" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Checks structure for table eye_picture
-- ----------------------------
ALTER TABLE "public"."eye_picture" ADD CONSTRAINT "eye_picture_task_check" CHECK (task >= 0);
ALTER TABLE "public"."eye_picture" ADD CONSTRAINT "eye_picture_recognition_check" CHECK (recognition >= 0);

-- ----------------------------
-- Primary Key structure for table eye_picture
-- ----------------------------
ALTER TABLE "public"."eye_picture" ADD CONSTRAINT "eye_picture_pkey" PRIMARY KEY ("picture_name");

-- ----------------------------
-- Indexes structure for table eye_result
-- ----------------------------
CREATE INDEX "eye_result_picture_name_id_a71faf37" ON "public"."eye_result" USING btree (
  "picture_name_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "eye_result_picture_name_id_a71faf37_like" ON "public"."eye_result" USING btree (
  "picture_name_id" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table eye_result
-- ----------------------------
ALTER TABLE "public"."eye_result" ADD CONSTRAINT "eye_result_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_user_groups
-- ----------------------------
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_user_user_permissions
-- ----------------------------
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table django_admin_log
-- ----------------------------
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table eye_detect
-- ----------------------------
ALTER TABLE "public"."eye_detect" ADD CONSTRAINT "eye_detect_detect_type_id_7b1db9f7_fk_eye_detec" FOREIGN KEY ("detect_type_id") REFERENCES "public"."eye_detecttype" ("detect_type") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."eye_detect" ADD CONSTRAINT "eye_detect_picture_name_id_bd23101e_fk_eye_picture_picture_name" FOREIGN KEY ("picture_name_id") REFERENCES "public"."eye_picture" ("picture_name") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table eye_result
-- ----------------------------
ALTER TABLE "public"."eye_result" ADD CONSTRAINT "eye_result_picture_name_id_a71faf37_fk_eye_picture_picture_name" FOREIGN KEY ("picture_name_id") REFERENCES "public"."eye_picture" ("picture_name") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
