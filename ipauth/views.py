import urlparse

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login as auth_login
from django.contrib.auth.views import login as base_login_view
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect



@csrf_protect
@never_cache
def login(request, redirect_field_name=REDIRECT_FIELD_NAME, **kwargs):
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    
    value = None
    
    if 'ipauth_meta_key' in kwargs:
        value = request.META.get(kwargs.pop('ipauth_meta_key'), None)
    
    if value is None and hasattr(settings,'IPAUTH_IP_META_KEY'):
        value = request.META.get(settings.IPAUTH_IP_META_KEY, None)
    
    if value is None:
        value = request.META['REMOTE_ADDR']
    
    user = authenticate(ip=value)
    
    if user is None:
        return base_login_view(request, redirect_field_name=redirect_field_name, 
                               **kwargs)
    
    auth_login(request, user)
    
    messages.add_message(request, messages.INFO,
                        'You are now logged in as %s' % (user.get_full_name(),))
    
    netloc = urlparse.urlparse(redirect_to)[1]
    
    # Use default setting if redirect_to is empty
    if not redirect_to:
        redirect_to = settings.LOGIN_REDIRECT_URL
    
    # Security check -- don't allow redirection to a different
    # host.
    elif netloc and netloc != request.get_host():
        redirect_to = settings.LOGIN_REDIRECT_URL
    
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    
    return HttpResponseRedirect(redirect_to)
