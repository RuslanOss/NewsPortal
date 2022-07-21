from django.views.generic import\
    ListView,\
    DetailView,\
    CreateView,\
    UpdateView,\
    DeleteView


from .forms import PostForm
from .filters import PostFilter
from django.urls import reverse_lazy
from datetime import datetime
from .models import Post
from django.contrib.auth.mixins import PermissionRequiredMixin



class PostsList(ListView):
    model = Post
    permission_required = (
        'news.view_post',
    )
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs




class PostDetail(DetailView):
    model = Post
    permission_required = (
        'news.view_post',
    )
    template_name = 'new.html'
    context_object_name = 'new'



class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = (
        'news.add_post',
    )
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')


    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        if current_url.split('/')[1] == 'news':
            post.categoryType = self.model.NEWS
        else:
            post.categoryType = self.model.ARTICLE
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    permission_required = (
        'news.change_post',
    )
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        post = Post.objects.get(pk=id)
        post.isUpdated = True
        return post


class PostDelete(DeleteView):
    model = Post
    permission_required = (
        'news.change_post',
    )
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')



class SearchListViews(PostsList):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context