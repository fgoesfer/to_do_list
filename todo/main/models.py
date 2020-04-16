from django.db import models

class Todo(models.Model):
    added_date = models.DateTimeField()
    complete = models.BooleanField(default=False)
    text = models.CharField(max_length=200)

