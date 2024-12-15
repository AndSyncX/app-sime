create database bdsime;
use bdsime;

create table persona(
    id_persona int primary key auto_increment,
    ape_paterno varchar(50) not null,
    ape_materno varchar(50) not null,
    nom1 varchar(50) not null,
    nom2 varchar(50),
    dni varchar(8) unique not null,
    departamento varchar(50),
    provincia varchar(50),
    distrito varchar(50),
    direccion varchar(200),
    celular int unique not null,
    correo varchar(150) unique not null,
    fec_nacimiento date not null,
    sexo char(1)
);

insert into persona(
    ape_paterno,
    ape_materno,
    nom1,
    nom2,
    dni,
    departamento,
    provincia,
    distrito,
    direccion,
    celular,
    correo,
    fec_nacimiento,
    sexo
) values

('Fernandez', 'Pancorvo', 'Joel', 'Anderson', 72463299, 'Lima', 'Lima', 'Villa  el Salvador', 'Sector 1 Grupo 9 Mz G Lt 17 Av. Revolucion', 969480248, 'fernandezpancorvo@gmail.com', '1998-10-25', 'M'),
('Gonzales', 'Lopez', 'Maria', 'Josefa', 70328475, 'Arequipa', 'Arequipa', 'Cayma', 'Av. Bolognesi 123', 958342156, 'maria.gonzalez@gmail.com', '1995-03-12', 'F'),
('Rodriguez', 'Perez', 'Luis', 'Alberto', 65897412, 'Cusco', 'Cusco', 'Wanchaq', 'Calle Zetas 45', 912345678, 'luis.rodriguez@gmail.com', '1990-07-25', 'M'),
('Torres', 'Garcia', 'Ana', 'Carolina', 74859302, 'Piura', 'Piura', 'Catacaos', 'Jr. San Martin 678', 987654321, 'ana.torres@gmail.com', '2000-05-16', 'F'),
('Lopez', 'Mendoza', 'Carlos', 'Eduardo', 81234567, 'Lambayeque', 'Chiclayo', 'La Victoria', 'Av. Grau 456', 976543210, 'carlos.lopez@gmail.com', '1997-11-02', 'M'),
('Gomez', 'Perez', 'Carlos', 'Alberto', 12345678, 'Lima', 'Lima', 'Miraflores', 'Av. Pardo 123', 981654321, 'carlos.gomez@email.com', '1980-06-15', 'M'),
('Martinez', 'Ruiz', 'Laura', 'Elena', 23456789, 'Lima', 'Lima', 'San Isidro', 'Calle Las Palmas 456', 912445678, 'laura.martinez@email.com', '1975-11-22', 'F'),
('Lopez', 'Torres', 'Juan', 'Carlos', 34567890, 'Arequipa', 'Arequipa', 'Centro', 'Calle A 789', 923456759, 'juan.lopez@email.com', '1982-04-10', 'M'),
('Rodriguez', 'Sanchez', 'Ana', 'Maria', 45678901, 'Cusco', 'Cusco', 'Wanchaq', 'Jr. Real 101', 934567690, 'ana.rodriguez@email.com', '1988-02-05', 'F'),
('Fernandez', 'Diaz', 'Pedro', 'Jose', 56789012, 'Lima', 'Lima', 'Callao', 'Av. La Marina 200', 945676901, 'pedro.fernandez@email.com', '1990-09-14', 'M');

create table modalidad(
    id_modalidad int primary key auto_increment,
    descripcion varchar(30) not null
);

insert into modalidad(
    descripcion
) values
('Presencial'),
('Semipresencial'),
('Virtual');

create table carrera(
    id_carrera int primary key auto_increment,
    nom_carrera varchar(60) not null,
    creditos_total int not null,
    duracion varchar(15) not null,
    id_modalidad int not null,
    foreign key (id_modalidad) references modalidad(id_modalidad)
);

insert into carrera(
    nom_carrera,
    creditos_total,
    duracion,
    id_modalidad
) values
('Ingeniería de Sistemas', 200, '5 años', 1),
('Administración de Empresas', 180, '5 años', 3),
('Contabilidad', 190, '3 años', 1),
('Diseño Gráfico', 150, '3 años', 2),
('Ingeniería Industrial', 210, '5 años', 1),
('Marketing Digital', 120, '3 años', 3),
('Enfermería', 240, '6 años', 1);

create table estudiante(
    id_estudiante int auto_increment primary key,
    id_persona int,
    id_carrera int,
    foreign key (id_persona) references persona(id_persona),
    foreign key (id_carrera) references carrera(id_carrera)
);

insert into estudiante(
    id_persona,
    id_carrera
) values
(1, 1),
(2, 3),
(3, 2),
(4, 4),
(5, 1);

create table docente(
    id_docente int primary key auto_increment,
    especialidad varchar(50) not null,
    id_persona int,
    foreign key (id_persona) references persona(id_persona)
);

insert into docente(
    especialidad,
    id_persona
) values
('Matemáticas', 6),
('Lengua y Literatura', 7),
('Ciencias Sociales', 8),
('Biología', 9),
('Física', 10);

create table curso(
    id_curso int auto_increment primary key,
    nom_curso varchar(75) not null,
    creditos int
);

