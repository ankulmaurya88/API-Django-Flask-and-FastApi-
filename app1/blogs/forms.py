# from django import forms
# from .models import Blog

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['title', 'content']
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'w-full p-2 border rounded focus:ring focus:ring-blue-300'
#             }),
#             'content': forms.Textarea(attrs={
#                 'class': 'w-full p-2 border rounded focus:ring focus:ring-blue-300',
#                 'rows': 5
#             }),
#         }


from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded focus:ring focus:ring-blue-300'
            }),
            'content': forms.Textarea(attrs={
                'id': 'editor',   # important
                'class': 'w-full p-2 border rounded'
            }),
        }
