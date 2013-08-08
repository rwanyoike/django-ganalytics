=================
Django GAnalytics
=================

This project is a simple integration of the Google Analytics tracking code for
quick implementation in Django projects.

Requirements
============

- Python 2.5+
- Django 1.4+

Installation
============

#. Add the ``ganalytics`` directory to your Python path. Using ``pip``::

       pip install "git+https://bitbucket.org/raymondwanyoike/django-ganalytics.git#egg=django-ganalytics"

#. Add ``ganalytics`` to your ``INSTALLED_APPS`` setting::

       INSTALLED_APPS = (
           ...
           'ganalytics',
       )

Configuration
=============

#. The ``ganalytics_load`` template tag requires a ``tracking_id`` and
   ``site_domain``. You must either pass them as arguments or set
   ``GOOGLE_ANALYTICS_PROPERTY_ID`` and ``GOOGLE_ANALYTICS_SITE_DOMAIN`` in
   your settings. Setting this value means that you can omit the
   ``tracking_id`` and ``site_domain`` arguments when invoking the template
   tag.

Basic Usage
===========

#. Load the tag library::

       {% load ganalytics %}

#. Load the js tracking code::

      {% ganalytics_load tracking_id=XXXXXXXXX site_domain=XXXXXXXXX %}

   or with ``GOOGLE_ANALYTICS_PROPERTY_ID`` and
   ``GOOGLE_ANALYTICS_SITE_DOMAIN`` defined in settings.py::

      {% ganalytics_load %}

Example
=======

::

    {% load ganalytics %}

    <html>
      <head>
        <title>Full Example</title>
        {% ganalytics_load %}
      </head>
      <body>
        ...
      </body>
    </html>

Note
====

``django-ganalytics`` uses the
`Universal Analytics <https://support.google.com/analytics/answer/2790010>`_
tracking method (not the Classic Analytics) for the code.
