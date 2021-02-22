from django.db import models


class Student(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    classroom = models.CharField("Classroom", max_length=20)

    def __str__(self):
        return self.first_name
