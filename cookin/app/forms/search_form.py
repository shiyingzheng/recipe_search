from django.forms import Form, CharField


class SearchForm(Form):
    keywords = CharField(required=False)
    tools = CharField(required=False)
