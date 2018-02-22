from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf

from blog.models import Article, Comments
from blog.forms import CommentForm


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def show_article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    return render_to_response('blog/article.html', args)


def addcomment(request, article_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.comments_article = Article.objects.get(id=article_id)
        form.save()
    return redirect('/article/%s/' % article_id)
