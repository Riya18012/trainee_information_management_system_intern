# decorators.py

from django.shortcuts import redirect

def user_is_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        print("Decorator is being executed")  # Add this line
        if not request.user.is_staff:
            return redirect('login')  # Redirect non-admin users to login
        return view_func(request, *args, **kwargs)
    return _wrapped_view
