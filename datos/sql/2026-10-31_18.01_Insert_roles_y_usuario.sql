-- ATENCION!
-- ESTOS DATOS SON SOLO DE PRUEBA PARA TESTEAR LOS METODOS DE SESION
-- PROBABLEMENTE EN EL FUTURO NO EXISTA LA TABLA ROLES Y SOLO SEA UN DATO DE LA TABLA USUARIOS

INSERT INTO roles (nombre) VALUES
('Administrador'),
('Trabajador');

INSERT INTO usuarios (nombre, usuario, contrasena, id_rol, id_almacen) VALUES
('Don Migajero', 'melzt', '12345678', 1, 1);