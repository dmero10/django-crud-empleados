from django.db import models

# Create your models here.

# Position model (Cargo)
class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


# Employee model (Empleado)
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.position.name
