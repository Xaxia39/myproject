# My Django Project

Este proyecto es una aplicación web en Django que sigue el patrón MVT. Contiene:

1. Herencia de HTML.
2. Al menos 3 clases en models (Author, Category, Book).
3. Formularios para insertar datos en todas las clases de models.
4. Un formulario para buscar libros en la base de datos.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/myproject.git
    cd myproject
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Realiza las migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Funcionalidades

1. **Home**: Página principal con enlaces a todas las funcionalidades.
2. **Agregar Autor**: Formulario para agregar un nuevo autor.
3. **Agregar Categoría**: Formulario para agregar una nueva categoría.
4. **Agregar Libro**: Formulario para agregar un nuevo libro.
5. **Buscar**: Formulario para buscar libros por título.

## Pruebas

Para probar las funcionalidades, sigue estos pasos:

1. Accede a la página principal: `http://127.0.0.1:8000/`
2. Agrega un autor, una categoría y un libro usando los formularios correspondientes.
3. Utiliza la función de búsqueda para encontrar un libro por su título.

echo "# miproyecto" >> README.md 
git init 
git add README.md 
git commit -m "primer compromiso" 
git rama -M principal 
git remoto agregar origen https://github.com/Xaxia39/myproject.git
 git push - u origen principal