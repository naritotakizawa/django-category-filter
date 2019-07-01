from django import forms
from .models import Post, ParentCategory


class PostCreateForm(forms.ModelForm):
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。
    parent_category = forms.ModelChoiceField(
        label='親カテゴリ',
        queryset=ParentCategory.objects,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    field_order = ('title', 'parent_category', 'category')
