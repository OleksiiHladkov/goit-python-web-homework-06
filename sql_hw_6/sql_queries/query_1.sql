SELECT g.student_id, s.student, ROUND(AVG(g.grade), 1) as avg_grade
FROM grades g
	LEFT JOIN students s ON s.id = g.student_id 
GROUP BY g.student_id
ORDER BY avg_grade DESC
LIMIT 5;