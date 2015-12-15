from django.forms import Form, CharField


class SearchForm(Form):
    keywords = CharField(required=False)
    tools = CharField(required=False)
    time = CharField(required=False)
    dietary_restrictions = CharField(required=False)
    max_cost = CharField(required=False)
