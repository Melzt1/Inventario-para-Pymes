-- =====================================================================
-- ** ESTE SCRIPT SQL FUE GENERADO POR IA ESPECIFICAMENTE PARA TESTEAR ** 
-- ** ESTE SCRIPT SQL FUE GENERADO POR IA ESPECIFICAMENTE PARA TESTEAR ** 
-- ** ESTE SCRIPT SQL FUE GENERADO POR IA ESPECIFICAMENTE PARA TESTEAR ** 

-- Datos de prueba: PYME de Comercio Electronico / Marketplace
-- Generado: 2026-10-20
--
-- Contenido:
--   8 categorias | 9 proveedores | 3 almacenes
--   24 productos | 40 inventarios | 26 movimientos
--   18 productos con proveedor principal, 5 con proveedor secundario
--   6 productos SIN proveedor (ids 4, 9, 12, 15, 20, 24) para asignar a mano
--
-- Todas las entidades con columna estado quedan en 1 (activas).
-- Descripciones de producto breves para que prettytable no se rompa.
-- =====================================================================

USE sistema_pyme;

-- ---------------------------------------------------------------------
-- 1) LIMPIEZA (borra los datos previos respetando las claves foraneas)
-- ---------------------------------------------------------------------
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM movimientos;
DELETE FROM producto_proveedor;
DELETE FROM inventarios;
DELETE FROM productos;
DELETE FROM proveedores;
DELETE FROM almacenes;
DELETE FROM categorias;
DELETE FROM direcciones;
SET FOREIGN_KEY_CHECKS = 1;
SET SQL_SAFE_UPDATES = 1;

-- ---------------------------------------------------------------------
-- 2) DIRECCIONES
-- ---------------------------------------------------------------------
INSERT INTO direcciones (id_direccion, calle, numero, comuna, ciudad) VALUES
(1, 'Av. Providencia', '1248', 'Providencia', 'Santiago'),
(2, 'San Antonio', '425', 'Santiago', 'Santiago'),
(3, 'Av. Irarrazaval', '3400', 'Nunoa', 'Santiago'),
(4, 'Av. Apoquindo', '4501', 'Las Condes', 'Santiago'),
(5, 'Av. Colon', '8500', 'San Bernardo', 'Santiago'),
(6, 'Av. Matta', '1440', 'Santiago', 'Santiago'),
(7, 'Av. Vicuna Mackenna', '7200', 'La Florida', 'Santiago'),
(8, 'Av. Pajaritos', '3200', 'Maipu', 'Santiago'),
(9, 'Av. El Bosque', '500', 'Pudahuel', 'Santiago'),
(10, 'Av. Vicuna Mackenna', '4860', 'Macul', 'Santiago'),
(11, 'Av. Americo Vespucio', '1234', 'Quilicura', 'Santiago'),
(12, 'Camino a Melipilla', '5500', 'Maipu', 'Santiago');

-- ---------------------------------------------------------------------
-- 3) CATEGORIAS
-- ---------------------------------------------------------------------
INSERT INTO categorias (id_categoria, nombre, descripcion, estado) VALUES
(1, 'Electronica', 'Dispositivos y accesorios tecnologicos.', 1),
(2, 'Hogar y Cocina', 'Articulos para el hogar y la cocina.', 1),
(3, 'Deportes', 'Equipamiento y accesorios deportivos.', 1),
(4, 'Belleza', 'Cuidado personal y cosmetica.', 1),
(5, 'Mascotas', 'Alimentos y accesorios para mascotas.', 1),
(6, 'Moda', 'Ropa, calzado y accesorios de moda.', 1),
(7, 'Papeleria', 'Cuadernos, escritura y oficina.', 1),
(8, 'Infantil', 'Juguetes y articulos para ninos.', 1);

