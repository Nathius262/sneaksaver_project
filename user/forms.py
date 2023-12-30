from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser
from user.models import Profile


class AccountSettingsForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60, required=False)
    last_name = forms.CharField(max_length=60, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'image',)
        widgets = {
            #'image': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'readURL(this)', 'id':'id_image_file', 'hidden':'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-3', 'id':'floatingInput', 'placeholder':"name@example.com"}),
            'username': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingUsername', 'placeholder':"username"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"Last Name"}),
        }

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
            except CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
            except CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use.' % account.username)
        
    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        # Check if an image is provided for updating
        if image:
            # You can add additional checks or processing here if needed
            return image
        else:
            pass
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name
        
    
    def save(self, commit=True):
        user = super(AccountSettingsForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()

        profile = user.user_profile  # Assuming a one-to-one relationship between CustomUser and profile
        profile.image = self.cleaned_data['image']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']

        if commit:
            profile.save()
            
        return user
