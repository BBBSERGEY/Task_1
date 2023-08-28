from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput
from app_online_shop.models import OnlineShop

class OnlineShopForm(ModelForm):
    class Meta:
        model = OnlineShop
        fields = ('title', 'description', 'price', 'auction', 'image')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

form = OnlineShopForm()










# title = ModelForm.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
# description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
# price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
# auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
# image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))







