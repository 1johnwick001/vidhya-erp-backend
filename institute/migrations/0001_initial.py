# Generated by Django 5.0.6 on 2024-06-10 09:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('registration_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('institute_name', models.CharField(max_length=250)),
                ('branch_name', models.CharField(blank=True, max_length=250)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('billing_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='PIN must be 6 digits.', regex='^\\d{6}$')])),
                ('mobile_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Mobile number must be 10 to 12 digits.', regex='^\\d{10,12}$')])),
                ('mobile_number2', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Mobile number must be 10 to 12 digits.', regex='^\\d{10,12}$')])),
                ('fax_number', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('principal_name', models.CharField(blank=True, max_length=100)),
                ('acc_start_year', models.CharField(max_length=100)),
                ('session_start_month', models.CharField(max_length=15)),
                ('accredited_by', models.CharField(max_length=20)),
                ('scholar_prefix', models.CharField(blank=True, max_length=50)),
                ('scholar_suffix', models.CharField(blank=True, max_length=50)),
                ('emp_no_prefix', models.CharField(blank=True, max_length=100)),
                ('no_of_pg_in_tcbook', models.CharField(blank=True, max_length=255)),
                ('auto_enroll_no', models.BooleanField(default=False)),
                ('std_attd_assignment', models.BooleanField(default=False)),
                ('live_class_show_time', models.BooleanField(default=False)),
                ('allow_edit_emp_attd_time', models.BooleanField(default=False)),
                ('show_std_contact_no_app', models.BooleanField(default=False)),
                ('auto_admi_number', models.BooleanField(default=False)),
                ('live_class_log_Std', models.BooleanField(default=False)),
                ('suggest_auto_section', models.BooleanField(default=False)),
                ('send_Std_wc_msg', models.BooleanField(default=False)),
                ('auto_scholar_no', models.BooleanField(default=False)),
                ('change_zoom_url', models.BooleanField(default=False)),
                ('single_login', models.BooleanField(default=False)),
                ('suggest_auto_house', models.BooleanField(default=False)),
                ('allow_ss_in_app', models.BooleanField(default=True)),
                ('auto_emp_no', models.BooleanField(default=False)),
                ('std_attd_through_live_class', models.BooleanField(default=False)),
                ('login_with_single_device', models.BooleanField(default=False)),
                ('show_yt_opt_4_app', models.BooleanField(default=False)),
                ('show_teach_mo_no_app', models.BooleanField(default=False)),
                ('show_exam_list_res_wise', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Institute',
                'verbose_name_plural': 'Institutes',
            },
        ),
    ]
