# Learnings throughout the course

## python manage.py migrate

This command doesn't actually execute/apply the migrations. This will scan through the listed apps
to see why one has listed migrations pending to be executed.

The creation of these files is actually achieved by **python manage.py makemigrations**

You may then run `python manage.py migrate`

## You may see the output bare SQL code if you scan it

This scanning can be achieved by running `python manage.py sqlmigrate [app_name] [number]_migration_file.py`.

## Q operator

Django ships with this operator that facilitates the AND OR operations when querying the database (using Django's ORM):

In [5]: from django.db.models import Q

In [6]: Patient.objects.filter(Q(last_name='serrano') & Q(age=27)).all()
Out[6]: <QuerySet [<Patient: hector serrano, is 27 years old>, <Patient: monica serrano, is 27 years old>, <Patient: monica serrano, is 27 years old>]>

As you can see, I'm able to retrieve these records if they meet both of the **criterias** here.

## Querysets and field lookups

Django's querysets can leverage something known as field lookups. I personally think of them as discriminators. Here's how the docs describe them:
<https://docs.djangoproject.com/en/4.2/ref/models/querysets/#id4>

examples:
In [7]: Patient.objects.filter(last_name__startswith='s').all()
Out[7]: <QuerySet [<Patient: hector serrano, is 27 years old>, <Patient: monica serrano, is 27 years old>, <Patient: monica serrano, is 27 years old>]>

### In this case none of the records I had stored in my local database (up until that moment) met the criteria

In [8]: Patient.objects.filter(last_name__in=[20, 30, 40]).all()
Out[8]: <QuerySet []>
