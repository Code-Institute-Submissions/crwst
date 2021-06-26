from django.shortcuts import render, redirect
from .models import Blog, Comment
from .forms import SearchForm, CommentForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def BlogListView(request):
    dataset = Blog.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = Blog.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset': dataset,
            'form': form,
        }
    return render(request, 'blog/listview.html', context)


@login_required
def BlogDetailView(request, _id):
    try:
        data = Blog.objects.get(id=_id)
        comments = Comment.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = Comment(author=form.cleaned_data['author'],
                comment_text=form.cleaned_data['comment_text'],
                blog=data)
            Comment.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()

    context = {
            'data': data,
            'form': form,
            'comments': comments,
        }
    return render(request, 'blog/detailview.html', context)


@login_required
def add_blog(request):
    """ Add a blog to the site """
    form = BlogForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
