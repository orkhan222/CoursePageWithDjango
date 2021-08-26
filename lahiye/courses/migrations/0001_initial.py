# Generated by Django 3.2.3 on 2021-08-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('yazili', models.CharField(max_length=127, null=True, verbose_name='Yazili')),
                ('text', models.CharField(max_length=127, null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('time', models.CharField(max_length=127, null=True, verbose_name='Time')),
                ('campus', models.CharField(max_length=127, null=True, verbose_name='Campus')),
                ('hafttime', models.CharField(max_length=127, null=True, verbose_name='Hafttime')),
                ('rc', models.CharField(max_length=127, null=True, verbose_name='Rc')),
            ],
            options={
                'verbose_name': 'Apply',
                'verbose_name_plural': 'Applys',
            },
        ),
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('span', models.CharField(max_length=127, null=True, verbose_name='Span')),
                ('name', models.CharField(max_length=127, null=True, verbose_name='Name')),
                ('programming', models.CharField(max_length=127, null=True, verbose_name='Prohramming')),
                ('image', models.ImageField(upload_to='basic_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Basic',
                'verbose_name_plural': 'Basics',
            },
        ),
        migrations.CreateModel(
            name='Fall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('text', models.CharField(max_length=127, null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Fall',
                'verbose_name_plural': 'Falls',
            },
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('span', models.CharField(max_length=127, null=True, verbose_name='Span')),
                ('name', models.CharField(max_length=127, null=True, verbose_name='Name')),
                ('image', models.ImageField(upload_to='featured_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Featured',
                'verbose_name_plural': 'Featureds',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, null=True, verbose_name='Name')),
                ('span', models.CharField(max_length=127, null=True, verbose_name='Span')),
                ('image', models.ImageField(upload_to='image_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to='basic_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Make',
                'verbose_name_plural': 'Makes',
            },
        ),
        migrations.CreateModel(
            name='Our',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('span', models.CharField(max_length=127, null=True, verbose_name='Span')),
                ('name', models.CharField(max_length=127, null=True, verbose_name='Name')),
                ('image', models.ImageField(upload_to='our_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Our',
                'verbose_name_plural': 'Ours',
            },
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('span', models.CharField(max_length=127, null=True, verbose_name='Span')),
                ('name', models.CharField(max_length=127, null=True, verbose_name='Name')),
                ('image', models.ImageField(upload_to='related_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Related',
                'verbose_name_plural': 'Relateds',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('yazili', models.CharField(max_length=127, null=True, verbose_name='Yazili')),
                ('image', models.ImageField(upload_to='slider_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('span', models.CharField(max_length=127, null=True, verbose_name='Span')),
                ('name', models.CharField(max_length=127, null=True, verbose_name='Name')),
                ('span2', models.CharField(max_length=127, null=True, verbose_name='Span2')),
                ('image', models.ImageField(upload_to='Store_image', verbose_name='Shekili')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, null=True, verbose_name='Title')),
                ('title2', models.CharField(max_length=127, null=True, verbose_name='Title2')),
                ('text', models.CharField(max_length=127, null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
