from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from .models import MyUser, Profile

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    email = forms.EmailField(
        max_length=100,
        required=True,
    )
    username = forms.CharField(
        max_length=30, 
        required=True,
    )
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username', ) # 編輯個人資料頁面其他資料不修改就不列出來

class ProfileChangeForm(forms.ModelForm):
    """
    A form for updating user's profile
    """
    name = forms.CharField(
        max_length=30,
        required=False,
    )
    person_incharge = forms.CharField(
        max_length=30,
        required=False,
    )
    id_num = forms.CharField(
        max_length=30,
        required=False,
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    address = forms.CharField(
        max_length=50,
        required=False,
    )
    contact_no = forms.CharField(
        max_length=10,
        required=False,
    )
    mobile_no = forms.CharField(
        max_length=10,
        required=False,
    )
    fax_no = forms.CharField(
        max_length=10,
        required=False,
    )

    class Meta:
        model = Profile
        fields = [
            'name', 'person_incharge', 
            'id_num', 'date_of_birth', 'address', 
            'contact_no', 'mobile_no', 'fax_no',
        ]

class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []
        
    users = forms.ModelMultipleChoiceField(
        queryset=MyUser.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        instance = super(GroupAdminForm, self).save()
        self.save_m2m()
        return instance