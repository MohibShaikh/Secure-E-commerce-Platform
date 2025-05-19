from functools import wraps
from django_ratelimit.decorators import ratelimit
from django_ratelimit.exceptions import Ratelimited
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

def rate_limit(group='default', key='ip', method=['POST', 'PUT', 'DELETE']):
    """
    Rate limit decorator that can be applied to views.
    
    Args:
        group (str): Rate limit group from settings
        key (str): Rate limit key ('ip', 'user', or 'user_or_ip')
        method (list): HTTP methods to rate limit
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            @ratelimit(
                group=group,
                key=key,
                method=method,
                rate=settings.RATELIMIT_GROUPS[group],
                block=True
            )
            def _wrapped_view(request, *args, **kwargs):
                return view_func(request, *args, **kwargs)
            
            try:
                return _wrapped_view(request, *args, **kwargs)
            except Ratelimited:
                return Response(
                    {
                        'error': 'Too many requests',
                        'detail': f'Rate limit exceeded. Please try again later.'
                    },
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )
        return wrapped_view
    return decorator 