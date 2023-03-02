import profile
from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):

    # Home
    home = Home.objects.latest('updated')
    

    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    # About
    
   
    

    context = {
        'home': home,
        'about':about,
        'profile':profiles,
        'categories':categories,
        'portfolios':portfolios,
        
    }


    return render(request, 'index.html', context)