from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # if user is authenticated redirect to managelist page otherwise do nothing

        if request.user.is_authenticated:
            return redirect('managelist')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            # if user has a group, get the name
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            # if the group is in the allowed roles then redirect to view function
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')

            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
