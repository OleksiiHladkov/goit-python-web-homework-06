SELECT g.student_id, s.student, g.subject_id, sub.subject_name, ROUND(AVG(g.grade), 1) AS avg_grade
FROM grades g
	LEFT JOIN students s ON s.id = g.student_id
	LEFT JOIN subjects sub ON g.subject_id = sub.id
WHERE g.subject_id = :subject_id
GROUP BY g.student_id, s.student, g.subject_id, sub.subject_name
ORDER BY avg_grade DESC
LIMIT 1;