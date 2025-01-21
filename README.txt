English

This project automates student performance evaluation and email notifications. It includes scripts for querying a PostgreSQL database, calculating total and average scores, filtering approved and rejected students, and sending personalized emails with the results. Additionally, a module named Students-Generator.py allows users to generate a specified number of student records and insert them directly into the PostgreSQL database for further analysis.

Files and Modules:
conn.py: Handles the connection to the PostgreSQL database.
emailconf.py: Manages the email configuration and sending process.
Students-Score.py: Determines approved and rejected students based on their scores and sends personalized emails with detailed summaries.
Students-Generator.py: Inserts the desired number of student records into the PostgreSQL database for later analysis.
email_info_key.txt and key_db.txt: Files to configure email credentials and database connection details, respectively.
Key Functionalities:
Data Analysis: Calculates total and average scores from student grades.
Automation: Automatically filters students (approved ≥ 75, rejected < 75).
Email Notifications: Sends personalized emails to both approved and rejected students.
Data Generation: The Students-Generator.py module simplifies creating synthetic student data and loading it into the database.
Technologies used include Python, pandas, numpy, psycopg2, and custom email configuration modules.
_____________________________________________________________________________________________________________________
Español
Este proyecto automatiza la evaluación del desempeño estudiantil y las notificaciones por correo electrónico. Incluye scripts para consultar una base de datos PostgreSQL, calcular puntuaciones totales y promedios, filtrar estudiantes aprobados y rechazados, y enviar correos personalizados con los resultados. Además, un módulo llamado Students-Generator.py permite a los usuarios generar un número específico de registros de estudiantes e insertarlos directamente en la base de datos PostgreSQL para su posterior análisis.

Archivos y Módulos:
conn.py: Maneja la conexión a la base de datos PostgreSQL.
emailconf.py: Administra la configuración y el envío de correos electrónicos.
Students-Score.py: Determina los estudiantes aprobados y rechazados según sus calificaciones y envía correos personalizados con resúmenes detallados.
Students-Generator.py: Inserta la cantidad deseada de registros de estudiantes en la base de datos PostgreSQL para su posterior análisis.
email_info_key.txt y key_db.txt: Archivos para configurar las credenciales de correo electrónico y los detalles de conexión a la base de datos, respectivamente.
Funcionalidades clave:
Análisis de datos: Calcula las puntuaciones totales y promedios de las calificaciones de los estudiantes.
Automatización: Filtra automáticamente a los estudiantes (aprobados ≥ 75, rechazados < 75).
Notificaciones por correo: Envía correos personalizados a estudiantes aprobados y rechazados.
Generación de datos: El módulo Students-Generator.py simplifica la creación de datos sintéticos de estudiantes y su inserción en la base de datos.
Las tecnologías utilizadas incluyen Python, pandas, numpy, psycopg2 y módulos personalizados de configuración de correo electrónico.
