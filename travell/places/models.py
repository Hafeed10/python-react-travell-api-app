from django.db import models



class Place(models.Model):
    name = models.CharField(max_length=255,blank=True)
    featured_image = models.ImageField(upload_to="place/images/",blank=True)
    place_field = models.CharField(max_length=200,blank=True)  # Corrected field name
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="places",blank=True)  # Corrected ForeignKey reference
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False,blank=True)

    class Meta:
        db_table = "place"

    def __str__(self):
        return self.name

class Category(models.Model):
    image = models.ImageField(upload_to="category/images/")  # Corrected upload_to path
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name

class Gallery(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="gallery")  # Corrected ForeignKey reference
    image = models.ImageField(upload_to='gallery_images/')
    name = models.CharField(max_length=100,blank=True) 
    class Meta:
        db_table = "gallery"

    def __str__(self):
        return str(self.id)


