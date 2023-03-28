from django.contrib import admin
from .models import MyModel


@admin.register(MyModel)
class Xadmin(admin.ModelAdmin):
    class Meta:
        model = MyModel
        fields = ["id", "name", "email", 'phone', "image"]
