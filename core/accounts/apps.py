from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        # اینجا می‌تونی کد اضافی بذاری، ولی فعلاً نیازی نیست
        pass
