-- USAR BD
USE bdsime;

-- --------------------CARRERA--------------------

-- PROCEDIMIENTO LISTARCARRERA()
DELIMITER $$
CREATE PROCEDURE listarCarrera()
BEGIN
	SELECT 
		c.id_carrera,
        c.nom_carrera,
        c.creditos_total,
        c.duracion,
        m.descripcion
	FROM carrera c 
    INNER JOIN modalidad m 
    ON c.id_modalidad = m.id_modalidad 
    ORDER BY id_carrera
    DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARCARRERAxID()
DELIMITER $$
CREATE PROCEDURE listarCarreraxId(IN p_id_carrera int)
BEGIN
	SELECT 
		c.id_carrera,
		c.nom_carrera,
		c.creditos_total,
		c.duracion,
		m.descripcion
	FROM carrera c 
	INNER JOIN modalidad m 
	ON c.id_modalidad = m.id_modalidad 
	WHERE id_carrera = p_id_carrera
	ORDER BY id_carrera 
	DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO INSERTARCARRERA()
DELIMITER $$
CREATE PROCEDURE insertarCarrera(IN 
	p_nom_carrera varchar(60),
    p_creditos_totales int,
    p_duracion varchar(15),
    p_id_modalidad int)
BEGIN
	INSERT INTO carrera(
		nom_carrera,
        creditos_total,
        duracion,
        id_modalidad) 
    VALUES(
		p_nom_carrera,
		p_creditos_totales,
		p_duracion,
		p_id_modalidad
	);
END$$
DELIMITER ;

-- PROCEDIMIENTO ACTUALIZARCARRERA()
DELIMITER $$
CREATE PROCEDURE actualizarCarrera(IN
	p_nom_carrera varchar(60),
    p_creditos_totales int,
    p_duracion varchar(15),
    p_id_modalidad int,
    p_id_carrera int)
BEGIN
	UPDATE carrera SET
		nom_carrera = p_nom_carrera,
        creditos_total = p_creditos_totales,
        duracion = p_duracion,
        id_modalidad = p_id_modalidad
	WHERE id_carrera = p_id_carrera;
END$$
DELIMITER ;

-- --------------------HORARIO--------------------

-- PROCEDIMIENTO LISTARHORARIO
DELIMITER $$
CREATE PROCEDURE listarHorario()
BEGIN
	SELECT 
		h.id_horario,
        h.hora_inicio,
        h.hora_fin,
        d.descripcion
	FROM horario h 
    INNER JOIN diaSemana d 
    ON h.id_dia_semana = d.id_dia_semana 
    ORDER BY id_horario 
    DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARHORARIOxID
DELIMITER $$
CREATE PROCEDURE listarHorarioxId(IN p_id_horario int)
BEGIN
	SELECT 
		h.id_horario,
		h.hora_inicio,
        h.hora_fin,
        d.descripcion
	FROM horario h
    INNER JOIN diaSemana d
    ON h.id_dia_semana = d.id_dia_semana
    WHERE id_horario = p_id_horario 
    ORDER BY id_horario 
    DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO INSERTARHORARIO
DELIMITER $$
CREATE PROCEDURE insertarHorario(IN
	p_hora_inicio time,
    p_hora_fin time,
    p_id_dia_semana int)
BEGIN
	INSERT INTO horario (
		hora_inicio,
        hora_fin,
        id_dia_semana
	)
    VALUES (
		p_hora_inicio,
        p_hora_fin,
        p_id_dia_semana
    );
END$$
DELIMITER ;

-- PROCEDIMIENTO ACTUALIZAR HORARIO
DELIMITER $$
CREATE PROCEDURE actualizarHorario(
	p_hora_inicio time,
    p_hora_fin time,
    p_id_dia_semana int,
    p_id_horario int
)
BEGIN
	UPDATE horario
    SET
		hora_inicio = p_hora_inicio,
        hora_fin = p_hora_fin,
        id_dia_semana = p_id_dia_semana
	WHERE
		id_horario = p_id_horario;
END$$
DELIMITER ;

-- --------------------SECCION--------------------

-- CREAR VISTA DOCENTExPERSONA
CREATE VIEW vista_docente AS 
SELECT 
    d.id_docente,
    CONCAT(p.ape_paterno, ' ', p.nom1, ' ', p.nom2) AS nombre_docente,
    p.id_persona, p.ape_paterno, p.nom1, p.nom2, p.ape_materno -- Agrega los campos necesarios
FROM 
    docente d
INNER JOIN 
    persona p ON d.id_persona = p.id_persona;
    
-- CREAR VISTA HORARIOxDIASEMANA
CREATE VIEW vista_horario AS 
SELECT 
    h.id_horario,
    CONCAT(h.hora_inicio, " - ", h.hora_fin, " - ", ds.descripcion) AS Horario_Dia_Semana
FROM 
    horario h
INNER JOIN 
    diasemana ds ON h.id_dia_semana = ds.id_dia_semana;

