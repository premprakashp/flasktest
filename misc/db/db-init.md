# Db setup

## Create database

```bash
CREATE DATABASE IF NOT EXISTS flaskapp CHARACTER SET 'utf8';

GRANT ALL PRIVILEGES ON flaskapp.* TO 'pprakash'@'localhost';


CREATE TABLE `flaskapp`.`user` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  `password` VARCHAR(150) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  `loginid` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE INDEX `loginid_idx` (`loginid` ASC) VISIBLE);
```