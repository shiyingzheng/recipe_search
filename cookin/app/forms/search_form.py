from django.forms import Form, CharField


class SearchForm(Form):
    keywords = CharField(required=False)
    tools = CharField(required=False)
    max_time = CharField(required=False)
    dietary_restrictions = CharField(required=False)
    max_cost_per_serving = CharField(required=False)
