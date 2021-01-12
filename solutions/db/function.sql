CREATE DEFINER=`root`@`localhost` FUNCTION `check_teacher`(
	teacher_id INT,
    subject_id INT
) RETURNS tinyint(1)
BEGIN
	IF EXISTS (SELECT * FROM subject_teacher st WHERE st.teacher_id = teacher_id AND st.subject_id = subject_id) THEN
		RETURN TRUE;
	ELSE
		RETURN FALSE;
	END IF;
END


CREATE TABLE class_subject_teacher (
    class_id INT,
    teacher_id INT,
    subject_id INT,
    CONSTRAINT fk_cst_primary_key PRIMARY KEY (class_id , teacher_id , subject_id),
    CONSTRAINT fk_cst_class_id FOREIGN KEY (class_id)
        REFERENCES class (class_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_cst_subject_teacher FOREIGN KEY (teacher_id , subject_id)
        REFERENCES subject_teacher (teacher_id , subject_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);