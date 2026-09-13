CREATE DATABASE sistema_pymme;
USE sistema_pymme;

CREATE TABLE direcciones(
    id_direccion INTEGER AUTO_INCREMENT,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NULL,
    comuna VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,

    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion)
);

CREATE TABLE categorias(
    id_categoria INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NOT NULL

    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE proveedores(
    id_proveedor INTEGER AUTO_INCREMENT,
    rut VARCHAR(12) UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE,
    telefono VARCHAR(9) UNIQUE NOT NULL,
    id_direccion INTEGER NOT NULL,

    CONSTRAINT pk_proveedor PRIMARY KEY (id_proveedor),

    CONSTRAINT fk_proveedor_direccion FOREIGN KEY (id_direccion) REFERENCES direcciones(id_direccion)
);

CREATE TABLE productos(
    id_producto INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    sku VARCHAR(100) UNIQUE NOT NULL,
    precio INT NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    id_categoria INTEGER NOT NULL,
    id_proveedor_principal INTEGER NOT NULL,

    CONSTRAINT pk_producto PRIMARY KEY (id_producto),

    CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    CONSTRAINT fk_producto_proveedor FOREIGN KEY (id_proveedor_principal) REFERENCES proveedores(id_proveedor)
);

-- RELACION PRODUCTO - PROVEEDOR
CREATE TABLE producto_proveedor(
    id_producto INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,

    -- PRIMARY KEY COMPUESTA
    CONSTRAINT pk_producto_proveedor PRIMARY KEY (id_producto, id_proveedor),

    CONSTRAINT fk_producto_proveedor_producto FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    CONSTRAINT fk_producto_proveedor_proveedor FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
):

CREATE TABLE productos_perecibles(
    id_producto INTEGER,
    fecha_vencimiento DATE NOT NULL,

    CONSTRAINT pk_producto_perecible PRIMARY KEY (id_producto),

    CONSTRAINT fk_producto_perecible FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE productos_no_perecibles(
    id_producto INTEGER,

    CONSTRAINT pk_producto_no_perecible PRIMARY KEY (id_producto),

    CONSTRAINT fk_producto_no_perecible FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE almacenes(
    id_almacen INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    encargado VARCHAR(50) NOT NULL,
    id_direccion INTEGER NOT NULL,

    CONSTRAINT pk_almacen PRIMARY KEY (id_almacen),

    CONSTRAINT fk_almacen_direccion FOREIGN KEY (id_direccion) REFERENCES direcciones(id_direccion)
);

CREATE TABLE inventarios(
    id_inventario INTEGER AUTO_INCREMENT,
    stock_actual INTEGER NOT NULL,
    stock_min INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    id_almacen INTEGER NOT NULL,

    CONSTRAINT pk_inventario PRIMARY KEY (id_inventario),

    CONSTRAINT fk_inventario_producto FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    CONSTRAINT fk_inventario_almacen FOREIGN KEY (id_almacen) REFERENCES almacenes(id_almacen),

    -- Evita que un mismo producto tenga mas de un registro de inventario dentro del mismo almacen.
    CONSTRAINT uk_inventario_producto_almacen UNIQUE (id_producto, id_almacen)
);

CREATE TABLE movimientos(
    id_movimiento INTEGER AUTO_INCREMENT,
    descripcion VARCHAR(255),
    cantidad INTEGER NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_inventario INTEGER NOT NULL,

    CONSTRAINT pk_movimiento PRIMARY KEY (id_movimiento),
    
    CONSTRAINT fk_movimiento_inventario FOREIGN KEY (id_inventario) REFERENCES inventarios(id_inventario)
);