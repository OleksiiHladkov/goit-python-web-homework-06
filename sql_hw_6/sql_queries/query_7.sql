SELECT gr.id AS group_id, gr.group_name, sub.id AS subject_id, sub.subject_name, s.id AS student_id, s.student, g.grade
FROM grades g
	LEFT JOIN students s ON s.id = g.student_id
	LEFT JOIN groups gr ON s.group_id = gr.id
	LEFT JOIN subjects sub ON sub.id = g.subject_id
WHERE s.group_id = :group_id AND g.subject_id = :subject_id;