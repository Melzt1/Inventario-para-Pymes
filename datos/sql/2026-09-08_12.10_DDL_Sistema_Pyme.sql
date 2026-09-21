CREATE DATABASE sistema_pyme;
USE sistema_pyme;

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
    descripcion VARCHAR(255) NOT NULL,

    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE proveedores(
    id_proveedor INTEGER AUTO_INCREMENT,
    rut VARCHAR(12) UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE,
    telefono VARCHAR(9) UNIQUE NOT NULL,
    estado TINYINT(1) DEFAULT 1 NOT NULL, -- ACTIVO/INACTIVO para un borrado logico
    id_direccion INTEGER NOT NULL,

    CONSTRAINT pk_proveedor PRIMARY KEY (id_proveedor),

    CONSTRAINT fk_proveedor_direccion FOREIGN KEY (id_direccion) REFERENCES direcciones(id_direccion)
    -- CHECK para que estado solo pueda ser 0 o 1.
    CHECK (estado IN (0,1))
);

CREATE TABLE productos(
    id_producto INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    sku VARCHAR(100) UNIQUE NOT NULL,
    precio_costo INT NOT NULL,
    precio_venta INT NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    fecha_elaboracion DATE NULL,
    fecha_vencimiento DATE NULL, -- Pueden existir productos NO perecibles
    estado TINYINT(1) DEFAULT 1 NOT NULL, -- ACTIVO/INACTIVO para un borrado logico
    id_categoria INTEGER NOT NULL,

    CONSTRAINT pk_producto PRIMARY KEY (id_producto),
    CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    
    -- CHECK para validar que si agregan una fecha de elaboracion y una fecha de vencimiento, la fecha de vencimiento sea mayor o igual a la fecha de elaboracion.
    CHECK (fecha_elaboracion IS NULL OR fecha_vencimiento IS NULL OR fecha_vencimiento >= fecha_elaboracion),

    -- CHECK para que estado solo pueda ser 0 o 1.
    CHECK (estado IN (0,1))
);

-- RELACION PRODUCTO - PROVEEDOR
CREATE TABLE producto_proveedor(
    id_producto INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,
    es_principal TINYINT(1) DEFAULT 0 NOT NULL,  -- AGREGUE EL NOT NULL PARA IMPEDIR EL ESTADO NULL Y MANTENER SOLO 0 o 1

    -- PRIMARY KEY COMPUESTA
    CONSTRAINT pk_producto_proveedor PRIMARY KEY (id_producto, id_proveedor),

    CONSTRAINT fk_producto_proveedor_producto FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    CONSTRAINT fk_producto_proveedor_proveedor FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor),
    CHECK (es_principal IN (0,1)) -- Para chequear que el valor de es_principal sea 0 o 1 y no permita mas valores.
);


CREATE TABLE almacenes(
    id_almacen INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    encargado VARCHAR(50) NOT NULL,
    estado TINYINT(1) DEFAULT 1 NOT NULL, -- ACTIVO/INACTIVO para un borrado logico
    id_direccion INTEGER NOT NULL,

    CONSTRAINT pk_almacen PRIMARY KEY (id_almacen),

    CONSTRAINT fk_almacen_direccion FOREIGN KEY (id_direccion) REFERENCES direcciones(id_direccion)
    -- CHECK para que estado solo pueda ser 0 o 1.
    CHECK (estado IN (0,1))
);

CREATE TABLE stocks(
    id_stock INTEGER AUTO_INCREMENT,
    stock_actual INTEGER NOT NULL,
    stock_minimo INTEGER NOT NULL,

    CONSTRAINT pk_stock PRIMARY KEY (id_stock),
    CONSTRAINT ck_stock_actual CHECK (stock_actual >= 0),
    CONSTRAINT ck_stock_minimo CHECK (stock_minimo >= 0)
);

CREATE TABLE inventarios(
    id_inventario INTEGER AUTO_INCREMENT,
    id_producto INTEGER NOT NULL,
    id_almacen INTEGER NOT NULL,
    id_stock INTEGER NOT NULL,

    CONSTRAINT pk_inventario PRIMARY KEY (id_inventario),

    CONSTRAINT fk_inventario_producto FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
    CONSTRAINT fk_inventario_almacen FOREIGN KEY (id_almacen) REFERENCES almacenes(id_almacen),
    CONSTRAINT fk_inventario_stock FOREIGN KEY (id_stock) REFERENCES stocks(id_stock),

    -- Evita que un mismo producto tenga mas de un registro de inventario dentro del mismo almacen.
    -- Evitar que se dupliquen registros del mismo producto en la misma bodega.
    CONSTRAINT uk_inventario_producto_almacen UNIQUE (id_producto, id_almacen),
    CONSTRAINT uk_inventario_stock UNIQUE (id_stock) -- 1:1 con stock
);

CREATE TABLE movimientos(
    id_movimiento INTEGER AUTO_INCREMENT,
    descripcion VARCHAR(255),
    cantidad INTEGER NOT NULL,
    tipo ENUM('ENTRADA','SALIDA') NOT NULL, 
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_inventario INTEGER NOT NULL,

    CONSTRAINT pk_movimiento PRIMARY KEY (id_movimiento),

    CONSTRAINT fk_movimiento_inventario FOREIGN KEY (id_inventario) REFERENCES inventarios(id_inventario),
    CONSTRAINT ck_movimiento_cantidad CHECK (cantidad > 0)
);