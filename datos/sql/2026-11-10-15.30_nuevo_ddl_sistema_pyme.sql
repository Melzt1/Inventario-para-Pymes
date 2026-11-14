-- Nuevo esquema completo del sistema_pyme en base al MER actualizado.
DROP DATABASE IF EXISTS sistema_pyme;
CREATE DATABASE IF NOT EXISTS sistema_pyme;
USE sistema_pyme;

CREATE TABLE direcciones (
    id_direccion INTEGER AUTO_INCREMENT,
    calle VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NULL,
    ciudad VARCHAR(100) NOT NULL,
    comuna VARCHAR(100) NULL,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion)
);

CREATE TABLE categorias (
    id_categoria INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1, -- ACTIVO/INACTIVO para un borrado logico

    CONSTRAINT pk_categorias PRIMARY KEY (id_categoria),
    CONSTRAINT uk_categorias_nombre UNIQUE (nombre),
    CONSTRAINT ck_categorias_estado CHECK (estado IN (0, 1))
);

CREATE TABLE roles (
    id_rol INTEGER AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT pk_roles PRIMARY KEY (id_rol),
    CONSTRAINT uk_roles_nombre UNIQUE (nombre)
);

CREATE TABLE proveedores (
    id_proveedor INTEGER AUTO_INCREMENT,
    rut VARCHAR(12) NULL, -- Null: pueden existir proveedores extranjeros
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1, 
    id_direccion INTEGER NOT NULL,

    CONSTRAINT pk_proveedores PRIMARY KEY (id_proveedor),
    CONSTRAINT uk_proveedores_rut UNIQUE (rut),
    CONSTRAINT uk_proveedores_correo UNIQUE (correo),
    CONSTRAINT ck_proveedores_estado CHECK (estado IN (0, 1)),
    CONSTRAINT fk_proveedores_direcciones FOREIGN KEY (id_direccion)
        REFERENCES direcciones (id_direccion) ON DELETE RESTRICT
);

CREATE TABLE productos (
    id_producto INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    sku VARCHAR(100) NOT NULL,
    precio_costo DECIMAL(12,4) NOT NULL,
    precio_venta DECIMAL(12,2) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    fecha_elaboracion DATE NULL,
    fecha_vencimiento DATE NULL, -- NULL: Pueden existir productos NO perecibles
    estado TINYINT(1) NOT NULL DEFAULT 1,
    id_categoria INTEGER NOT NULL,

    CONSTRAINT pk_productos PRIMARY KEY (id_producto),
    CONSTRAINT uk_productos_sku UNIQUE (sku),
    CONSTRAINT ck_productos_precios CHECK (precio_costo > 0 AND precio_venta > 0),
    CONSTRAINT ck_productos_estado CHECK (estado IN (0, 1)),
    CONSTRAINT fk_productos_categorias FOREIGN KEY (id_categoria)
        REFERENCES categorias (id_categoria) ON DELETE RESTRICT
);

CREATE TABLE almacenes (
    id_almacen INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1,
    id_direccion INTEGER NOT NULL,

    CONSTRAINT pk_almacenes PRIMARY KEY (id_almacen),
    CONSTRAINT uk_almacenes_nombre UNIQUE (nombre),
    CONSTRAINT ck_almacenes_estado CHECK (estado IN (0, 1)),
    CONSTRAINT fk_almacenes_direcciones FOREIGN KEY (id_direccion)
        REFERENCES direcciones (id_direccion) ON DELETE RESTRICT
);

CREATE TABLE secciones (
    id_seccion INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1,
    id_almacen INTEGER NOT NULL,

    CONSTRAINT pk_secciones PRIMARY KEY (id_seccion),

    -- Restriccion para evitar nombres de secciones repetidos dentro del mismo almacen
    CONSTRAINT uk_secciones_almacen_nombre UNIQUE (id_almacen, nombre),
    CONSTRAINT ck_secciones_estado CHECK (estado IN (0, 1)),
    CONSTRAINT fk_secciones_almacenes FOREIGN KEY (id_almacen)
        REFERENCES almacenes (id_almacen) ON DELETE RESTRICT
);

