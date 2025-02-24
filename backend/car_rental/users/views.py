from django.http import HttpResponse

# Create your views here.
def get_user_page(request):
    return HttpResponse('User page')


def get_user_info(request, name):
    surname = request.GET.get('surname', 'Surname not Found')
    return HttpResponse(f'User name: {name}, user surname: {surname}')


def get_user_age(request):
    age = request.GET.get('age', 'Age not found')
    return HttpResponse(f'User age: {age}')