insert into curso(
    nom_curso,
    creditos
) values
('Matemáticas I', 4),
('Lengua y Literatura I', 3),
('Física I', 5),
('Química I', 6),
('Historia Universal', 6),
('Ciencias Sociales', 3),
('Biología', 4),
('Filosofía', 3),
('Geografía', 3),
('Inglés I', 2),
('Cálculo Diferencial', 5),
('Álgebra Lineal', 4),
('Estadística', 3),
('Economía General', 4),
('Literatura Universal', 3),
('Cálculo Integral', 5),
('Psicología', 3),
('Derecho General', 3),
('Teología', 2),
('Ética Profesional', 3);

create table diaSemana(
    id_dia_semana int auto_increment primary key,
    descripcion varchar(10)
);

insert into diaSemana(
    descripcion
) values
('Lunes'),
('Martes'),
('Miercoles'),
('Jueves'),
('Viernes');

create table horario(
    id_horario int auto_increment primary key,
    hora_inicio time,
    hora_fin time,
    id_dia_semana int,
    foreign key (id_dia_semana) references diaSemana(id_dia_semana)
);

insert into horario(
    hora_inicio,
    hora_fin,
    id_dia_semana
) values
-- lunes
('08:00:00', '12:00:00', 1),
('12:00:00', '16:00:00', 1),
('16:00:00', '20:00:00', 1),
-- martes
('08:00:00', '12:00:00', 2),
('12:00:00', '16:00:00', 2),
('16:00:00', '20:00:00', 2),
-- miercoles
('08:00:00', '12:00:00', 3),
('12:00:00', '16:00:00', 3),
('16:00:00', '20:00:00', 3),
-- jueves
('08:00:00', '12:00:00', 4),
('12:00:00', '16:00:00', 4),
('16:00:00', '20:00:00', 4),
-- viernes
('08:00:00', '12:00:00', 5),
('12:00:00', '16:00:00', 5),
('16:00:00', '20:00:00', 5);

create table seccion(
	id_seccion int primary key auto_increment,
    id_docente int,
    id_horario int,
    id_curso int,
    nom_seccion char(6),
    capacidad int,
    foreign key (id_docente) references docente(id_docente),
    foreign key (id_horario) references horario(id_horario),
    foreign key (id_curso) references curso(id_curso)
);

insert into seccion(
	id_docente,
    id_horario,
    id_curso,
    nom_seccion,
    capacidad
) values
(1, 1, 1, 'MAT101', 30),
(2, 1, 2, 'COM101', 30),
(3, 1, 3, 'QUI101', 30),
(4, 1, 4, 'FIS101', 30);

create table concepto(
	id_concepto int primary key auto_increment,
    descripcion varchar(50) not null,
    monto decimal(10, 2) not null
);

insert into concepto(
	descripcion,
	monto
) values
('Matrícula', 150.00),
('Pensión Mensual', 400.00),
('Cuota Especial', 200.00),
('Material Educativo', 100.00),
('Seguro Estudiantil', 50.00);

create table matricula(
	id_matricula int primary key auto_increment,
    id_seccion int,
    id_estudiante int,
    fec_matricula date,
    estado varchar(25),
    periodo varchar(50),
    foreign key (id_seccion) references seccion(id_seccion),
    foreign key (id_estudiante) references estudiante(id_estudiante)
);

insert into matricula(
	id_seccion,
    id_estudiante,
    fec_matricula,
    estado,
    periodo
) values
(1, 1, '2024-01-15', 'Activo', '2024-I'),
(1, 2, '2024-01-16', 'Activo', '2024-I'),
(1, 3, '2024-01-17', 'Suspendido', '2024-I'),
(1, 4, '2024-01-18', 'Activo', '2024-I'),
(1, 5, '2024-01-19', 'Retirado', '2024-I');

create table cuota (
	id_cuota int primary key auto_increment,
    id_estudiante int,
    id_concepto int,
    id_matricula int,
    fec_pago date,
    monto decimal(10, 2),
    estado varchar(20),
    foreign key (id_concepto) references concepto(id_concepto),
    foreign key (id_matricula) references matricula(id_matricula)
);

insert into Cuota(
	id_estudiante,
    id_concepto,
    id_matricula,
    fec_pago,
    monto,
    estado
)values
(1, 2, 1, '2024-02-01', 300.00, 'Pagada'),
(1, 2, 1, '2024-02-05', 300.00, 'Pendiente'),
(1, 4, 1, '2024-02-10', 200.00, 'Pagada'),
(1, 3, 1, '2024-02-15', 50.00, 'Pendiente'),
(1, 5, 1, '2024-02-20', 100.00, 'Pagada');

create table detalle (
	id_detalle int primary key auto_increment,
    id_cuota int,
    id_concepto int,
    fec_detalle date,
    monto_detalle decimal(10, 2),
    observacion varchar(255),
    foreign key (id_cuota) references cuota(id_cuota),
    foreign key (id_concepto) references concepto(id_concepto)
);

insert into detalle values
(1, 1, 2, '2024-02-01', 300.00, 'Cuota Mensual Enero'),
(2, 2, 2, '2024-02-05', 300.00, 'Cuota Mensual Febrero'),
(3, 3, 4, '2024-02-10', 200.00, 'Seguro Estudiantil'),
(4, 4, 3, '2024-02-15', 50.00, 'Pago Materiales'),
(5, 5, 5, '2024-02-20', 100.00, 'Pago de Actividades');