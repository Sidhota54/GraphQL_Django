import graphene  
from .models import Books
from graphene_django import DjangoObjectType


class BooksType(DjangoObjectType):
    class Meta:
        model =Books
        fields = ("id","title","excerpt")

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    def resolve_all_books(root, info):
        return Books.objects.all()
        # return Books.objects.filter(title ="django")

schema = graphene.Schema(query=Query)