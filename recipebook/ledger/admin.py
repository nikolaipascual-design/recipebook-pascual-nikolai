from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, RecipeImage
from .views import LoginView


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInline,]


class CustomView(LoginRequiredMixin, LoginView):
    template_name = "recipe_detail"
    redirect_field_name = '/accounts/login'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)