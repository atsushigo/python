from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from .models import MyUser, Profile
from .forms import UserCreationForm, UserChangeForm, GroupAdminForm


class ProfileInline(admin.StackedInline):
    model = Profile

# @admin.register(MyUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'person_incharge', 'id_num', 'date_of_birth', 'address', 'contact_no', 'mobile_no', 'fax_no', 'cert')
    # fields = ('name', 'person_incharge', 'id_num', 'date_of_birth', 'address', 'contact_no', 'mobile_no', 'fax_no', 'cert')
    fieldsets = (
        (None, {'fields': ('name', 'person_incharge', 'id_num', 'date_of_birth', 'address', 'contact_no', 'mobile_no', 'fax_no', 'cert')})
    )

class GroupInline(admin.StackedInline):
    model = Group

class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_admin', 'last_login')
    list_filter = ('is_admin', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_admin',
            'is_active',
            'is_superuser',
            )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        },
        ('Permissions', {'fields': ('is_admin','is_staff','groups',)})
        ),
    )
    search_fields = ('email','username', )
    ordering = ('email','username', )
    filter_horizontal = ()
    inlines = [ProfileInline, ]

class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm

# # Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