-- PROCEDIMIENTO LISTARSECCION
DELIMITER $$
CREATE PROCEDURE listarSeccion()
BEGIN
    SELECT 
        s.id_seccion, 
        dv.nombre_docente,
		vh.Horario_Dia_Semana,
        c.nom_curso, 
        s.nom_seccion, 
        s.capacidad
    FROM 
        seccion s
    INNER JOIN vista_docente dv ON dv.id_docente = s.id_docente
    INNER JOIN vista_horario vh ON vh.id_horario = s.id_horario
    INNER JOIN curso c ON c.id_curso = s.id_curso
    ORDER BY id_seccion DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARSECCIONxID
DELIMITER $$
CREATE PROCEDURE listarSeccionxId(IN sp_id_seccion INT)
BEGIN
    SELECT 
        s.id_seccion, 
        dv.nombre_docente,
        vh.Horario_Dia_Semana, 
        c.nom_curso, 
        s.nom_seccion, 
        s.capacidad
    FROM 
        seccion s
    INNER JOIN vista_docente dv ON dv.id_docente = s.id_docente
    INNER JOIN vista_horario vh ON vh.id_horario = s.id_horario
    INNER JOIN curso c ON c.id_curso = s.id_curso
    WHERE id_seccion = sp_id_seccion
    ORDER BY id_seccion DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO INSERTARSECCION
DELIMITER $$

CREATE PROCEDURE insertarSeccion(IN
	sp_id_docente INT,
    sp_id_horario INT,
    sp_id_curso INT,
    sp_nom_seccion VARCHAR(45),
    sp_capacidad INT
)
BEGIN
    INSERT INTO seccion (
        id_docente,
        id_horario,
        id_curso,
        nom_seccion,
        capacidad
    )
    VALUES (
        sp_id_docente,
        sp_id_horario,
        sp_id_curso,
        sp_nom_seccion,
        sp_capacidad
    );
END$$

DELIMITER ;

-- PROCEDIMIENTO ACTUALIZARSECCION
DELIMITER $$
CREATE PROCEDURE actualizarSeccion(IN
	sp_id_docente INT,
    sp_id_horario INT,
    sp_id_curso INT,
    sp_nom_seccion VARCHAR(45),
    sp_capacidad INT,
    sp_id_seccion INT
)
BEGIN
	UPDATE seccion
    SET
		id_docente = sp_id_docente,
        id_horario = sp_id_horario,
        id_curso = sp_id_curso,
        nom_seccion = sp_nom_seccion,
        capacidad = sp_capacidad
	WHERE
		id_seccion = sp_id_seccion;
END$$
DELIMITER ;

-- --------------------PERSONA--------------------

-- PROCEDIMIENTO INSERTARPERSONA
DELIMITER $$
CREATE PROCEDURE insertarPersona(IN
	sp_ape_paterno varchar(50),
    sp_ape_materno varchar(50),
    sp_nom1 varchar(50),
    sp_nom2 varchar(50),
    sp_dni varchar(8),
    sp_departamento varchar(50),
    sp_provincia varchar(50),
    sp_distrito varchar(50),
    sp_direccion varchar(50),
    sp_celular int,
    sp_correo varchar(150),
    sp_fec_nacimiento date,
    sp_sexo char(1),
    OUT id_generado int
)
BEGIN
    INSERT INTO Persona (
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
    )
    VALUES (
        sp_ape_paterno,
        sp_ape_materno,
        sp_nom1,
        sp_nom2,
        sp_dni,
        sp_departamento,
        sp_provincia,
        sp_distrito,
        sp_direccion,
        sp_celular,
        sp_correo,
        sp_fec_nacimiento,
        sp_sexo
    );
    SET id_generado = LAST_INSERT_ID();
END$$
DELIMITER ;

-- PROCEDIMIENTO ACTUALIZARPERSONA
DELIMITER $$
CREATE PROCEDURE actualizarPersona(IN
	sp_ape_paterno varchar(50),
    sp_ape_materno varchar(50),
    sp_nom1 varchar(50),
    sp_nom2 varchar(50),
    sp_dni varchar(8),
    sp_departamento varchar(50),
    sp_provincia varchar(50),
    sp_distrito varchar(50),
    sp_direccion varchar(50),
    sp_celular int,
    sp_correo varchar(150),
    sp_fec_nacimiento date,
    sp_sexo char(1),
    sp_id_persona int
)
BEGIN
	UPDATE Persona
    SET
		ape_paterno = sp_ape_paterno,
        ape_materno = sp_ape_materno,
        nom1 = sp_nom1,
        nom2 = sp_nom2,
        dni = sp_dni,
        departamento = sp_departamento,
        provincia = sp_provincia,
        distrito = sp_distrito,
        direccion = sp_direccion,
        celular = sp_celular,
        correo = sp_correo,
        fec_nacimiento = sp_fec_nacimiento,
        sexo = sp_sexo
	WHERE
		id_persona = sp_id_persona;
