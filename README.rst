Introduction
------------

IP based authentication for Django. IP ranges are specified and tied to a user 
account.

Installation
------------

* Install the ``django_ipauth`` package into your path either using ``buildout``,
  ``easy_install`` or ``pip``.
* Make the following changes to your ``settings.py``
  * Add `'ipauth.backend.RangeBackend'` to your ``AUTHENTICATION_BACKENDS``
  * Add ``ipauth`` to your ``INSTALLED_APPS``
  * If it isn't already, add ``django.contrib.auth`` to your ``INSTALLED_APPS``
* Change your login url to use the ``ipauth.views.login`` view.
* Run ``manage.py syncdb``

Using
-----

If you are using the ``contrib.admin`` package from Django, you should have a 
new section in your admin site called ``Ipauth`` where you can add ``Ranges``.
