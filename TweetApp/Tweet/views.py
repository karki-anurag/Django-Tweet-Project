from django.shortcuts import render
from .models import Tweet
from .forms import TweetForms
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def landing_page(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')
    return(request, 'home.html', {'tweet': tweet})

def tweet_create(request):
    if request.method == "POST":
      form = TweetForms(request.POST, request.FILES)
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('tweet_list')
    else:
        form = TweetForms()
    return(request, 'form_create.html', {'form': form})


def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        else:
            form = TweetForms(instance=tweet)
    return(request, 'form_create.html', {'form': form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POSt':
        tweet.delete()
        return redirect('tweet_list')
    return(request, 'tweet_confirm_delete.html', {'tweet': tweet})