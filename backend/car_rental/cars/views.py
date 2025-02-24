from django.http import HttpResponse

# Create your views here.
def get_view(request):
    return HttpResponse('Home page')


def get_view_with_arg(request, arg):
    return HttpResponse(f'Page with argument: {arg}')


def get_view_with_param(request):
    parametr = request.GET.get('name', 'Not parametr')
    return HttpResponse(f'Page with parametr: {parametr}')
