from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from ipauth.models import Range



class RangeBackend(ModelBackend):
    supports_anonymous_user = False
    
    def authenticate(self, ip=None):
        try:
            print ip
            current = Range.objects.get(Q(lower=ip) | Q(lower__lte=ip, upper__gte=ip))
            return current.user
        except Range.DoesNotExist:
            pass
        return None