# Prueba desarrollador backend Habi

## Planteamiento de la solucion

- Para la creacion de la API no se utilizaran frameworks sino librerias internas de Python como http.
- Para la conexion a la base de datos no se utilizara ninguna ORM sino librerias externas de Python como mysql-connector-python.
- Se propene el siguiente esquema como solucion como punto inicial de la solucion:

![arquitectura](./img/arquitectura.png "arquitectura")

- El desarrollodo de la API se realizara guiada por pruebas (TDD)

Como todo proyecto, mientras se trabaja en el se van realizando cambios que se consideran pertinentes, aun asi, tener un modelo esquema te permite tener una idea clara de lo que quiere lograr como PMV

## Servicio "Me gusta"

Para implementar el microservicio de me gustas, se propone expandir los modelos de las bases de datos como sugiere el siguiente esquema:

![modelos likes](./img/modelo_likes.png "modelo likes")

Codigo SQL para extender los modelos de la base de datos
```SQL
-- -----------------------------------------------------
-- Table `habi_db`.`property`
-- -----------------------------------------------------

ALTER TABLE `habi_db`.`property`
ADD likes INT;

-- -----------------------------------------------------
-- Table `habi_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi_db`.`users` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `phone` TINYINT NOT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `habi_db`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi_db`.`likes` (
  `property_id` INT(11) NOT NULL,
  `users_id` INT NOT NULL,
  `id` INT NOT NULL,
  INDEX `fk_likes_property1_idx` (`property_id` ASC) VISIBLE,
  INDEX `fk_likes_users1_idx` (`users_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_likes_property1`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_db`.`property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `habi_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
```