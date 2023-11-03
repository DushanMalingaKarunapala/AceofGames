from django.shortcuts import render
from .models import StoreItemDes  # import the created class in models.py
from .models import StoreItemDes, StoreNewGamesSlide

# Create your views here.


def gaming(request):
    return render(request, "gaming.html")


def Store(request):

    # item1 = StoreItemDes()
    # item1.price = 51
    # item1.discount = 50
    # item1.image = 's_product_img01.jpg'
    # item1.description = 'E sport gaming jersey bro'

    # item2 = StoreItemDes()
    # item2.price = 49
    # item2.discount = 25
    # item2.image = 'out.jpg'
    # item2.description = 'E sport gaming jersey bro'

    # item3 = StoreItemDes()
    # item3.price = 12
    # item3.discount = 3
    # item3.image = 'product_img01.jpg'
    # item3.description = 'E sport gaming jersey ekak'

    # items = [item1, item2, item3] before i fetch the data from database and display using .objects.all() function ,you created these objects above manually and passed them using a list
    # passing the create objects to the store.html using a list
    # this function will fetch the data from storeitemdes table

    items = StoreItemDes.objects.all()
    games = StoreNewGamesSlide.objects.all()
    context = {'items': items, 'games': games}
    return render(request, 'Store.html', context)

    # return render(request, 'Store.html',{'games': games})


def forza(request):
    return render(request, "forza.html")
