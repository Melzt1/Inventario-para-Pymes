# Sistema de Inventario para PYMEs

Sistema de gestión de inventario por terminal.
Administra categorías, proveedores, productos, almacenes, stock y movimientos,
conectado a MySQL mediante el ORM Peewee.

## Arquitectura

Cuatro capas, cada una con una única responsabilidad:

| Capa | Carpeta | Responsabilidad |
|---|---|---|
| Presentación | `presentacion/` | Menús y entrada por teclado |
| Negocio | `negocio/` | Reglas, validaciones y transacciones |
| Repositorios | `datos/repositorios/` | Consultas a la base de datos |
| Modelos | `datos/modelos/` | Tablas mapeadas con Peewee |

La presentación nunca escribe SQL ni pide IDs internos: busca por nombre o SKU y
elige de una lista. El borrado es lógico mediante la columna `estado`.

## Requisitos

- Python 3.10 o superior
- MySQL 8.0 o superior

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

El archivo `.env` de la raíz contiene las credenciales de conexión. Si tu MySQL
local usa otro usuario o contraseña, edítalo antes de ejecutar:

```ini
host = 'localhost'
port = 3306
user = 'melzt'
password = 'tu_password'
db = 'sistema_pyme'
```

## Base de datos

El usuario debe existir en tu MySQL local y coincidir con el `.env`:

```sql
CREATE USER 'melzt'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON sistema_pyme.* TO 'melzt'@'localhost';
FLUSH PRIVILEGES;
```

### Scripts SQL: ejecutar en este orden

> **Importante:** los scripts de `datos/sql/` deben ejecutarse **en el orden
> indicado**. Cada uno depende del anterior: agrega columnas, elimina tablas o
> reemplaza datos. Si se altera el orden, la aplicación falla al iniciar.

| # | Script | Qué hace |
|---|---|---|
| 1 | `2026-09-08_12.10_DDL_Sistema_Pyme.sql` | Crea la base de datos y todas las tablas |
| 2 | `2026-09-16_19.07_alter_table.sql` | Agrega comentarios a las tablas |
| 3 | `2026-10-07_16.32_alter_table.sql` | Agrega la columna `estado` a categorías |
| 4 | `2026-10-15_20.08_fusionar_stock_en_inventario.sql` | Fusiona la tabla `stocks` dentro de `inventarios` |
| 5 | `2026-10-20_03.00_datos_prueba_ecommerce.sql` | Carga los datos de prueba (e-commerce) |

`2026-10-05_23.42_insert_categorias.sql` es **opcional**: el script 5 reemplaza
esas categorías por las del rubro e-commerce.

## Ejecución

```bash
python app.py
```

## Menú

```
Sistema de Inventario
│
├── [1] Gestión de categorías
│   ├── [1] Listar categorías
│   ├── [2] Guardar categoría
│   ├── [3] Consultar categoría
│   ├── [4] Actualizar categoría
│   ├── [5] Desactivar categoría
│   ├── [6] Activar categoría
│   └── [0] Volver al menú principal
│
├── [2] Gestión de proveedores
│   ├── [1] Listar proveedores
│   ├── [2] Registrar proveedor
│   ├── [3] Consultar proveedor
│   ├── [4] Actualizar proveedor
│   ├── [5] Actualizar dirección del proveedor
│   ├── [6] Desactivar proveedor
│   ├── [7] Activar proveedor
│   └── [0] Volver al menú principal
│
├── [3] Gestión de productos
│   ├── [1] Listar productos
│   ├── [2] Registrar producto
│   ├── [3] Consultar producto por nombre
│   ├── [4] Actualizar producto
│   ├── [5] Desactivar producto
│   ├── [6] Activar producto
│   ├── [7] Relaciones producto-proveedor
│   │   ├── [1] Asignar proveedor principal
│   │   ├── [2] Asignar proveedor secundario
│   │   ├── [3] Quitar proveedor
│   │   ├── [4] Ver proveedores del producto
│   │   └── [0] Volver al menú anterior
│   └── [0] Volver al menú principal
│
├── [4] Gestión de almacenes
│   ├── [1] Listar almacenes
│   ├── [2] Registrar almacén
│   ├── [3] Consultar almacén
│   ├── [4] Actualizar almacén
│   ├── [5] Actualizar dirección del almacén
│   ├── [6] Desactivar almacén
│   ├── [7] Activar almacén
│   └── [0] Volver al menú principal
│
├── [5] Gestión de inventario y movimientos
│   ├── [1] Asociar producto a un almacén
│   ├── [2] Consultar inventario de un producto en un almacén
│   ├── [3] Listar inventario de un almacén
│   ├── [4] Listar productos bajo stock mínimo
│   ├── [5] Gestión de movimientos
│   │   ├── [1] Registrar entrada de stock
│   │   ├── [2] Registrar salida de stock
│   │   ├── [3] Consultar movimientos por tipo
│   │   ├── [4] Consultar movimientos por rango de fecha
│   │   ├── [5] Ver historial completo
│   │   └── [0] Volver al menú anterior
│   └── [0] Volver al menú principal
│
└── [0] Salir
```

## Estructura del proyecto

```
app.py                    Punto de entrada
auxiliares/               Menús, mensajes y entrada validada por teclado
datos/conexion.py         Conexión a MySQL
datos/modelos/            Tablas mapeadas con Peewee
datos/repositorios/       Consultas SQL por entidad
datos/sql/                Scripts de creación y datos de prueba
negocio/                  Reglas de negocio y validaciones
presentacion/             Menús e interacción con el usuario
requirements.txt          Dependencias del proyecto
Diagrama_UML.png          Diagrama de clases
```
