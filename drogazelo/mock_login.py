from django.contrib.auth import login
from django.contrib.auth.models import User

def force_login_middleware(get_response):
    def middleware(request):
        if request.path.startswith('/mock_login/'):
            user = User.objects.get(username='admin')
            login(request, user)
        return get_response(request)
    return middleware
