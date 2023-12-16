from django.contrib import admin
#from django.apps import apps
from auctions.models import Bid, Comment
from . models import User, Category, Listing, Bid

# Register your models here.

"""
app_config = apps.get_app_config('auctions') 
models = app_config.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass"""

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)