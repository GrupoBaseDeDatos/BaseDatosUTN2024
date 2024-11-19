# Talleres de Autos - Normalización de Datos

Queremos revisar y mejorar la forma de guardar los datos en la cadena de talleres de autos “UNQar”. Actualmente se cuenta con el siguiente esquema obtenido de una planilla Excel:


## Restricciones
1. El `codigoSucursal` corresponde a una sucursal puntual para la cual conocemos el domicilio, teléfono, las fosas que tiene y los mecánicos que trabajan en la misma.
2. De las fosas conocemos el código, que es un número secuencial por sucursal (dos sucursales podrían tener el mismo código de fosa, pero serían fosas distintas). También registramos su largo y ancho.
3. En una fosa se arreglan autos, y se registra para cada fosa qué autos se arreglaron en la misma. De los autos conocemos:
   - Patente
   - Marca
   - Modelo
   - Cliente asociado
4. Un cliente puede tener varios autos, pero un auto tiene un único cliente.
5. De los clientes se registra:
   - DNI
   - Nombre
   - Celular
6. De los mecánicos se registra:
   - DNI
   - Nombre
   - Email

---

## Dependencias Funcionales (DFs)

1. `codigoSucursal` determina `{domicilioSucursal, telefonoSucursal}`  
   **DF:** `codigoSucursal = {domicilioSucursal, telefonoSucursal}`

2. `codigoSucursal, codigoFosa` determina `{largoFosa, anchoFosa}`  
   **DF:** `codigoSucursal, codigoFosa = {largoFosa, anchoFosa}`

3. `codigoSucursal, codigoFosa, patenteAuto` determina `{marcaAuto, modeloAuto, dniCliente}`  
   **DF:** `codigoSucursal, codigoFosa, patenteAuto = {marcaAuto, modeloAuto, dniCliente}`

4. `dniCliente` determina `{nombreCliente, celularCliente}`  
   **DF:** `dniCliente = {nombreCliente, celularCliente}`

5. `dniMecanico` determina `{nombreMecanico, emailMecanico}`  
   **DF:** `dniMecanico = {nombreMecanico, emailMecanico}`

6. `dniCliente, patenteAuto` determina `{marcaAuto, modeloAuto}`  
   **DF:** `dniCliente, patenteAuto = {marcaAuto, modeloAuto}`


---

## Claves Candidatas

- `codigoSucursal, codigoFosa, patenteAuto`

---

## Clave Primaria

**Clave primaria:**  
`codigoSucursal, codigoFosa, patenteAuto`


- Estos tres atributos permiten identificar de manera única un registro, considerando la jerarquía de sucursal, fosa, y auto.

---

### 1FN

- El esquema ya está en 1FN porque no tiene grupos repetidos y todos los valores son indivisibles, es decir, no hay atributos compuestos.

- **TALLER** `{codigoSucursal, domicilioSucursal, telefonoSucursal, codigoFosa,largoFosa, anchoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente,nombreCliente, celularCliente, dniMecanico, nombreMecanico, emailMecanico}`



---

### 2FN

Descomponemos el esquema para eliminar dependencias parciales:

1. **Sucursal**: {codigoSucursal, domicilioSucursal, telefonoSucursal}

2. **Fosa**: {codigoSucursal, codigoFosa, largoFosa, anchoFosa}

3. **AutoCliente**: {codigoSucursal, codigoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente}

4. **Cliente**: {dniCliente, nombreCliente, celularCliente}

5. **Mecanico**: {dniMecanico, nombreMecanico, emailMecanico}

6. **Arreglo**: {codigoSucursal, codigoFosa, patenteAuto, dniMecanico}

---

### 3FN

Con las tablas propuestas en 2FN, cada atributo no clave depende directamente de la clave primaria. Por lo tanto, el esquema ya cumple con la 3FN.

---

## Esquema en 3FN

1. **Tabla `Sucursal`**
   - `codigoSucursal` (Clave primaria)
   - `domicilioSucursal`
   - `telefonoSucursal`

2. **Tabla `Fosa`**
   - `codigoSucursal` (Clave foránea a `Sucursal`)
   - `codigoFosa` (Clave primaria compuesta junto con `codigoSucursal`)
   - `largoFosa`
   - `anchoFosa`

3. **Tabla `Auto`**
   - `patenteAuto` (Clave primaria)
   - `marcaAuto`
   - `modeloAuto`
   - `dniCliente` (Clave foránea a `Cliente`)

4. **Tabla `Cliente`**
   - `dniCliente` (Clave primaria)
   - `nombreCliente`
   - `celularCliente`

5. **Tabla `Mecanico`**
   - `dniMecanico` (Clave primaria)
   - `nombreMecanico`
   - `emailMecanico`

6. **Tabla `Reparacion`**
   - `codigoSucursal` (Clave foránea a `Sucursal`)
   - `codigoFosa` (Clave foránea a `Fosa`)
   - `patenteAuto` (Clave foránea a `Auto`)
   - `dniMecanico` (Clave foránea a `Mecanico`)
   - Clave primaria compuesta: (`codigoSucursal`, `codigoFosa`, `patenteAuto`, `dniMecanico`)


---

Con este diseño, la base de datos está normalizada hasta la Tercera Forma Normal, lo que mejora la eficiencia y elimina redundancias.

