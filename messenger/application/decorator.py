from django.shortcuts import redirect
from functools import wraps

def login_needed(function=None, redirect_field_name='login'):
    def decorator(view_func):
        @wraps(view_func)
        def check(request, *args, **kwargs):
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            return redirect(redirect_field_name)
        return check
    if function is not None:
        return decorator(function)
    return decorator