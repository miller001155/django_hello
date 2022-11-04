from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента', widget=forms.TextInput(attrs={'class': 'myfield'}), min_length=3)
    # подсказки для ввода
    age = forms.IntegerField(label='Возраст клиента', widget=forms.NumberInput(attrs={'class': 'myfield'}),
                             min_value=1, max_value=100)  # изменение поля
    # required_css_class = "field"
    # error_css_class = 'error'
    # weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    # email = forms.EmailField(label='Электронный адрес', help_text='Обязательный символ -@')
    # reklama = forms.BooleanField(label='Согласны получать рекламу?', required=False)
    # vyb = forms.NullBooleanField(label='На море летим ?')
    # basket = forms.BooleanField(label='Поставьте галочку')
    # ip_adres = forms.GenericIPAddressField(label='IP адрес', help_text='Пример формата 192.0.2.0')
    # reg_text = forms.RegexField(label='Текст', regex='^[0-9][A-F][0-9]$')
    # slug_text = forms.SlugField(label='Введите текст')
    # url_text = forms.URLField(label='Введите URL', help_text='Например http://www.google.com')
    # # file_path = forms.FilePathField(label='Выберите файл', path='lib/home/slach') выбор файла из корня системы ноута
    # file = forms.FileField(label='Файлы')  # вставка файла из ноута
    # # file = forms.ImageField(label='Изображения')
    # date = forms.DateField(label='выберите дату')
    # time = forms.DateField(label='Введите время')
    # date_time = forms.DateTimeField(label='введите дату и время')
    # time_delta = forms.DurationField(label='Введите промежуток времени')
    # num = forms.IntegerField(label='Введите целое число')
    # num_1 = forms.DecimalField(label='Введите десятичное число')
    # ling = forms.ChoiceField(label='Выберите', choices=((1, 'a'), (2, 'b'), (3, 'c')))
