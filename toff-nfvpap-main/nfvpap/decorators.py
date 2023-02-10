from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect


def group_required(*groups):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return func(request, *args, **kwargs)
            raise PermissionDenied
        return wrap
    return decorator

