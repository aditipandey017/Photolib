from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"