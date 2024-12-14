from django import forms
from apps.common.models import Ticket, TypeChoices, Comment, StateChoices
from django_quill.forms import QuillFormField


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('user', 'states', 'custom_development', )
    
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
        
    def clean(self):
        cleaned_data = super().clean()
        ticket_type = cleaned_data.get('type')
        product = cleaned_data.get('product')
        platform = cleaned_data.get('platform')
        repo_url = cleaned_data.get('repo_url')

        if ticket_type == TypeChoices.PRODUCT_ASSISTANCE and not product:
            self.add_error('product', 'Product is required.')
        
        if ticket_type == TypeChoices.PLATFORM and not platform:
            self.add_error('platform', 'Platform is required.')
        
        if ticket_type == TypeChoices.GENERATED_APP and not repo_url:
            self.add_error('repo_url', 'Repository URL is required.')

        return cleaned_data


class CommentForm(forms.ModelForm):
    state = forms.ChoiceField(choices=StateChoices.choices, required=False)
    class Meta:
        model = Comment
        exclude = ('user', 'ticket', )


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

        if not user or not user.is_superuser:
            self.fields.pop('state')
            
        self.order_fields(['state', 'comment'])

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            self.fields[field_name].widget.attrs['class'] = 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
        

class SupportForm(forms.Form):
    description = QuillFormField()