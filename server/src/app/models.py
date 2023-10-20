from django.db import models

# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. 
# Generally, each model maps to a single database table.

# Using ORM (Object Relational Mapping) to write python code to create database models, and then have those models automatically made for us in a structured db schema like SQLlite3
# Will use migrations (automated code that will create the corresponding model in a db like SQL/MongoDB)
# Anytime a change is made to a database model, we need to make a migration using <python manage.py makemigrations>to save changes and <python manage.py migrate> to apply them

# Create your models here.

class Prompt(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    sdlc_phase = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

# Each attribute of the Prompt model represents a database field.
# Each field is specified as a class attribute, and each attribute maps to a database column.

# For example, the Prompt model would create a databse like this:

# CREATE TABLE Prompt (
#     "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
#     "title" varchar(200) NOT NULL,
#     "sdlc_phase" varchar(30) NOT NULL
#     "role" varchar(30) NOT NULL
# );