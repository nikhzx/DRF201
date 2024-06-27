from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class StudentRateThrottle(UserRateThrottle):
    scope = 'student'