ALTER TABLE direcciones
COMMENT = 'Informacion de direccion asociada a Proveedores y Almacenes';

ALTER TABLE categorias
COMMENT = 'Informacion de las categorias utilizadas para clasificar los productos';

ALTER TABLE proveedores
COMMENT = 'Tabla de proveedores de productos';

ALTER TABLE productos
COMMENT = 'Informacion comercial de los productos, incluyendo precios, categoria y fechas de elaboracion y vencimiento';

ALTER TABLE producto_proveedor
COMMENT = 'Relacion entre productos y proveedores, identificando el proveedor principal de cada producto';

ALTER TABLE almacenes
COMMENT = 'Informacion de los almacenes donde se almacenan los productos de la empresa';

ALTER TABLE stocks
COMMENT = 'Informacion del stock actual y nivel minimo de productos almacenados';

ALTER TABLE inventarios
COMMENT = 'Relacion entre productos, almacenes y su respectivo stock';

ALTER TABLE movimientos
COMMENT = 'Registro historico de entradas y salidas de productos en el inventario';