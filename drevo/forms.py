from django import forms
from .models import Znanie, Author, AuthorType
from ckeditor.widgets import CKEditorWidget


class ZnanieForm(forms.ModelForm):
    """
    Форма для вывода сущности Знания.
    """
    name = forms.CharField(widget=forms.Textarea(attrs={'cols': 40,
                                                        'rows': 3,
                                                        }
                                                 ),
                           label='Тема'
                           )
    content = forms.CharField(widget=CKEditorWidget(attrs={'cols': 40,
                                                           'rows': 10,
                                                           }
                                                    ),
                              label='Содержание',
                              required=False
                              )

    class Meta:
        model = Znanie
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    """
    Форма для вывода сущности Author.
    """
    info = forms.CharField(widget=CKEditorWidget(attrs={'cols': 40,
                                                        'rows': 10,
                                                        }
                                                 ),
                           label='Сведения об авторе',
                           required=False
                           )

    class Meta:
        model = Author
        fields = '__all__'


class GlossaryTermForm(forms.ModelForm):
    """
    Форма для вывода терминов глоссария.
    """
    description = forms.CharField(widget=CKEditorWidget(attrs={'cols': 40,
                                                           'rows': 10,
                                                           }
                                                    ),
                              label='Описание',
                              required=False
                              )

    class Meta:
        model = Znanie
        fields = '__all__'


class AuthorsFilterForm(forms.Form):
    """
    Форма для фильтрации списка авторов по типу авторов (AuthorType).

    В поле author_type добавляем атрибут oninput для поля формы Select. Это
    необходимо для вызова JS функции в шаблоне, которая при вводе данных
    в форму, т.е. по настплении события oninput, отправляет её на сервер.
    Т.о. форма не требует кнопки типа "Отправить".
    """
    author_type = forms.ModelChoiceField(queryset=AuthorType.objects.all(),
                                   empty_label='Все',
                                   widget=forms.Select(attrs={'oninput': 'doSubmit(this.form.id)'
                                                              })                                   
                                   )    