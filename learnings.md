# Learnings throughout the course

## python manage.py migrate

This command doesn't actually execute/apply the migrations. This will scan through the listed apps
to see why one has listed migrations pending to be executed.

The creation of th4ese files is actually achieved by **python manage.py makemigrations**

You may then run `python manage.py migrate`

## You may see the output bare SQL code if you scan it

This scanning can be achieved by running `python manage.py sqlmigrate [app_name] [number]_migration_file.py`.
