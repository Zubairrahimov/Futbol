

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StadiumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),

                ('address', models.TextField(default='')),

                ('contact', models.CharField(default='', max_length=13)),
                ('images', models.ImageField(blank=True, upload_to='Images/')),
            ],
            options={


                'db_table': 'Stadium',

            },
        ),
        migrations.CreateModel(
            name='BronModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(default=datetime.datetime.now)),

                ('price', models.IntegerField(default=0)),
                ('bron_status', models.BooleanField(default=False, null=True)),
                ('stadium', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bron.stadiummodel')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={

                'db_table': 'Bron',

            },
        ),
    ]
