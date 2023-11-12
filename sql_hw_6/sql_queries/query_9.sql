SELECT st.id AS student_id, st.student, sb.id AS subject_id, sb.subject_name
FROM grades g
	LEFT JOIN subjects sb ON sb.id = g.subject_id
	LEFT JOIN students st ON st.id  = g.student_id 
WHERE g.student_id = :student_id
GROUP BY st.id, st.student, sb.id, sb.subject_name;