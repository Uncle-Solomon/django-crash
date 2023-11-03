from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {"id": 5, "title": "The Shawshank Redemption", "year": 1994},
        {"id": 623, "title": "The Godfather", "year": 1972},
        {"id": 680, "title": "The Dark Knight Rises", "year": 2012}
    ]
    
}


def movies(request):
    return render(request, "movies/movies.html", data)


def home(request):
    return HttpResponse("Home Page")

