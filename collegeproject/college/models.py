from django.db import models

# Create your models here.
class colleges(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    fees = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return self.name

class field(models.Model):
    college = models.ForeignKey(
        'colleges',
        on_delete=models.CASCADE,
    )
    field = models.CharField(max_length=200)
    marks =models.IntegerField()
    def __str__(self):
        return str(self.college)
