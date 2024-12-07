create database bdsime;
use bdsime;

create table persona(
    id_persona int primary key auto_increment,
    ape_paterno varchar(50) not null,
    ape_materno varchar(50) not null,
    nom1 varchar(50) not null,
    nom2 varchar(50),
    dni int unique not null,
    departamento varchar(50),
    provincia varchar(50),
    distrito varchar(50),
    direccion varchar(200),
    celular int unique not null,
    correo varchar(150) unique not null,
    fec_nacimiento date not null,
    estado_civil varchar(25),
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
    estado_civil,
    sexo
) values
('Fernandez', 'Pancorvo', 'Joel', 'Anderson', 72463299, 'Lima', 'Lima', 'Villa  el Salvador', 'Sector 1 Grupo 9 Mz G Lt 17 Av. Revolucion', 969480248, 'fernandezpancorvo@gmail.com', '1998-10-25', 'Soltero', 'M'),
('Gonzales', 'Lopez', 'Maria', 'Josefa', 70328475, 'Arequipa', 'Arequipa', 'Cayma', 'Av. Bolognesi 123', 958342156, 'maria.gonzalez@gmail.com', '1995-03-12', 'Casada', 'F'),
('Rodriguez', 'Perez', 'Luis', 'Alberto', 65897412, 'Cusco', 'Cusco', 'Wanchaq', 'Calle Zetas 45', 912345678, 'luis.rodriguez@gmail.com', '1990-07-25', 'Soltero', 'M'),
('Torres', 'Garcia', 'Ana', 'Carolina', 74859302, 'Piura', 'Piura', 'Catacaos', 'Jr. San Martin 678', 987654321, 'ana.torres@gmail.com', '2000-05-16', 'Soltera', 'F'),
('Lopez', 'Mendoza', 'Carlos', 'Eduardo', 81234567, 'Lambayeque', 'Chiclayo', 'La Victoria', 'Av. Grau 456', 976543210, 'carlos.lopez@gmail.com', '1997-11-02', 'Soltero', 'M'),
('Gomez', 'Perez', 'Carlos', 'Alberto', 12345678, 'Lima', 'Lima', 'Miraflores', 'Av. Pardo 123', 981654321, 'carlos.gomez@email.com', '1980-06-15', 'Casado', 'M'),
('Martinez', 'Ruiz', 'Laura', 'Elena', 23456789, 'Lima', 'Lima', 'San Isidro', 'Calle Las Palmas 456', 912445678, 'laura.martinez@email.com', '1975-11-22', 'Soltera', 'F'),
('Lopez', 'Torres', 'Juan', 'Carlos', 34567890, 'Arequipa', 'Arequipa', 'Centro', 'Calle A 789', 923456759, 'juan.lopez@email.com', '1982-04-10', 'Viudo', 'M'),
('Rodriguez', 'Sanchez', 'Ana', 'Maria', 45678901, 'Cusco', 'Cusco', 'Wanchaq', 'Jr. Real 101', 934567690, 'ana.rodriguez@email.com', '1988-02-05', 'Soltera', 'F'),
('Fernandez', 'Diaz', 'Pedro', 'Jose', 56789012, 'Lima', 'Lima', 'Callao', 'Av. La Marina 200', 945676901, 'pedro.fernandez@email.com', '1990-09-14', 'Casado', 'M');

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

SELECT
	h.id_horario,
	h.hora_inicio,
	h.hora_fin,
	d.descripcion 
FROM horario h
INNER JOIN diaSemana d 
where h.id_dia_semana = d.id_dia_semana 
ORDER BY id_horario 
DESC;

SELECT  
	d.id_docente,
	p.ape_paterno,
	p.ape_materno,
	p.nom1,
	p.nom2,
	p.dni,
	p.departamento,
	p.provincia,
	p.distrito,
	p.direccion,
	p.celular,
	p.correo,
	p.fec_nacimiento,
	p.estado_civil,
	p.sexo
FROM docente d 
INNER JOIN persona p 
ON d.id_persona = p.id_persona
ORDER BY id_docente
DESC;