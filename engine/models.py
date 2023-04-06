from django.db import models

class Factory(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['name']


class MachineModel(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['name']


class Machine(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    buildDate = models.DateField()
    machineModel = models.ForeignKey(MachineModel, on_delete=models.CASCADE)
    costPerMinute = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['machineModel', 'buildDate']

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

class ProductionLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lineSteps = models.ManytoManyField(MachineModel, through='LineStepInfo')

class LineStepInfo(models.Model):
    machineModel = models.ForeignKey(MachineModel)
    line = models.ForeignKey(ProductionLine)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = (('line', 'order'),)
        ordering = ['line', 'order']

