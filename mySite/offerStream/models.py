from django.db import models

class Adress(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=10)

    def __str__(self):
        return "%s, %s %s" % (self.street, self.zipCode, self.city)

class Store(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Offer(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    detail = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
