###########################
Django error page templates
###########################

Simple and generic ``404.html`` and ``500.html`` templates for django. The
error messages are styled with the bootstrap hero-unit style.


Issues/contribute
=================

Report any issues at the `github project page <django_errortemplates>`_, and feel free
to add your own guides/experiences to the wiki, and to contribute changes using
pull requests.


Install
=======

::

    $ pip install django_errortemplates


Setup
=====

Add ``'errortemplates'`` and ``'django.contrib.staticfiles'`` to
``INSTALLED_APPS``.


Try it out
==========

Start your server with::

    python manage.py runserver --insecure

set ``DEBUG`` to ``False``, and navigate to a non-existing url or an url that
raises an exception. Note that we use ``--insecure`` to serve static files
event when ``DEBUG`` is ``False``.


.. _`django_errortemplates`: https://github.com/espenak/django_errortemplates
