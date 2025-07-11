# BlogSpot - Un Proyecto de Blog con Django

Este es un proyecto de blog personal desarrollado con el framework web **Django**, diseñado para demostrar mis habilidades en desarrollo web backend y frontend básico, manejo de bases de datos y la implementación de funcionalidades clave en un entorno de práctica, tuve la sensacion y la necesidad de tener que centrarme en las CBVs Con django, los metodos de autenticacion **auth** y modelos basicos pero potentes. Me centre en las funcionalidades del Backend para llevar a cabo esta practica, Utilice **Bootstrap** para el Frontend con una plantilla predefinida, que me permitiera enforcarme mas en la funcionalidad.

---

## Características Implementadas

* **Gestión de Posts:**
    * **CRUD completo:** Los usuarios autenticados pueden **Crear**, **Leer**, **Actualizar** y **Eliminar** posts.
    * **Visualización de posts individuales:** Cada post tiene su propia página detallada.
    * **Paginación:** Los posts se muestran en páginas para mejorar la navegación.
* **Categorías Dinámicas:**
    * Posts organizados por categorías predefinidas (ej. World, Technology, Culture, Business).
    * **Navegación dinámica:** Una barra de navegación superior muestra todas las categorías disponibles.
    * **Filtrado por categoría:** Al hacer clic en una categoría, solo se muestran los posts relacionados con ella.
* **Sistema de Autenticación de Usuarios:**
    * **Registro seguro** de nuevos usuarios.
    * **Inicio y cierre de sesión** utilizando el sistema de autenticación robusto de Django.
    * **Protección de rutas:** Solo los usuarios autenticados pueden acceder a las funcionalidades de creación, edición y eliminación de posts.
* **URLs Amigables (Slugs):**
    * Implementación de campos `SlugField` para generar URLs legibles y optimizadas para motores de búsqueda (ej: `.../post/mi-primer-post/`).
* **Base de Datos SQLite3:** Configuración por defecto de Django, ideal para desarrollo y proyectos pequeños.
* **Panel de Administración de Django:** Acceso y uso del potente panel de administración para gestionar posts, usuarios y categorías de manera eficiente.
* **Estilos:** Interfaz de usuario básica y responsiva construida con **Bootstrap 5**.

---

## 🛠️ Tecnologías Utilizadas

* **Python**
* **Django** 
* **Bootstrap**
* **SQLite3**

---

## 💻 Configuración y Ejecución Local

Sigue estos pasos para clonar el proyecto y ejecutarlo en tu máquina local:

1.  **Clonar el repositorio:**

2.  **Crear y activar un entorno virtual:**

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones y crear un superusuario:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser # Sigue las instrucciones en pantalla para crear un usuario administrador
    ```

5.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
---

## Proceso de Desarrollo y Aprendizajes Clave

Este proyecto sirvió como una excelente oportunidad para profundizar en varios aspectos fundamentales de Django:

* **Vistas Basadas en Clases (CBVs):** Aprendí a utilizar y personalizar `ListView`, `DetailView`, `CreateView`, `UpdateView` y `DeleteView` para manejar operaciones de datos de manera eficiente, comprendiendo cómo sobrescribir métodos como `get_queryset` y `get_context_data` para adaptar su funcionalidad a requisitos específicos, como el filtrado por categoría.

* **Sistema de Autenticación y Autorización de Django (`django.contrib.auth`):** Implementé el registro, inicio y cierre de sesión, así como la protección de vistas con `LoginRequiredMixin`, entendiendo la importancia de la seguridad en acciones del usuario y el uso de `{% csrf_token %}`.

* **Organización de URLs con Namespaces:** Practiqué la definición de patrones de URL y el uso de `namespaces` (ej. `blog:` para mis URLs de app y `auth:` para las de autenticación de Django) para mantener el proyecto modular y escalable.

* **Diseño de Modelos:** Reforcé el uso de campos como `SlugField` para URLs amigables y `CharField` con `choices` para opciones predefinidas, y cómo se relacionan con el diseño de la base de datos.

* **Gestión de Plantillas:** Aprendí a crear plantillas dinámicas utilizando el lenguaje de plantillas de Django, incluyendo bucles, condicionales y la generación de URLs con `{% url %}`.

* **Control de Versiones:** Utilicé Git para el control de versiones, gestionando el historial del proyecto a través de commits y sincronizándolo con GitHub.

---

## Contacto

* **Eber Josue Colmenares Mendoza**
* [LinkedIn](https://www.linkedin.com/in/eber-josue-colmenares-mendoza)
* Correo Electrónico: `ebercolmenares_11@hotmail.com`