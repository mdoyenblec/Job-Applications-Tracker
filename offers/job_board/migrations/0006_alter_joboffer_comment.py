# Generated by Django 5.0.3 on 2024-03-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_board", "0005_alter_joboffer_interview_rh_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joboffer",
            name="comment",
            field=models.TextField(max_length=200),
        ),
    ]