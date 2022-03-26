from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'id': 'file_id'
    }),
    allow_empty_file=True, # for test files
    )

class SearchForm(forms.Form):
    file = forms.TextInput()
