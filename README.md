# hair_salon_appointments

Documentación del Proyecto

**Versión de Python recomendada: Python 3.12.0**

## Configuración
Para configurar el proyecto, necesitarás establecer algunas variables de entorno en un archivo .env. Este archivo debe estar en la raíz del proyecto.

## Variables de entorno
Las siguientes variables de entorno son necesarias para el proyecto:

EMAIL: Este es el correo electrónico que se utilizará para las pruebas. Debe ser una cuenta de Gmail y no debe tener habilitada la verificación en dos pasos.
PASSWORD: Esta es la contraseña de la cuenta de correo electrónico especificada en EMAIL.
Aquí hay un ejemplo de cómo debería verse tu archivo .env:

````plaintext
  EMAIL=tu_correo@gmail.com
  PASSWORD=tu_contraseña
````

Por favor, reemplaza tu_correo@gmail.com y tu_contraseña con tu dirección de correo electrónico de Gmail y tu contraseña, respectivamente.

## Instalación de dependencias
Para instalar las dependencias del proyecto, ejecuta el siguiente comando en la terminal:
````plaintext
pip install -r requirements.txt
````
## Ejecución del proyecto
Para ejecutar el proyecto, utiliza el siguiente comando en la terminal:
````plaintext
   uvicorn main:app --reload --port 5000 --host 0.0.0.0
````
Este comando inicia el servidor con Uvicorn, carga la aplicación desde el archivo main (asegúrate de que el archivo y la variable de la aplicación app estén correctamente nombrados según tu proyecto), y establece el puerto y el host. El uso de --reload habilita la recarga automática cuando se realizan cambios en el código.

Asegúrate de que las dependencias estén instaladas antes de ejecutar este comando. Puedes instalarlas usando el comando pip install -r requirements.txt, como se menciona en la sección de instalación de dependencias.

## Pruebas
Para ejecutar pruebas específicas en el proyecto, utiliza los siguientes comandos en la terminal:

```bash
# Ejecutar pruebas en el módulo testLogicaCliente
python -m unittest app.test.testLogicaCliente

# Ejecutar pruebas en el módulo testLogicaServicio
python -m unittest app.test.testLogicaServicio

# Ejecutar pruebas en el módulo testLogicaPeluquero
python -m unittest app.test.testLogicaPeluquero

# Ejecutar pruebas en el módulo testLogicaCita
python -m unittest app.test.testLogicaCita

````

## Interfaz de Usuario de Swagger
Puedes acceder a la interfaz de usuario de Swagger para explorar la documentación de la API utilizando el siguiente enlace: http://localhost:5000/docs
