from django.forms import Form, CharField, ChoiceField


class SearchForm(Form):
    keywords = CharField(required=False)
    tools = CharField(required=False)
    max_time = CharField(required=False)
    dietary_restrictions = CharField(required=False)
    max_cost_per_serving = CharField(required=False)
    sort_by = ChoiceField(choices=(('rating','Rating'),('cost','Cost per Serving'),('time','Time')), required=False)
