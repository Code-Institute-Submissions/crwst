from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog, Comment
from .forms import SearchForm, CommentForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def BlogListView(request):
    dataset = Blog.objects.all()
    if request.method == "POST":
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
def BlogDetailView(request, blog_id):
    try:
        data = Blog.objects.get(id=blog_id)
        comments = Comment.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == "POST":
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blog', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. Please ensure form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit blog on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. Please ensure form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing blog {blog.blog_title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog():
    """ Delete a blog from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blogs'))
