DELIMITER //

CREATE PROCEDURE AsignarRecursosAProyectos()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_ProyectoId INT;
    DECLARE v_RecursosNecesarios INT;
    DECLARE v_RecursosAsignados INT;
    DECLARE v_CantidadDisponible INT;

    DECLARE ProyectoCursor CURSOR FOR
    SELECT ProyectoId, RecursosNecesarios, RecursosAsignados
    FROM Proyectos
    WHERE Estado = 'Pendiente'
    ORDER BY RecursosNecesarios DESC;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    START TRANSACTION;

    OPEN ProyectoCursor;

    read_loop: LOOP
        FETCH ProyectoCursor INTO v_ProyectoId, v_RecursosNecesarios, v_RecursosAsignados;

        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT SUM(CantidadDisponible) INTO v_CantidadDisponible
        FROM RecursosDisponibles;

        IF v_CantidadDisponible >= v_RecursosNecesarios THEN
            UPDATE Proyectos
            SET RecursosAsignados = v_RecursosNecesarios,
                Estado = 'En Curso'
            WHERE ProyectoId = v_ProyectoId;

            UPDATE RecursosDisponibles
            SET CantidadDisponible = CantidadDisponible - v_RecursosNecesarios
            WHERE CantidadDisponible >= v_RecursosNecesarios
            LIMIT 1;
        END IF;
    END LOOP;

    CLOSE ProyectoCursor;

    COMMIT;
END;
//

DELIMITER ;