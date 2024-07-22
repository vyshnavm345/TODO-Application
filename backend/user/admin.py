# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import MyUser
# from task.models import Task

# class MyUserAdmin(BaseUserAdmin):
#     list_display = ('email', 'name', 'is_admin')
#     search_fields = ('email', 'name')
#     readonly_fields = ('id',)

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = (
#         (None, {'fields': ('email', 'name', 'password', 'is_active', 'is_admin', 'is_staff')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password1', 'password2'),
#         }),
#     )

#     ordering = ('email',)
#     filter_horizontal = ()

# admin.site.register(MyUser, MyUserAdmin)
# admin.site.register(Task)















from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.

admin.site.register(User)