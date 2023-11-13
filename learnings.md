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
