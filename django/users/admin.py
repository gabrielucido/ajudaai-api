from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserForm(forms.ModelForm):
    """
    User Admin Form.
    """

    def clean_password(self):
        return make_password(self.cleaned_data['password'])

    class Meta:
        """
        Form Options.
        """
        model = get_user_model()
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserAdmin(admin.ModelAdmin):
    """
    User Admin.
    """
    form = UserForm


admin.site.register(get_user_model(), UserAdmin)
