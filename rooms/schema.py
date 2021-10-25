import graphene
from .types import RoomListResponse, RoomType
from .queries import resolve_rooms, resolve_room


class Query(object):
    rooms = graphene.Field(RoomListResponse,page=graphene.Int(default_value=1), resolver=resolve_rooms)
    room = graphene.Field(RoomType, id=graphene.Int(required=True), resolver=resolve_room)

        