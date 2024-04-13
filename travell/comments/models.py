from django.db import models
  # Adjust the import path based on your project structure

class Comment(models.Model):
    place = models.ForeignKey("comment", on_delete=models.CASCADE, related_name="comment",blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.id)




