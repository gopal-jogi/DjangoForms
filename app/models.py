from django.db import models

# Create your models here.
class Topic(models.Model):
    TName=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.TName
    

    
class WebPage(models.Model):
    TName=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    URL=models.URLField()
    Email=models.EmailField()

    def __str__(self) -> str:
        return self.Name

class AccessRecord(models.Model):
    Name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Author
