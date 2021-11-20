from django import forms


class FirstForm(forms.Form):
    test_name = forms.TimeField(label='Here', help_text='this is help text')
    test_number = forms.IntegerField()
    test_many = forms.MultipleChoiceField(choices=[
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
])
