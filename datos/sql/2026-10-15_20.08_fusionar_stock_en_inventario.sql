-- Fusion de la tabla stocks dentro de inventarios.
-- Motivo: la relacion era 1:1 sin atributos propios, forzada por UNIQUE
-- son atributos de la relacion (producto, almacen), no de una entidad aparte.
USE sistema_pyme;

-- Agregar las columnas de stock a la tabla inventarios
ALTER TABLE inventarios
    ADD COLUMN stock_actual INTEGER NOT NULL DEFAULT 0,
    ADD COLUMN stock_minimo INTEGER NOT NULL DEFAULT 0;

-- Eliminar primero la relacion 
ALTER TABLE inventarios DROP FOREIGN KEY fk_inventario_stock;
-- Eliminar la restriccion UNIQUE para luego borrar la fk
ALTER TABLE inventarios DROP INDEX uk_inventario_stock;

-- Eliminar la columna (fk)
ALTER TABLE inventarios DROP COLUMN id_stock;

-- Reaplicar los checks que estaban en stocks
ALTER TABLE inventarios
    ADD CONSTRAINT ck_inventario_stock_actual CHECK (stock_actual >= 0),
    ADD CONSTRAINT ck_inventario_stock_minimo CHECK (stock_minimo >= 0);

-- Eliminar la tabla stocks
DROP TABLE stocks;    