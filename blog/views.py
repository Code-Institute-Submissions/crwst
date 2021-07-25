from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog, Comment
from .forms import SearchForm, CommentForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Basic structure of models adapted taken from
# (https://www.askpython.com/django/django-blog-app)


def BlogListView(request):
    """ A view to see all the blog posts and search function """
    dataset = Blog.objects.all()
    query = None
    form = SearchForm()
    if request.GET:
        if 'title' in request.GET:
            query = request.GET['title']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('blogs'))

            queries = Q(blog_title__icontains=query) | Q(blog__icontains=query)
            dataset = dataset.filter(queries)

    context = {
            'dataset': dataset,
            'search_term': query,
            'form': form,
        }
    return render(request, 'blog/listview.html', context)


def BlogDetailView(request, _id):
    """ A view to see an individual blog post
    and if authorised add comments """
    try:
        data = Blog.objects.get(id=_id)
        comments = Comment.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if not request.user:
            messages.error(request,
                           'Sorry, only registered shoppers can do that.')
            return redirect(reverse('blogs'))
        if form.is_valid():
            comment_variable = Comment(author=request.user,
                                       comment_text=form.cleaned_data[
                                           'comment_text'
                                           ],
                                       blog=data)
            comment_variable.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(f'/blogs/blog/{_id}/')
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
            messages.error(request,
                           'Failed to add blog. Please ensure form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, _id):
    """ Edit blog on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog', args=[blog.id]))
        else:
            messages.error(request,
                           'Failed to update blog.'
                           + 'Please ensure form is valid.')
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
def delete_blog(request, _id):
    """ Delete a blog from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blogs'))
