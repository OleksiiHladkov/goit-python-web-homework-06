SELECT t.id AS teacher_id, t.teacher, s.id AS subject_id, s.subject_name, ROUND(AVG(g.grade), 1) AS avg_grade
FROM grades g
	LEFT JOIN subjects s ON s.id = g.subject_id
	LEFT JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = :teacher_id
GROUP BY t.id, t.teacher, s.id, s.subject_name;