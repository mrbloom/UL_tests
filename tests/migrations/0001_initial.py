# Generated by Django 2.1 on 2018-08-27 13:09

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('alt_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('question_text', models.TextField()),
                ('question_answer', models.TextField()),
                ('image', models.ManyToManyField(to='tests.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tests.CommonInfo')),
                ('avg_mark', models.PositiveSmallIntegerField()),
            ],
            bases=('tests.commoninfo',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tests.CommonInfo')),
                ('subject', models.CharField(max_length=50)),
            ],
            bases=('tests.commoninfo',),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Quiz'),
        ),
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.ManyToManyField(to='tests.Image'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Question'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tests.Teacher'),
        ),
    ]
