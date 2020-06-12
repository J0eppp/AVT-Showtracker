CREATE TABLE `shows` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `description` TEXT NOT NULL,
    `date` DATETIME NOT NULL
);

CREATE TABLE `files` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `url` TEXT NOT NULL,
    `file_name` TEXT NOT NULL,
    `show_name` TEXT NOT NULL
);