END$$
DELIMITER ;

-- --------------------ESTUDIANTE--------------------

-- PROCEDIMIENTO LISTARESTUDIANTE
DELIMITER $$
CREATE PROCEDURE listarEstudiante()
BEGIN
	SELECT 
		e.id_estudiante,
        p.id_persona,
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
		p.sexo,
        c.nom_carrera
	FROM estudiante e
    INNER JOIN persona p ON p.id_persona = e.id_persona
    INNER JOIN carrera c ON c.id_carrera = e.id_carrera 
    ORDER BY id_estudiante DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARESTUDIANTExID
DELIMITER $$
CREATE PROCEDURE listarEstudiantexId(IN sp_id_estudiante int)
BEGIN
	SELECT 
		e.id_estudiante,
        p.id_persona,
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
		p.sexo,
        c.nom_carrera
	FROM estudiante e
    INNER JOIN persona p ON p.id_persona = e.id_persona
    INNER JOIN carrera c ON c.id_carrera = e.id_carrera
    WHERE id_estudiante = sp_id_estudiante
    ORDER BY id_estudiante DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO INSERTARESTUDIANTE
DELIMITER $$
CREATE PROCEDURE insertarEstudiante(IN sp_id_persona int, sp_id_carrera int)
BEGIN
	INSERT INTO estudiante (
		id_persona,
        id_carrera
	) 
    VALUES (
		sp_id_persona,
        sp_id_carrera
	);
END$$
DELIMITER ;

-- PROCEDIMIENTO ACTUALIZARESTUDIANTE
DELIMITER $$
CREATE PROCEDURE actualizarEstudiante(IN sp_id_persona int, sp_id_carrera int, sp_id_estudiante int)
BEGIN
	UPDATE estudiante 
    SET id_persona = sp_id_persona,
        id_carrera = sp_id_carrera
    WHERE id_estudiante = sp_id_estudiante;
END$$
DELIMITER ;

-- VISTA ESTUDIANTExPERSONA
CREATE VIEW vista_estudiante AS 
SELECT 
    e.id_estudiante,
    CONCAT(p.ape_paterno, ' ', p.ape_materno, ' ', p.nom1, ' ', p.nom2) AS nombre_estudiante
FROM 
    estudiante e
INNER JOIN 
    persona p ON e.id_persona = p.id_persona;
    
-- PROCEDIMIENTO LISTARMATRICULA
DELIMITER $$
CREATE PROCEDURE listarMatricula()
BEGIN
    SELECT 
        m.id_matricula,
        s.nom_seccion,
        ev.nombre_estudiante,
        m.fec_matricula,
        m.estado, 
        m.periodo
    FROM
        matricula m
    INNER JOIN seccion s ON s.id_seccion = m.id_seccion
    INNER JOIN vista_estudiante ev ON ev.id_estudiante = m.id_estudiante
    ORDER BY id_matricula DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARMATRICULA
DELIMITER $$
CREATE PROCEDURE listarMatriculaxId(IN sp_id_matricula int)
BEGIN
    SELECT 
        m.id_matricula,
        s.nom_seccion,
        ev.nombre_estudiante,
        m.fec_matricula,
        m.estado, 
        m.periodo
    FROM
        matricula m
    INNER JOIN seccion s ON s.id_seccion = m.id_seccion
    INNER JOIN vista_estudiante ev ON ev.id_estudiante = m.id_estudiante
    WHERE id_matricula = sp_id_matricula
    ORDER BY id_matricula DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARCUOTA
DELIMITER $$
CREATE PROCEDURE listarCuota()
BEGIN
    SELECT 
        cu.id_cuota,
        ev.nombre_estudiante,
        cp.descripcion,
        ma.id_matricula,
        cu.fec_pago, 
        cu.monto,
        cu.estado
    FROM
        cuota cu
    INNER JOIN concepto cp ON cp.id_concepto = cu.id_concepto
    INNER JOIN vista_estudiante ev ON ev.id_estudiante = cu.id_estudiante
    INNER JOIN matricula ma ON ma.id_matricula = cu.id_matricula
    ORDER BY id_cuota DESC;
END$$
DELIMITER ;

-- PROCEDIMIENTO LISTARCUOTAxID
DELIMITER $$
CREATE PROCEDURE listarCuotaxId(IN sp_id_cuota int)
BEGIN
    SELECT 
        cu.id_cuota,
        ev.nombre_estudiante,
        cp.descripcion,
        ma.id_matricula,
        cu.fec_pago, 
        cu.monto,
        cu.estado
    FROM
        cuota cu
    INNER JOIN concepto cp ON cp.id_concepto = cu.id_concepto
    INNER JOIN vista_estudiante ev ON ev.id_estudiante = cu.id_estudiante
    INNER JOIN matricula ma ON ma.id_matricula = cu.id_matricula
    WHERE sp_id_cuota = id_cuota
    ORDER BY id_cuota DESC;
END$$
DELIMITER ;