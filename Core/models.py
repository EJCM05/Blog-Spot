from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # Necesario para el autor del post

class Post(models.Model):
    CHOICESCATEGORY = (
        ("World", "World"),("U.S", "U.S"),("Technology", "Technology"),("Desing", "Desing"),("Culture", "Culture"),("Business", "Business")
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="Un slug es una versión amigable del título para las URLs (ej: mi-primer-post).")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    category = models.CharField(choices=CHOICESCATEGORY, max_length=20, default="World", help_text="Categoría del post")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=((0, "Borrador"), (1, "Publicado")), default=0)

    class Meta:
        # Ordena los posts por fecha de publicación descendente por defecto
        ordering = ['-published_date']

    def __str__(self):
        # Representación de cadena del objeto Post
        return self.title

    def get_absolute_url(self):
        # Define la URL canónica para un post individual.
        # Esto es útil para CreateView y UpdateView para saber a dónde redirigir después de guardar.
        return reverse('Blog:post_detail', kwargs={'slug': self.slug})