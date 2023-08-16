from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path("graphql/",
         csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
