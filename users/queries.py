from .models import User

def resolve_user(self, info, id):
    return User.objects.get(id=id)

def resolve_me(self, info):
    user = info.context.user
    if user.is_authenticated:
        return info.context.user
    else:
        raise Exception("You need to be logged in")