from functools import wraps

from django.shortcuts import render


def login_check(func):
    @wraps(func)
    def wrapper(request):
        if 'id' in request.session:
            return func(request)
        else:
            return render()