from django import forms


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    description = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data['title']
        if "python" in title.lower():
            raise forms.ValidationError("title must not contain python")
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if title and description and title.lower() == description.lower():
            raise forms.ValidationError("Title and Description must be different")
        return cleaned_data

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 5:
            raise forms.ValidationError("Very short description")
        return description