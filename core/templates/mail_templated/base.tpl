<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block subject %}Default Subject{% endblock %}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .email-container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .email-content {
            font-size: 16px;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <div class="email-content">
            {% block html %}
            <p>This is a placeholder for email content.</p>
            {% endblock %}
        </div>
    </div>
</body>
</html>
