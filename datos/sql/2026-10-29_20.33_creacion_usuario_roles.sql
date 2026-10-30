USE sistema_pyme;

-- ROLES
CREATE TABLE roles(
    id_rol INTEGER AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT pk_rol PRIMARY KEY (id_rol),
    CONSTRAINT uk_nombre UNIQUE (nombre)
);

-- USUARIOS
CREATE TABLE usuarios(
    id_usuario INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    estado TINYINT(1) DEFAULT 1 NOT NULL, -- ACTIVO/INACTIVO para un borrado logico
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    id_rol INTEGER NOT NULL,
    id_almacen INTEGER NOT NULL,

    CONSTRAINT pk_id_usuario PRIMARY KEY (id_usuario),
    CONSTRAINT uk_nombre_usuario UNIQUE (usuario),

    CONSTRAINT fk_usuario_rol FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    CONSTRAINT fk_usuario_almacen FOREIGN KEY (id_almacen) REFERENCES almacenes(id_almacen)
);

-- Se relaciona con usuario para saber que trajador ejecuto "x" movimiento
ALTER TABLE movimientos
    ADD COLUMN id_usuario INTEGER NOT NULL,
    ADD CONSTRAINT fk_movimientos_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario);
        
-- Usuario se relacion con Almacen, un trabajador (usuario) trabaja en un almacen
ALTER TABLE almacenes
    ADD COLUMN id_encargado INTEGER NULL,
    ADD CONSTRAINT fk_almacen_usuario
        FOREIGN KEY (id_encargado) 
        REFERENCES usuarios(id_usuario);

-- Ahora el encargado se obtiene de la relacion con Usuarios (id_encargado)	
ALTER TABLE almacenes
	DROP COLUMN encargado;        