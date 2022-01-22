### CREACIÓN DE TABLAS

Usuarios
~~~
create table usuarios(
    dni varchar(9) PRIMARY KEY,
    username varchar(20) NOT NULL,
    contraseña varchar(20) NOT NULL,
    nombre varchar(60) NOT NULL,
    fecha_nacimiento date NOT NULL,
    correo varchar(100) NOT NULL
);
~~~

Clientes
~~~
create table clientes(
    dni varchar(9) REFERENCES usuarios(dni)
);
~~~

Peluqueros
~~~
create table peluqueros(
    dni varchar(9) REFERENCES usuarios(dni),
    cnae varchar(4) NOT NULL,
    localizacion varchar(100)
);
~~~

Mensajes
~~~
create table mensajes(
	id_mensaje varchar(20) PRIMARY KEY,
	emisor varchar(9) REFERENCES usuarios(dni),
	receptor varchar(9) REFERENCES usuarios(dni),
	contenido VARCHAR(280) NOT NULL
);
~~~

Citas
~~~
create table citas(
    id_cita varchar(20) PRIMARY KEY,
    fecha date NOT NULL, 
    hora varchar(5) NOT NULL # time da error
);
~~~

Cliente pide Cita
~~~
create table clientePideCita(
    id_cita varchar(20) REFERENCES citas(id_cita),
    dni varchar(9) REFERENCES usuarios(dni)
);
~~~

Peluquero acepta Cita
~~~
create table PeluqueroAceptaCita(
    id_cita varchar(20) REFERENCES citas(id_cita),
    dni varchar(9) REFERENCES usuarios(dni)
);
~~~

Valoraciones y Comentarios
~~~
create table valycom(
    id_val varchar(20) PRIMARY KEY,
    valoracion varchar(2) NOT NULL, 
    comentario varchar(400)
);
~~~

Asocia Valoraciones 
~~~
create table AsociaVal(
    id_val varchar(20) REFERENCES valycom(id_val),
    id_cita varchar(20) REFERENCES citas(id_cita)
);
~~~

Fotografías 
~~~
create table fotografias(
    id_foto varchar(20) PRIMARY KEY, 
    foto ordimage NOT NULL
);
~~~

Añade fotografía
~~~
create table AnadeFoto(
    id_foto varchar(20) REFERENCES fotografias(id_foto),
    id_val varchar(20) REFERENCES valycom(id_val)
);
~~~

Pagos
~~~
create table pagos(
    id_pago varchar(20) PRIMARY KEY, 
    importe decimal(4,2),
    num_tarjeta varchar(16)
);
~~~

Asocia pagos
~~~
create table AsociaPago(
    id_pago varchar(20) REFERENCES pagos(id_pago), 
    id_cita varchar(20) REFERENCES citas(id_cita)
);
~~~

Incidencias
~~~
create table incidencias(
    id_incidencia varchar(20) PRIMARY KEY, 
    incidencia varchar(100) NOT NULL
);
~~~

Comunica Incidencia
~~~
create table ComunicaIncidencia(
    id_incidencia varchar(20) REFERENCES incidencias(id_incidencia), 
    id_cita varchar(20) REFERENCES citas(id_cita)
);
~~~

Productos
~~~
create table productos(
    id_producto varchar(20) PRIMARY KEY, 
    precio decimal(4,2), 
    tipo varchar(25) NOT NULL, 
    descripcion varchar(100)
);
~~~

Peluquero Producto
~~~
create table PeluqueroProducto(
    id_producto varchar(20) REFERENCES productos(id_producto)
    id_peluquero varchar(20) REFERENCES usuarios(dni)
    cantidad varchar(3)
);
~~~

Proveedores
~~~
create table proveedores(
    id_proveedor varchar(20) PRIMARY KEY, 
    nombre varchar(50) NOT NULL,
    tipos varchar(200)
);
~~~

Peluquero Proveedor
~~~
create table PeluqueroProveedor(
    id_peluquero varchar(20) REFERENCES usuarios(dni),
    id_proveedor varchar(20) REFERENCES proveedores(id_proveedor) 
);
~~~

Producto Proveedor
~~~
create table ProductoProveedor(
    id_producto varchar(20) REFERENCES productos(id_producto),
    id_proveedor varchar(20) REFERENCES proveedores(id_proveedor),
    cantidad varchar(3)
);
~~~

### LECTURA DE TABLAS

~~~
select * from user_tables;
select * from usuarios;
select * from clientes;
select * from peluqueros;
select * from mensajes; 

describe usuarios;
~~~

### INSERCIÓN EN TABLAS

~~~
insert into usuarios values ('77555876Z', 'Trajano', '1234', 'Juanma', TO_DATE('09/10/1999', 'DD/MM/YYYY'), 'juanma');

INSERT INTO clientes VALUES ('77555876Z');

insert into usuarios values ('77555878Z', 'Trajano', '1234', 'Juanma', TO_DATE('09/10/1999', 'DD/MM/YYYY'), 'juanma');

INSERT INTO peluqueros VALUES ('77555878Z', '1111', null);
~~~

### ELIMINACIÓN DE TABLAS

~~~
delete from peluqueros where dni = '77555872Z';
delete from usuarios where dni = '77555872Z';

DROP table usuarios;
~~~

### ACTUALIZACIÓN DE TABLAS
~~~
update usuarios set username = 'Josesito', contraseña = '1234', nombre = 'Jose', fecha_nacimiento = TO_DATE('09/10/1996', 'DD/MM/YYYY'), correo = 'jose' where dni = '77555878Z';

commit;
~~~