CREATE TABLE usuarios (
    id_usuario INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    estado TINYINT(1) NOT NULL DEFAULT 1,
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_rol INTEGER NOT NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),
    CONSTRAINT uk_usuarios_usuario UNIQUE (usuario),
    CONSTRAINT ck_usuarios_estado CHECK (estado IN (0, 1)),
    CONSTRAINT fk_usuarios_roles FOREIGN KEY (id_rol)
        REFERENCES roles (id_rol) ON DELETE RESTRICT
);

CREATE TABLE producto_proveedor (
    id_producto INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,
    es_principal TINYINT(1) NOT NULL DEFAULT 0,

    CONSTRAINT pk_producto_proveedor PRIMARY KEY (id_producto, id_proveedor),
    CONSTRAINT ck_producto_proveedor_principal CHECK (es_principal IN (0, 1)),
    CONSTRAINT fk_producto_proveedor_producto FOREIGN KEY (id_producto)
        REFERENCES productos (id_producto) ON DELETE RESTRICT,
    CONSTRAINT fk_producto_proveedor_proveedor FOREIGN KEY (id_proveedor)
        REFERENCES proveedores (id_proveedor) ON DELETE RESTRICT
);

CREATE TABLE usuario_almacen (
    id_usuario INTEGER NOT NULL,
    id_almacen INTEGER NOT NULL,
    es_encargado TINYINT(1) NOT NULL DEFAULT 0,

    CONSTRAINT pk_usuario_almacen PRIMARY KEY (id_usuario, id_almacen),
    CONSTRAINT ck_usuario_almacen_encargado CHECK (es_encargado IN (0, 1)),
    CONSTRAINT fk_usuario_almacen_usuario FOREIGN KEY (id_usuario)
        REFERENCES usuarios (id_usuario) ON DELETE RESTRICT,
    CONSTRAINT fk_usuario_almacen_almacen FOREIGN KEY (id_almacen)
        REFERENCES almacenes (id_almacen) ON DELETE RESTRICT
);

CREATE TABLE minimos_almacen (
    id_producto INTEGER NOT NULL,
    id_almacen INTEGER NOT NULL,
    stock_minimo INTEGER NOT NULL,

    CONSTRAINT pk_minimos_almacen PRIMARY KEY (id_producto, id_almacen),
    CONSTRAINT ck_minimos_almacen_stock CHECK (stock_minimo >= 0),
    CONSTRAINT fk_minimos_almacen_producto FOREIGN KEY (id_producto)
        REFERENCES productos (id_producto) ON DELETE RESTRICT,
    CONSTRAINT fk_minimos_almacen_almacen FOREIGN KEY (id_almacen)
        REFERENCES almacenes (id_almacen) ON DELETE RESTRICT
);

CREATE TABLE inventarios (
    id_inventario INTEGER AUTO_INCREMENT,
    id_producto INTEGER NOT NULL,
    id_seccion INTEGER NOT NULL,
    stock_actual INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT pk_inventarios PRIMARY KEY (id_inventario),

    -- restriccion para evitar registrar el mismo producto mas de una vez en la misma seccion.
    CONSTRAINT uk_inventarios_producto_seccion UNIQUE (id_producto, id_seccion),

    CONSTRAINT ck_inventarios_stock CHECK (stock_actual >= 0),
    CONSTRAINT fk_inventarios_producto FOREIGN KEY (id_producto)
        REFERENCES productos (id_producto) ON DELETE RESTRICT,
    CONSTRAINT fk_inventarios_seccion FOREIGN KEY (id_seccion)
        REFERENCES secciones (id_seccion) ON DELETE RESTRICT
);

CREATE TABLE movimientos (
    id_movimiento INTEGER AUTO_INCREMENT,
    descripcion VARCHAR(255) NOT NULL,
    cantidad INTEGER NOT NULL,
    tipo VARCHAR(7) NOT NULL, -- ENTRADA/SALIDA
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_inventario INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,

    CONSTRAINT pk_movimientos PRIMARY KEY (id_movimiento),
    CONSTRAINT ck_movimientos_cantidad CHECK (cantidad > 0),
    CONSTRAINT ck_movimientos_tipo CHECK (tipo IN ('ENTRADA', 'SALIDA')),
    CONSTRAINT fk_movimientos_inventarios FOREIGN KEY (id_inventario)
        REFERENCES inventarios (id_inventario) ON DELETE RESTRICT,
    CONSTRAINT fk_movimientos_usuarios FOREIGN KEY (id_usuario)
        REFERENCES usuarios (id_usuario) ON DELETE RESTRICT
);
