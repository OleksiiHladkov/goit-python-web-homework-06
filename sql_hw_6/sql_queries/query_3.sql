SELECT s.group_id, gr.group_name, g.subject_id, sub.subject_name, ROUND(AVG(g.grade), 1) AS avg_grade
FROM grades g
	LEFT JOIN students s ON s.id = g.student_id
		LEFT JOIN groups gr ON gr.id = s.group_id
	LEFT JOIN subjects sub ON g.subject_id = sub.id
WHERE g.subject_id = :subject_id
GROUP BY s.group_id, gr.group_name, g.subject_id, sub.subject_name;