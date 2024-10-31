from apps.common.models_products import Products, Props
from django import forms
import uuid

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'release_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        remove_slug = kwargs.pop('remove_slug', False)
        super(ProductForm, self).__init__(*args, **kwargs)

        if remove_slug:
            self.fields.pop('slug', None)
        
        if not self.instance.code:
            self.fields['code'].initial = str(uuid.uuid4())

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            self.fields['free'].widget.attrs['class'] = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'
            self.fields['code'].widget.attrs['readonly'] = True
            self.fields['downloads'].widget.attrs['readonly'] = True



class PropsForm(forms.ModelForm):
    class Meta:
        model = Props
        exclude = ('product', 'created_at', 'updated_at', )

    def __init__(self, *args, **kwargs):
        super(PropsForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            self.fields['state'].widget.attrs['class'] = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'