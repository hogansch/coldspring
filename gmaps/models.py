# myapp/models.py
from django.db import models
from wagtail.core.models import Page
from wagtailgmaps.edit_handlers import MapFieldPanel

class MapPage(Page):
    template = "map_page.html"
    # Wagtailgmaps expects a `CharField` (or any other field that renders as a text input)
    formatted_address = models.CharField(max_length=255)
    latlng_address = models.CharField(max_length=255, blank=True)

    # Use the `MapFieldPanel` just like you would use a `FieldPanel`
    content_panels = Page.content_panels + [
        MapFieldPanel('formatted_address'),
        MapFieldPanel('latlng_address', latlng=True),
    ]