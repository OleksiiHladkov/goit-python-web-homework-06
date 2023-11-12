SELECT st.id AS student_id, st.student, t.id AS teacher_id, t.teacher, sb.id AS subject_id, sb.subject_name
FROM grades g
	LEFT JOIN subjects sb ON sb.id = g.subject_id
		LEFT JOIN teachers t ON t.id = sb.teacher_id
	LEFT JOIN students st ON st.id  = g.student_id
WHERE g.student_id = :student_id AND t.id = :teacher_id
GROUP BY st.id, st.student, t.id, t.teacher, sb.id, sb.subject_name;