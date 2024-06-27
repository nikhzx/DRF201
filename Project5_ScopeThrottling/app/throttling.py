from rest_framework.throttling import ScopedRateThrottle

class studentThrottle(ScopedRateThrottle):
    scope = 'student'

class retrieveThrottle(ScopedRateThrottle):
    scope = 'one'