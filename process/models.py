from django.db import models

# Create your models here.
#class Item(models.Model):
#    name = models.CharField(max_length = 30, blank = False)
#    done = models.BooleanField(blank = False, default = False)
#    
#    def __str__(self):
#       return self.name
        

class Antq(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    price = models.CharField(max_length = 5, blank = False)
    manufacture = models.CharField(max_length = 4, blank = False)
    description = models.CharField(max_length = 500, blank = False)
    height = models.CharField(max_length = 4, blank = False)
    width = models.CharField(max_length = 4, blank = False)
    depth = models.CharField(max_length = 4, blank = False)
    
    def __str__(self):
        return self.name
    