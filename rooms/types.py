import graphene
from graphene_django import DjangoObjectType
from .models import Room

class RoomType(DjangoObjectType):

    is_favs = graphene.Boolean()

    user = graphene.Field("users.types.UserType")

    class Meta:
        model = Room
    
    def resolve_is_favs(parent, info):
        user = info.context.user
        if user.is_authenticated:
            return parent in user.favs.all()
        return False

class RoomListResponse(graphene.ObjectType):

    arr  = graphene.List(RoomType)
    total = graphene.Int()