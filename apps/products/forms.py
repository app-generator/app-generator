from apps.common.models_products import Products
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

        widgets = {
            'thumbnail': forms.FileInput(
                attrs={
                    'style': "opacity: 0; position: absolute; width: 100%; height: 100%; top: 0; left: 0; cursor: pointer; pointer-events: none;",
                    'accept': 'image/png, image/gif, image/jpeg',
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        remove_slug = kwargs.pop('remove_slug', False)
        super(ProductForm, self).__init__(*args, **kwargs)

        if remove_slug:
            self.fields.pop('slug', None)

        # Move 'free' field to the end
        free_field = self.fields.pop('free')
        self.fields['free'] = free_field

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            self.fields['free'].widget.attrs['class'] = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'
