from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from music.models import Article, Single, Album, Video, Actual


def home(request):
    news = Article.objects.order_by('-id')[:2]
    actual = Actual.objects.get()
    video = Video.objects.last()
    context = {
        "news": news,
        "actual": actual,
        "video": video
    }
    return render(request, 'music/home.html', context)

def music(request):
    singles = Single.objects.order_by('-id')
    albums = Album.objects.order_by('-id')
    context = {
        "singles": singles,
        "albums": albums
    }
    return render(request, 'music/music.html', context)


def videos(request):
    videos = Video.objects.order_by('-id')
    context = {
        "videos": videos
    }
    return render(request, 'music/videos.html', context)

# def blog(request):
#     news = Article.objects.order_by('-id')
#     context = {
#         "news": news
#     }
#     return render(request, 'music/blog.html', context)

def shop(request):
    return render(request, 'music/shop.html')

def tour(request):
    return render(request, 'music/tour.html')

def media(request):
    return render(request, 'music/media.html')

def show_news(request, article_id):
    news = Article.objects.order_by('-id')[:4]

    article = get_object_or_404(Article, id=article_id)
    return render(request, 'music/news.html', {'article': article, 'news': news})

def blog(
        request,
        template='music/blog.html',
        page_template='music/blog_news.html'):
    context = {
        'news': Article.objects.order_by('-id'),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(
        template, context, context_instance=RequestContext(request))