-- ---------------------------------------------------------------------
-- 4) PROVEEDORES
-- ---------------------------------------------------------------------
INSERT INTO proveedores (id_proveedor, rut, nombre, correo, telefono, estado, id_direccion) VALUES
(1, '76.543.210-3', 'Tecnologia Andina SpA', 'contacto@tecnoandina.cl', '912345678', 1, 1),
(2, '61.234.567-8', 'Importadora Hogar Chile Ltda', 'ventas@hogarchile.cl', '923456781', 1, 2),
(3, '78.901.234-2', 'Sport Supply Chile SpA', 'ventas@sportsupply.cl', '934567812', 1, 3),
(4, '65.432.109-4', 'Beauty Import SpA', 'contacto@beautyimport.cl', '945678123', 1, 4),
(5, '70.123.456-1', 'PetFood Chile Ltda', 'ventas@petfoodchile.cl', '956781234', 1, 5),
(6, '73.456.789-2', 'Moda Global SpA', 'contacto@modaglobal.cl', '967812345', 1, 6),
(7, '68.901.234-5', 'Papelera del Sur Ltda', 'ventas@papeleradelsur.cl', '978123456', 1, 7),
(8, '71.234.567-5', 'Juguetes Andinos SpA', 'contacto@juguetesandinos.cl', '989234567', 1, 8),
(9, '74.567.890-4', 'Dropshipping Express SpA', 'hola@dropshippingexpress.cl', '991234568', 1, 9);

-- ---------------------------------------------------------------------
-- 5) ALMACENES
-- ---------------------------------------------------------------------
INSERT INTO almacenes (id_almacen, nombre, encargado, estado, id_direccion) VALUES
(1, 'Bodega Central', 'Camila Rojas', 1, 10),
(2, 'Bodega Norte', 'Diego Fuentes', 1, 11),
(3, 'Bodega Despacho', 'Valentina Munoz', 1, 12);

-- ---------------------------------------------------------------------
-- 6) PRODUCTOS
-- ---------------------------------------------------------------------
INSERT INTO productos (id_producto, nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, estado, id_categoria) VALUES
(1, 'Audifonos Bluetooth Pro', 'AUD-BT-001', 12000, 19990, 'Audifonos inalambricos con estuche.', NULL, NULL, 1, 1),
(2, 'Mouse Inalambrico Ergo', 'MOU-ERG-002', 8000, 12990, 'Mouse ergonomico con receptor USB.', NULL, NULL, 1, 1),
(3, 'Teclado Mecanico RGB', 'TEC-MEC-003', 22000, 34990, 'Teclado mecanico con luz RGB.', NULL, NULL, 1, 1),
(4, 'Parlante Portatil Mini', 'PAR-POR-004', 15000, 24990, 'Parlante bluetooth resistente al agua.', NULL, NULL, 1, 1),
(5, 'Cargador Rapido 65W', 'CAR-65W-005', 9000, 15990, 'Cargador USB-C de carga rapida.', NULL, NULL, 1, 1),
(6, 'Set de Ollas Antiadherente', 'OLL-ANT-006', 25000, 39990, 'Set de 3 ollas antiadherentes.', NULL, NULL, 1, 2),
(7, 'Cafetera de Goteo 12 Tazas', 'CAF-GOT-007', 18000, 27990, 'Cafetera de goteo para 12 tazas.', NULL, NULL, 1, 2),
(8, 'Lampara de Escritorio LED', 'LAM-LED-008', 11000, 17990, 'Lampara LED con brazo ajustable.', NULL, NULL, 1, 2),
(9, 'Organizador de Cocina', 'ORG-COC-009', 6000, 9990, 'Organizador plastico de 3 niveles.', NULL, NULL, 1, 2),
(10, 'Mancuernas Ajustables 20kg', 'MAN-20K-010', 35000, 54990, 'Par de mancuernas ajustables.', NULL, NULL, 1, 3),
(11, 'Mat de Yoga Antideslizante', 'MAT-YOG-011', 12000, 19990, 'Mat de yoga antideslizante de 6 mm.', NULL, NULL, 1, 3),
(12, 'Botella Deportiva 1L', 'BOT-DEP-012', 7000, 11990, 'Botella termica de acero de 1 litro.', NULL, NULL, 1, 3),
(13, 'Crema Facial Hidratante', 'CRE-HID-013', 5000, 8990, 'Crema facial de uso diario.', NULL, '2027-06-30', 1, 4),
(14, 'Secador de Pelo Ionico', 'SEC-ION-014', 20000, 32990, 'Secador ionico de 1800W.', NULL, NULL, 1, 4),
(15, 'Set de Brochas Maquillaje', 'BRO-SET-015', 8000, 13990, 'Set de 5 brochas de maquillaje.', NULL, NULL, 1, 4),
(16, 'Alimento Perro Adulto 10kg', 'ALI-PER-016', 22000, 31990, 'Alimento seco para perro adulto.', NULL, '2027-03-31', 1, 5),
(17, 'Rascador para Gatos', 'RAS-GAT-017', 10000, 16990, 'Rascador de sisal de 60 cm.', NULL, NULL, 1, 5),
(18, 'Juguete Interactivo Gato', 'JUG-GAT-018', 4000, 6990, 'Juguete con pluma y cascabel.', NULL, NULL, 1, 5),
(19, 'Mochila Urbana 25L', 'MOC-URB-019', 16000, 25990, 'Mochila con bolsillo para notebook.', NULL, NULL, 1, 6),
(20, 'Gorro de Lana Unisex', 'GOR-LAN-020', 5000, 8990, 'Gorro tejido de lana merino.', NULL, NULL, 1, 6),
(21, 'Cuaderno A5 Punteado', 'CUA-A5P-021', 3000, 5490, 'Cuaderno punteado de 160 paginas.', NULL, NULL, 1, 7),
(22, 'Set de Plumones 12 Colores', 'PLU-SET-022', 4500, 7990, 'Set de 12 plumones de colores.', NULL, NULL, 1, 7),
(23, 'Set de Bloques Didacticos', 'BLO-DID-023', 14000, 22990, 'Bloques de construccion de 50 piezas.', NULL, NULL, 1, 8),
(24, 'Peluche Osito 30cm', 'PEL-OSO-024', 8000, 13990, 'Peluche suave de 30 cm.', NULL, NULL, 1, 8);

