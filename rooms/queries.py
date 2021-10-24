from .models import Room
from .types import RoomListResponse

def resolve_rooms(self,info, page):
    print(page)
    if 1 > page:
        page = 1
    page_size = 15
    skipping = page_size * (page - 1)
    taking = page_size * page
    rooms = Room.objects.all()[skipping:taking]
    total = Room.objects.count()
    return RoomListResponse(arr=rooms,total=total)

def resolve_room(self,info, id):   
    return Room.objects.get(id=id)    
