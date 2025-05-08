

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
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
                (
                    "author",
                    models.CharField(
                        max_length=150,
                        unique=True,
                        verbose_name="имя (псевдоним) автора",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="загрузите изображение автора",
                        null=True,
                        upload_to="authors/media",
                        verbose_name="изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="Books",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название книги"
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("adventures", "приключения"),
                            ("fantasy", "фантастика"),
                            ("story", "рассказ"),
                            ("novel", "повесть"),
                            ("poetry", "поэзия"),
                        ],
                        default="story",
                        max_length=20,
                        verbose_name="жанр",
                    ),
                ),
                (
                    "annotation",
                    models.TextField(blank=True, null=True, verbose_name="аннотация"),
                ),
                (
                    "barcode",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="штрихкод"
                    ),
                ),
                (
                    "quantity_all",
                    models.PositiveIntegerField(
                        default=0, verbose_name="всего в библиотеке"
                    ),
                ),
                (
                    "quantity_lending",
                    models.PositiveIntegerField(default=0, verbose_name="выдано всего"),
                ),
                (
                    "amount_lending",
                    models.PositiveIntegerField(
                        default=0, verbose_name="количество выдачи"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="загрузите обложку",
                        null=True,
                        upload_to="books/media",
                        verbose_name="обложка",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="book_author",
                        to="library.authors",
                        verbose_name="автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="Lending",
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
                (
                    "operation",
                    models.CharField(
                        choices=[
                            ("inventory", "инвентаризация"),
                            ("arrival", "поступление"),
                            ("issuance", "выдача"),
                            ("return", "возврат"),
                            ("loss", "утеря"),
                            ("write_off", "списание"),
                        ],
                        default="issuance",
                        max_length=20,
                        verbose_name="операция",
                    ),
                ),
                (
                    "date_event",
                    models.DateField(default=datetime.date.today, verbose_name="дата"),
                ),
                (
                    "id_return",
                    models.IntegerField(
                        default=0, verbose_name="id возврата или утери"
                    ),
                ),
                (
                    "is_return",
                    models.BooleanField(
                        default=False, verbose_name="пометка о возврате"
                    ),
                ),
                (
                    "is_loss",
                    models.BooleanField(default=False, verbose_name="пометка об утере"),
                ),
                (
                    "is_write_off",
                    models.BooleanField(
                        default=False, verbose_name="пометка о списании"
                    ),
                ),
                (
                    "arrival_quantity",
                    models.IntegerField(
                        default=0, verbose_name="Количество поступивших книг."
                    ),
                ),
                (
                    "issued_quantity",
                    models.IntegerField(default=0, verbose_name="выдано читателям"),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="lending_book",
                        to="library.books",
                        verbose_name="книга",
                    ),
                ),
            ],
            options={
                "verbose_name": "выдача",
                "verbose_name_plural": "выдачи",
            },
        ),
    ]
