from django.db import models

# Create your models here.
class reply_comments(models.Model):
    
    Comment = models.CharField(max_length=255)
    Reply_comment = models.CharField(max_length=255)


    class Meta:
        db_table = 'reply_comments'


    def __str__(self):
        return self.Comment    