from django.contrib import admin
from .models import TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Item, Promo


for model in [TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Promo]:
    admin.site.register(model)