-- ---------------------------------------------------------------------
-- 7) PRODUCTO - PROVEEDOR
--    principal = proveedor de su categoria | secundario = Dropshipping (9)
-- ---------------------------------------------------------------------
INSERT INTO producto_proveedor (id_producto, id_proveedor, es_principal) VALUES
(1, 1, 1),
(1, 9, 0),
(2, 1, 1),
(3, 1, 1),
(3, 9, 0),
(5, 1, 1),
(6, 2, 1),
(6, 9, 0),
(7, 2, 1),
(8, 2, 1),
(10, 3, 1),
(10, 9, 0),
(11, 3, 1),
(13, 4, 1),
(14, 4, 1),
(16, 5, 1),
(17, 5, 1),
(18, 5, 1),
(19, 6, 1),
(21, 7, 1),
(21, 9, 0),
(22, 7, 1),
(23, 8, 1);

-- ---------------------------------------------------------------------
-- 8) INVENTARIOS
--    almacen 1 = Bodega Central | 2 = Bodega Norte | 3 = Bodega Despacho
-- ---------------------------------------------------------------------
INSERT INTO inventarios (id_inventario, id_producto, id_almacen, stock_actual, stock_minimo) VALUES
(1, 1, 1, 60, 15),
(2, 2, 1, 45, 15),
(3, 3, 1, 30, 10),
(4, 4, 1, 0, 5),
(5, 5, 1, 25, 10),
(6, 6, 1, 18, 8),
(7, 7, 1, 12, 6),
(8, 8, 1, 22, 8),
(9, 9, 1, 1, 5),
(10, 10, 1, 15, 6),
(11, 11, 1, 20, 8),
(12, 12, 1, 2, 5),
(13, 13, 1, 40, 12),
(14, 14, 1, 14, 6),
(15, 15, 1, 0, 5),
(16, 16, 1, 28, 10),
(17, 17, 1, 16, 8),
(18, 18, 1, 35, 10),
(19, 19, 1, 19, 8),
(20, 20, 1, 1, 5),
(21, 21, 1, 50, 20),
(22, 22, 1, 42, 15),
(23, 23, 1, 13, 6),
(24, 24, 1, 0, 5),
(25, 1, 2, 18, 8),
(26, 3, 2, 10, 5),
(27, 6, 2, 8, 4),
(28, 10, 2, 6, 3),
(29, 13, 2, 15, 6),
(30, 16, 2, 9, 4),
(31, 19, 2, 7, 3),
(32, 21, 2, 20, 8),
(33, 23, 2, 5, 3),
(34, 24, 2, 2, 3),
(35, 2, 3, 12, 6),
(36, 7, 3, 6, 4),
(37, 11, 3, 9, 4),
(38, 14, 3, 5, 3),
(39, 17, 3, 7, 3),
(40, 22, 3, 18, 8);

