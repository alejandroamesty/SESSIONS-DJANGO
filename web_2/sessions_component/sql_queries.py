CREATE_USER = 'INSERT INTO "user" (username, password, email, created_at, last_login) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING user_id'
DELETE_USER = 'DELETE FROM "user" WHERE username = %s'
ASSIGN_ROLE = 'INSERT INTO user_has_role (user_id, role_id) VALUES (%s, %s)'
DELETE_ROLE = 'DELETE FROM user_has_role WHERE user_id = %s'
CHECK_USER = 'SELECT user_id, temporary, password_expires_at FROM "user" WHERE username = %s AND password = %s'
UPDATE_LOGIN = 'UPDATE "user" SET last_login = CURRENT_TIMESTAMP WHERE username = %s'
CHANGE_PASSWORD = 'UPDATE "user" SET password = %s, temporary = FALSE, password_expires_at = NULL WHERE username = %s'
CHECK_ROLE = 'SELECT role_id FROM user_has_role WHERE user_id = (SELECT user_id FROM "user" WHERE username = %s)'
CHECK_PERMISSION = 'SELECT 1 FROM permission AS p INNER JOIN method AS m ON p.method_id = m.method_id INNER JOIN object AS o ON m.object_id = o.object_id WHERE p.role_id = %s AND m.method_na = %s AND o.object_na = %s'
UPDATE_TEMPORARY_PASSWORD = 'UPDATE "user" SET password = %s, temporary = %s, password_expires_at = %s WHERE username = %s'
UPDATE_PASSWORD = 'UPDATE "user" SET password = %s, temporary = %s WHERE username = %s'
GET_USER_BY_EMAIL = 'SELECT username FROM "user" WHERE email = %s'