from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CHOICES =(
    ("Fantasy", "Fantasy"),
    ("Literary", "Literary"),
    ("Mystery", "Mystery"),
    ("Non-Fiction", "Non-Fiction"),
    ("Science Fiction", "Science Fiction"),
    ("Thriller", "Thriller"),
)

class ebook(models.Model):
    Title = models.TextField(max_length=250)
    Author = models.TextField(max_length=250)
    Genre = models.CharField(choices = CHOICES, max_length=50 )
    Review = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    Favorite = models.BooleanField()
