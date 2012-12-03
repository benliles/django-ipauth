from logging import getLogger

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from ipauth.models import Range, IP



log = getLogger('ipauth.backend')

class RangeBackend(ModelBackend):
    supports_anonymous_user = False

    def authenticate(self, ip=None):
        try:
            ip = IP(ip)
            current = Range.objects.get(Q(lower=ip) | Q(lower__lte=ip, upper__gte=ip))
            log.info('Authenticating %s from %s' % (unicode(current.user), unicode(ip),))
            return current.user
        except Range.DoesNotExist:
            log.error('Authentication failed for %s' % (unicode(ip),))
            pass
        return None
