# Generated by Django 3.0.8 on 2020-07-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dsuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='아이디')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')),
            ],
            options={
                'verbose_name': '회원',
                'verbose_name_plural': '회원목록',
                'db_table': 'member',
            },
        ),
    ]
