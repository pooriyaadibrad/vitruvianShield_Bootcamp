from django.http import JsonResponse
from .models import User


def index(request):
    users = User.objects.all()
    users=[
        {
            'username':obj.username,
            'email':obj.email,
            'mobile':obj.mobile
        }for obj in users
    ]
    return JsonResponse(users, safe=False)
