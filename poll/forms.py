from .models import Question,CheckBox
from django import forms

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['ques_text']

class QuestionCreateForm(forms.Form):
    ques_text=forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':"form-control form-control-lg",
            'type':"text",
            'placeholder':"Your Question",
        }))

    choice1_bool=forms.BooleanField(required=False)
    choice1_text=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':"form-control form-control-sm",
            'type':"text",
            'placeholder':"Option 1"
    }))

    choice2_bool=forms.BooleanField(required=False)
    choice2_text=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':"form-control form-control-sm",
            'type':"text",
            'placeholder':"Option 2"
    }))

    choice3_bool=forms.BooleanField(required=False)
    choice3_text=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':"form-control form-control-sm",
            'type':"text",
            'placeholder':"Option 3"
    }))

    choice4_bool=forms.BooleanField(required=False)
    choice4_text=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':"form-control form-control-sm",
            'type':"text",
            'placeholder':"Option 4"
    }))


        


class CheckBoxForm(forms.ModelForm):
    class Meta:
        model=CheckBox
        fields=['text_val','bool_val']