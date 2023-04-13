from django.db import models


class Factory(models.Model):
    user = models.ForeignKey('auth.User', related_name='factories', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ['name']


class Machine(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    buildDate = models.DateField()
    costPerMinute = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'buildDate']


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    materialCost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class LineStep(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    leadTimeSeconds = models.PositiveIntegerField() # in seconds

    class Meta:
        unique_together = (('product', 'number'),)
        ordering = ['product', 'number']


class Order(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
