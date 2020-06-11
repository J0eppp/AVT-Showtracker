CREATE TABLE `shows` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `description` TEXT NOT NULL,
    `date` DATETIME NOT NULL
);
