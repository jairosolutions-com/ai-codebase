# Generated by Django 5.0.4 on 2024-05-07 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_codeexplainer_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeexplainer',
            name='_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='code_explainer', to='api.category'),
        ),
    ]
