SELECT t.id AS teacher_id, t.teacher, st.id AS student_id, st.student, ROUND(AVG(g.grade), 1) AS avg_grade 
FROM grades g
	LEFT JOIN subjects sb ON sb.id = g.subject_id
		LEFT JOIN teachers t ON t.id = sb.teacher_id
	LEFT JOIN students st ON st.id  = g.student_id
WHERE g.student_id = :student_id AND t.id = :teacher_id
GROUP BY t.id, t.teacher, st.id, st.student;