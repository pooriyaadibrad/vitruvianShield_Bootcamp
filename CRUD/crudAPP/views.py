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


def create_user(request):
    """
    this function create new user
    :param request: request user
    :return: success return Json response with user data be created
    """
    """
    we need this data for updating user
    
    user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                    mobile=request.POST['mobile'])
    user.save()
    """
    return JsonResponse({'message': 'success create user'})


def update_user(request, pk):
    """
    this function update user specific data from database
    :param request: user request
    :param pk: primary key of user to update
    :return: json response with user data we update it
    """
    user = User.objects.get(id=pk)
    """
    we need this data for updating user

    user.username = request.POST['username']
    user.email = request.POST['email']
    user.mobile = request.POST['mobile']
    
    user.save()
    """
    return JsonResponse({'username': user.username, 'email': user.email, 'mobile': user.mobile})


def delete_user(request, pk):
    """
    this function delete user specific data from database
    :param request: user request
    :param pk: primary key of user to delete
    :return: Json response with success message
    """
    user = User.objects.get(id=pk)
    user.delete()
    return JsonResponse({'message': 'user deleted successfully'})
