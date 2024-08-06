from django.http import JsonResponse
from .models import User


def index(request):
    """
    this READ functions and read all data form database
    :param request: user request
    :return: return a Json response with user data
    """
    users = User.objects.all()
    users = [
        {
            'username': obj.username,
            'email': obj.email,
            'mobile': obj.mobile
        } for obj in users
    ]
    return JsonResponse(users, safe=False)


def get_user(request, pk):
    """
    this function get user specific data from database
    :param request: user request
    :param pk: we look for user with this is
    :return: Json response with specific user data
    """
    user = User.objects.get(id=pk)
    return JsonResponse({'username': user.username, 'email': user.email, 'mobile': user.mobile})
