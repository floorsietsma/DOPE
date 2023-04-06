from django.db import models

# class OptimisationRequest(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['created']s

class Machine(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    costPerMinute = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

