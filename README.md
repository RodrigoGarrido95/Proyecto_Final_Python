# Proyecto_Final_Python
Proyecto final para el curso de python en Coder_house
# Mi Blog - Proyecto Final Python

## Descripción del proyecto

Blog personal desarrollado con Django que permite a los usuarios registrarse, iniciar sesión y publicar entradas de blog. El proyecto resuelve la necesidad de contar con un espacio simple y personal donde compartir contenido escrito, sin depender de plataformas de terceros.

**Funcionalidades principales:**
- Registro e inicio de sesión de usuarios
- Creación y visualización de entradas de blog (posts)
- Panel de administración para gestionar contenido y usuarios
- Formularios con validación de datos


## Funcionalidades implementadas

- **Panel de administración (Admin):** acceso en `/admin/` para gestionar posts y usuarios registrados.
- **Registro y autenticación de usuarios:** los usuarios pueden crear una cuenta, iniciar sesión y cerrar sesión.
- **Páginas funcionales:** página principal con listado de posts, y vista de detalle de cada post.
- **Formularios con validación:** el formulario de creación de posts valida que el título tenga al menos 5 caracteres y el contenido al menos 20, mostrando errores si no se cumplen.

## Requisitos previos

- Python 3.10 o superior
- pip
- Git

## Instalación y ejecución local

1. Clonar el repositorio:
git clone https://github.com/RodrigoGarrido95/Proyecto_Final_Python.git
cd Proyecto_Final_Python/Mi_Blog

## Crear un superusuario (acceso al panel de administración)

Para poder acceder al panel de administración en `/admin/`, es necesario crear un superusuario:

El sistema pedirá:
- **Username:** nombre de usuario para el superusuario
- **Email:** opcional, se puede dejar en blanco
- **Password:** contraseña (no se muestra en pantalla mientras se escribe)

Una vez creado, se puede iniciar sesión en `http://127.0.0.1:8000/admin/` (o en la URL pública + `/admin/`) con esas credenciales.

## Checklist de requisitos y evidencia

| Requisito | Implementación | Evidencia |
|---|---|---|
| Panel de administración | Django Admin en `/admin/`, con el modelo Post registrado | Captura del panel admin con listado de posts |
| Registro de usuarios | Formulario en `/registro/` con `UserCreationForm` | Captura del formulario de registro completado |
| Inicio de sesión | Formulario en `/login/` con `LoginView` | Captura del login |
| Perfiles / gestión de usuarios | Gestionable desde el panel admin (`/admin/auth/user/`) | Captura de la lista de usuarios en el admin |
| Páginas funcionales | Home con listado de posts y vista de detalle | Captura de home y de detalle de un post |
| Formularios con validación | Formulario de creación/edición de posts, valida longitud mínima de título (5) y contenido (20) | Captura del formulario y del mensaje de error de validación |
| Edición de contenido | Los usuarios pueden editar sus propios posts desde `/post/<id>/editar/` | Captura de edición y del post actualizado (persistencia) |
ura accediendo desde el navegador a la URL pública |

2. Crear y activar el entorno virtual:

python -m venv venv

   En Windows (PowerShell):

.\venv\Scripts\Activate.ps1

   En Windows (Git Bash):

source venv/Scripts/activate


3. Instalar las dependencias:

pip install -r requirements.txt


4. Aplicar las migraciones:

python manage.py migrate


5. (Opcional) Crear un superusuario para acceder al panel de administración:

python manage.py createsuperuser


6. Ejecutar el servidor de desarrollo:

python manage.py runserver


7. Abrir en el navegador:

http://127.0.0.1:8000/


## Despliegue

Este proyecto no se encuentra desplegado en un servidor público, pero a continuación se detalla el proceso que se seguiría para desplegarlo en **Render** (servicio gratuito de hosting):

1. **Crear una cuenta en Render** (render.com) y conectarla con el repositorio de GitHub del proyecto.

2. **Configurar variables de entorno** necesarias, como `SECRET_KEY` y `DEBUG=False`, para producción.

3. **Ajustar `ALLOWED_HOSTS`** en `settings.py` para incluir el dominio que asigne Render (por ejemplo, `mi-blog.onrender.com`).

4. **Agregar un servidor de producción** como Gunicorn al archivo `requirements.txt`, ya que el servidor de desarrollo de Django (`runserver`) no está pensado para producción.

5. **Configurar el Build Command** en Render para que instale las dependencias y ejecute las migraciones automáticamente:

pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput


6. **Configurar el Start Command** para levantar el servidor con Gunicorn:

gunicorn Mi_Blog.wsgi


7. La aplicación se encuentra desplegada en Render y accesible públicamente en: https://proyecto-final-python-3t2j.onrender.com/ accesible desde cualquier lugar.

**Entorno de despliegue:** Render (plan gratuito), usando Gunicorn como servidor WSGI, Whitenoise para servir archivos estáticos, y una base de datos PostgreSQL provista por Render.

De esta manera, cualquier usuario podría acceder a la aplicación sin necesidad de tenerla corriendo localmente.