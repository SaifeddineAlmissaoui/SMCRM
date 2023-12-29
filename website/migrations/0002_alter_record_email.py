

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]
