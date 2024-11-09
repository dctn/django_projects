from django import forms
from .models import Todo_model
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_model
        fields = "__all__"