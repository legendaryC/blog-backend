from django.db import models



class Block(models.Model):
    tag = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)


    def __str__(self):
        return self.tag

class Article(models.Model):
    time = models.DateTimeField()
    title = models.CharField(max_length=100)
    intro=models.CharField(max_length=400)
    img=models.CharField(max_length=100,null=True)
    imgInf=models.CharField(max_length=100)
    blocks=models.ManyToManyField(Block)


    def __str__(self):
        return self.title

