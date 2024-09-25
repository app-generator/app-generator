
-- Table: api_user_user
CREATE TABLE IF NOT EXISTS "api_user_user" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "password" VARCHAR(255) NOT NULL,
  "last_login" DATETIME,
  "is_superuser" INTEGER NOT NULL,
  "username" VARCHAR(255) NOT NULL,
  "email" VARCHAR(255) NOT NULL,
  "is_active" INTEGER NOT NULL,
  "date" DATETIME NOT NULL
);

-- Table: api_authentication_activesession
CREATE TABLE IF NOT EXISTS "api_authentication_activesession" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "token" VARCHAR(255) NOT NULL,
  "date" DATETIME NOT NULL,
  "user_id" INTEGER NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "api_user_user" ("id")
);

-- Table: auth_group
CREATE TABLE IF NOT EXISTS "auth_group" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL
);

-- Table: api_user_user_groups
CREATE TABLE IF NOT EXISTS "api_user_user_groups" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "user_id" INTEGER NOT NULL,
  "group_id" INTEGER NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "api_user_user" ("id"),
  FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id")
);

-- Table: django_content_type
CREATE TABLE IF NOT EXISTS "django_content_type" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "app_label" VARCHAR(255) NOT NULL,
  "model" VARCHAR(255) NOT NULL
);

-- Table: auth_permission
CREATE TABLE IF NOT EXISTS "auth_permission" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "content_type_id" INTEGER NOT NULL,
  "codename" VARCHAR(255) NOT NULL,
  "name" VARCHAR(255) NOT NULL,
  FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id")
);

-- Table: api_user_user_user_permissions
CREATE TABLE IF NOT EXISTS "api_user_user_user_permissions" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "user_id" INTEGER NOT NULL,
  "permission_id" INTEGER NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "api_user_user" ("id"),
  FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id")
);

-- Table: auth_group_permissions
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "group_id" INTEGER NOT NULL,
  "permission_id" INTEGER NOT NULL,
  FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id"),
  FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id")
);

-- Table: django_admin_log
CREATE TABLE IF NOT EXISTS "django_admin_log" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "action_time" DATETIME NOT NULL,
  "object_id" TEXT,
  "object_repr" VARCHAR(255) NOT NULL,
  "change_message" TEXT NOT NULL,
  "content_type_id" INTEGER,
  "user_id" INTEGER NOT NULL,
  "action_flag" INTEGER NOT NULL,
  FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id"),
  FOREIGN KEY ("user_id") REFERENCES "api_user_user" ("id")
);

-- Table: django_migrations
CREATE TABLE IF NOT EXISTS "django_migrations" (
  "id" INTEGER NOT NULL PRIMARY KEY,
  "app" VARCHAR(255) NOT NULL,
  "name" VARCHAR(255) NOT NULL,
  "applied" DATETIME NOT NULL
);

-- Table: django_session
CREATE TABLE IF NOT EXISTS "django_session" (
  "session_key" VARCHAR(255) NOT NULL PRIMARY KEY,
  "session_data" TEXT NOT NULL,
  "expire_date" DATETIME NOT NULL
);
