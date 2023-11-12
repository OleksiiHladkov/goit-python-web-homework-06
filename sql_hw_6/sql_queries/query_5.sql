SELECT s.teacher_id, t.teacher, s.id, s.subject_name
FROM subjects s
LEFT JOIN teachers t ON s.teacher_id = t.id
ORDER BY teacher_id;