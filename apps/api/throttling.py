from rest_framework.throttling import SimpleRateThrottle

class OncePerMinuteThrottle(SimpleRateThrottle):
    scope = 'once_per_minute'

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': self.scope,
            'ident': request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')
        }

    def allow_request(self, request, view):
        return super().allow_request(request, view)
