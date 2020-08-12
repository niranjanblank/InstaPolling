from django import forms
from .models import Question,Option
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']

        widgets = {
            'question': forms.TextInput(attrs={'class':'form-control','placeholder':'What is your question?'})
        }

class OptionFormModel(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_title']

        widgets = {
            'option_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your option?'})
        }

    def __init__(self, *args, **kwargs):
        super(OptionFormModel, self).__init__(*args, **kwargs)
        self.fields['option_title'].label = "Option"
