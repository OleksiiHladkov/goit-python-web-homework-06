SELECT s.group_id, g.group_name , s.id AS student_id, s.student
FROM students s
LEFT JOIN groups g ON s.group_id = g.id
WHERE s.group_id = :group_id;