from django import forms
from .models import Article


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","category","image"]

        widgets = {
            'title':forms.TextInput(attrs = {
                'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-400 focus:outline-none','placeholder':'Enter Title'
            }),
            'content':forms.Textarea(attrs = {
                'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-400 focus:outline-none','placeholder':'Enter Content','rows':7
            }),
            'category':forms.Select(attrs = {
                'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-400 focus:outline-none'
            }),      
            'image':forms.ClearableFileInput(attrs = {
                'class':'w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-indigo-50 file:text-indigo-600 hover:file:bg-indigo-100'
            })              
        }