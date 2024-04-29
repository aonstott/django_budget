from django.db import models

# Create your models here.

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    note = models.TextField()

    def __str__(self):
        return "Transaction: " + self.name + " - " + str(self.amount) + " - " + str(self.date) + " - " + self.category + " - " + self.note
    
