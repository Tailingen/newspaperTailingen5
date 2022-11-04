from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'new'

class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.neworart = False
        return super().form_valid(form)

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.neworart = True
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/article_edit.html'

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'flatpages/article_delete.html'
    success_url = reverse_lazy('post_list')
