from django.db import models

# Create your models here.
class Likes(models.Model):
   
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = "likes"

    def __str__(self):
        return str(self.id)    