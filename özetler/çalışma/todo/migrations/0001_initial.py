# Generated by Django 4.1.1 on 2022-09-25 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task", models.CharField(max_length=50)),
                ("description", models.TextField()),
                (
                    "priority",
                    models.CharField(
                        choices=[("H", "High"), ("M", "Medium"), ("L", "Low")],
                        default="L",
                        max_length=18,
                    ),
                ),
                ("is_done", models.BooleanField()),
                ("createDate", models.DateTimeField(auto_now_add=True)),
                ("updateDate", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categorys",
                        to="todo.category",
                    ),
                ),
            ],
        ),
    ]
