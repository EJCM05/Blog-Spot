from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Core.models import Post
from django.contrib.auth.forms import UserCreationForm # This is a simple form for user creation
from django.shortcuts import render, redirect

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts' # La variable que usarás en el template para los posts
    paginate_by = 5 # Tu paginación existente

    def get_queryset(self):
        # 1. Empieza con el queryset de todos los posts publicados (tu lógica actual)
        queryset = Post.objects.filter(status=1).order_by('-published_date')
        
        # 2. Verifica si se pasó una categoría en la URL (a través de kwargs)
        #    'category_name' es el nombre que usamos en blog/urls.py para capturar la categoría.
        category_name = self.kwargs.get('category_name') 
        
        # 3. Si hay una categoría en la URL, filtra el queryset por esa categoría
        if category_name:
            # Filtra por el campo 'category' de tu modelo Post.
            # Puedes usar 'category__iexact=category_name' si quieres que la coincidencia sea
            # insensible a mayúsculas/minúsculas (ej. "world" y "World" funcionen igual).
            # Dado que tus CHOICESCATEGORY usan mayúsculas iniciales, un simple 'category=category_name' es suficiente
            # si los valores de la URL coinciden exactamente con los de tus CHOICESCATEGORY.
            queryset = queryset.filter(category=category_name) 
        
        return queryset

    def get_context_data(self, **kwargs):
        # Llama a la implementación base para obtener el contexto por defecto
        context = super().get_context_data(**kwargs)
        
        # Añade todas las opciones de categoría definidas en tu modelo Post al contexto.
        # Esto permite que tu template las itere para construir la navegación.
        context['all_categories'] = Post.CHOICESCATEGORY 
        
        # Añade la categoría que se está viendo actualmente (si existe en la URL) al contexto.
        # Esto es útil para resaltar la categoría activa en tu barra de navegación.
        context['active_category'] = self.kwargs.get('category_name')
        
        return context

# Vista para mostrar los detalles de un post individual
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug' # Usa el slug de la URL para encontrar el post

# Vista para crear un nuevo post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'slug', 'content', 'category', 'status'] # Campos que aparecerán en el formulario

    def form_valid(self, form):
        # Asigna automáticamente el autor del post al usuario logeado
        form.instance.author = self.request.user
        return super().form_valid(form)

# Vista para actualizar un post existente
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'slug', 'content', 'category','status']

    def test_func(self):
        # Solo permite al autor del post editarlo
        post = self.get_object()
        return self.request.user == post.author

# Vista para eliminar un post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('Blog:post_list') # Redirige a la lista de posts después de eliminar

    def test_func(self):
        # Solo permite al autor del post eliminarlo
        post = self.get_object()
        return self.request.user == post.author
    
class SignUpView(CreateView):
    form_class = UserCreationForm # Use Django's built-in user creation form
    success_url = reverse_lazy('Blog:login') # Redirect to login page after successful registration
    template_name = 'registration/signup.html' # Points to the template we discussed
