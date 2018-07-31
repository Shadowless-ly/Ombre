

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `users`;
CREATE TABLE users( 
  `id` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `role_id` INT DEFAULT 0,
  `mail` VARCHAR(50) NOT NULL,
  `created_at` REAL NOT NULL,
  KEY `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `post`;
CREATE TABLE post(
  `id` VARCHAR(50) NOT NULL,
  `plate` INT NOT NULL,
  `content` MEDIUMTEXT,
  `user_id` VARCHAR(50) NOT NULL,
  `user_name` VARCHAR(50) NOT NULL,
  `user_image` VARCHAR(500),
  `name` VARCHAR(50),
  `created_at` REAL NOT NULL,
  KEY `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `comments`;
CREATE TABLE comments(
  `id` VARCHAR(50) NOT NULL,
  `post_id` VARCHAR(50) NOT NULL,
  `user_id` VARCHAR(50) NOT NULL,
  `user_name` VARCHAR(50) NOT NULL,
  `user_image` VARCHAR(500),
  `content` MEDIUMTEXT,
  `created_at` REAL NOT NULL,
  KEY `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `role`;
CREATE TABLE role(
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `enable` BOOL NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `plate`;
CREATE TABLE plate(
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `manager_role_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8