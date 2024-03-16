from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class PostConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "post"
    verbose_name = pgettext_lazy("app name", "Posts")

