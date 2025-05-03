from django import forms
from .models import Test, Question, Choice, Answer, Result

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super(AnswerForm, self).__init__(*args, **kwargs)
        
        choices = question.choices.all()
        choice_list = [(choice.id, choice.text) for choice in choices]
        
        self.fields[f'question_{question.id}'] = forms.ChoiceField(
            choices=choice_list,
            widget=forms.RadioSelect(),
            required=True,
            label=question.text
        ) 