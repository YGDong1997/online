# Generated by Django 2.0.5 on 2018-05-30 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180529_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='course_org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organizationinfo', verbose_name='所属机构'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='讲师'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='lession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Courseinfo', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='lession',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Courseinfo', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='video',
            name='lession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Lession', verbose_name='章节'),
        ),
    ]