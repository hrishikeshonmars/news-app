from django.shortcuts import render
import requests

def index(request):
    r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2024-02-19&sortBy=publishedAt&apiKey=7c18002615b342108434ae8b11bb59b0')
    res = r.json()
    
    # Check if 'articles' key exists in the response
    if 'articles' in res:
        articles = res['articles']
        title = []
        description = []
        images = []
        url = []
        
        for article in articles:
            title.append(article['title'])
            description.append(article['description'])
            images.append(article.get('urlToImage', ''))  # Handle the case where image is missing
            url.append(article['url'])
            
        news = zip(title, description, images, url)
        return render(request, 'newsapp/index.html', {'news': news})
    else:
        error_message = "No articles found."
        return render(request, 'newsapp/error.html', {'error_message': error_message})
    
