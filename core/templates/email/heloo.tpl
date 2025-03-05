{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
<p>Here is your token:</p>
<strong>{{ token }}</strong>
{% endblock %}
