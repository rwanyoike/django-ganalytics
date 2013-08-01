from django import template


register = template.Library()


@register.inclusion_tag('ganalytics/analytics_js.html')
def ganalytics_load(tracking_id=None, site_domain=None):
    from django.conf import settings
    from django.template import TemplateSyntaxError

    if tracking_id is None:
        tracking_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', None)

    if site_domain is None:
        site_domain = getattr(settings, 'GOOGLE_ANALYTICS_SITE_DOMAIN', None)

    if tracking_id is None or site_domain is None:
        raise TemplateSyntaxError(
            'The `ganalytics_load` template tag requires a `tracking_id` and `site_domain`. You must either pass them as arguments or set GOOGLE_ANALYTICS_PROPERTY_ID and GOOGLE_ANALYTICS_SITE_DOMAIN in your settings.')

    return {
        'site_domain': site_domain,
        'tracking_id': tracking_id,
    }
