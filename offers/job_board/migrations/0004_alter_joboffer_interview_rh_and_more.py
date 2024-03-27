# Generated by Django 5.0.3 on 2024-03-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job_board", "0003_joboffer_comment_joboffer_interview_rh_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joboffer",
            name="interview_rh",
            field=models.CharField(
                choices=[("green", "Vert"), ("red", "Rouge"), ("gray", "Gris")],
                default="grey",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="joboffer",
            name="interview_technical",
            field=models.CharField(
                choices=[("green", "Vert"), ("red", "Rouge"), ("gray", "Gris")],
                default="grey",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="joboffer",
            name="status",
            field=models.CharField(
                choices=[("green", "Vert"), ("red", "Rouge"), ("gray", "Gris")],
                default="grey",
                max_length=10,
            ),
        ),
    ]
