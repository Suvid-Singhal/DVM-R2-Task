from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Train, TrainStops, TrainSeats, UserJourneys, JourneyPassengers

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'name', 'email', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'wallet' ,)}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username','name','email', 'password1', 'password2', 'is_staff', 'is_superuser', 'wallet'),
        }),
    )
    list_display = ['username', 'email', 'name', 'is_staff', 'is_superuser', 'wallet']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Train)
admin.site.register(TrainStops)
admin.site.register(TrainSeats)
admin.site.register(UserJourneys)
admin.site.register(JourneyPassengers)