-- ---------------------------------------------------------------------
-- 9) MOVIMIENTOS
--    El stock de esos inventarios ya quedo calculado con este historial.
-- ---------------------------------------------------------------------
INSERT INTO movimientos (id_movimiento, descripcion, cantidad, tipo, fecha, id_inventario) VALUES
(1, 'Carga inicial de stock', 80, 'ENTRADA', '2026-08-03 09:00:00', 1),
(2, 'Venta online pedido 1001', 12, 'SALIDA', '2026-08-18 15:30:00', 1),
(3, 'Venta online pedido 1042', 8, 'SALIDA', '2026-09-05 11:20:00', 1),
(4, 'Carga inicial de stock', 50, 'ENTRADA', '2026-08-04 09:30:00', 2),
(5, 'Venta online pedido 1015', 5, 'SALIDA', '2026-08-22 12:10:00', 2),
(6, 'Carga inicial de stock', 40, 'ENTRADA', '2026-08-05 10:00:00', 3),
(7, 'Venta online pedido 1033', 6, 'SALIDA', '2026-09-02 16:45:00', 3),
(8, 'Venta online pedido 1088', 4, 'SALIDA', '2026-09-28 10:05:00', 3),
(9, 'Carga inicial de stock', 35, 'ENTRADA', '2026-08-06 08:45:00', 5),
(10, 'Venta online pedido 1051', 10, 'SALIDA', '2026-09-10 14:00:00', 5),
(11, 'Carga inicial de stock', 25, 'ENTRADA', '2026-08-07 11:15:00', 6),
(12, 'Venta online pedido 1059', 7, 'SALIDA', '2026-09-12 09:40:00', 6),
(13, 'Carga inicial de stock', 20, 'ENTRADA', '2026-08-08 09:10:00', 7),
(14, 'Venta online pedido 1071', 8, 'SALIDA', '2026-09-18 17:25:00', 7),
(15, 'Carga inicial de stock', 30, 'ENTRADA', '2026-08-11 10:30:00', 8),
(16, 'Venta online pedido 1079', 8, 'SALIDA', '2026-09-22 13:15:00', 8),
(17, 'Carga inicial de stock', 22, 'ENTRADA', '2026-08-12 08:00:00', 10),
(18, 'Venta online pedido 1083', 7, 'SALIDA', '2026-09-25 11:50:00', 10),
(19, 'Carga inicial de stock', 28, 'ENTRADA', '2026-08-13 09:20:00', 11),
(20, 'Venta online pedido 1102', 8, 'SALIDA', '2026-10-02 10:15:00', 11),
(21, 'Carga inicial de stock', 55, 'ENTRADA', '2026-08-14 12:00:00', 13),
(22, 'Venta online pedido 1110', 15, 'SALIDA', '2026-10-06 15:35:00', 13),
(23, 'Carga inicial de stock', 40, 'ENTRADA', '2026-08-15 09:00:00', 16),
(24, 'Venta online pedido 1118', 12, 'SALIDA', '2026-10-09 11:05:00', 16),
(25, 'Carga inicial de stock', 26, 'ENTRADA', '2026-08-19 10:40:00', 19),
(26, 'Venta online pedido 1125', 7, 'SALIDA', '2026-10-13 16:20:00', 19);

-- ---------------------------------------------------------------------
-- 10) VERIFICACION
-- ---------------------------------------------------------------------
SELECT 'direcciones' AS tabla, COUNT(*) AS filas FROM direcciones
UNION ALL SELECT 'categorias' AS tabla, COUNT(*) AS filas FROM categorias
UNION ALL SELECT 'proveedores' AS tabla, COUNT(*) AS filas FROM proveedores
UNION ALL SELECT 'almacenes' AS tabla, COUNT(*) AS filas FROM almacenes
UNION ALL SELECT 'productos' AS tabla, COUNT(*) AS filas FROM productos
UNION ALL SELECT 'producto_proveedor' AS tabla, COUNT(*) AS filas FROM producto_proveedor
UNION ALL SELECT 'inventarios' AS tabla, COUNT(*) AS filas FROM inventarios
UNION ALL SELECT 'movimientos' AS tabla, COUNT(*) AS filas FROM movimientos;
