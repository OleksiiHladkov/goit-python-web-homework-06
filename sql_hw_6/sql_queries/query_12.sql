SELECT gr.id AS group_id, gr.group_name, sb.id AS subject_id, sb.subject_name, st.id AS student_id, st.student, g.date_of AS last_date_of
FROM grades g
	LEFT JOIN subjects sb ON sb.id = g.subject_id
	LEFT JOIN students st ON st.id  = g.student_id
		LEFT JOIN groups gr ON gr.id = st.group_id
WHERE gr.id = :group_id AND sb.id = :subject_id AND g.date_of IN (SELECT MAX(g.date_of)
																	FROM grades g
																		LEFT JOIN subjects sb ON sb.id = g.subject_id
																		LEFT JOIN students st ON st.id  = g.student_id
																			LEFT JOIN groups gr ON gr.id = st.group_id
																	WHERE gr.id = :group_id AND sb.id = :subject_id)