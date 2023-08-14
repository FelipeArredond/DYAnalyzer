create_user.sql
USE BD_Usuarios;
GO
CREATE USER lfarredong WITH PASSWORD='Fe24062020;*$'
GO
GRANT CONTROL ON DATABASE::BD_Usuarios TO admin;
GO
EOF