from django.db import models
from django.urls import reverse

# Create your models here.
AMOUNT = (
    ('O', 'Once'),
    ('T', 'Twice'),
    ('M', 'Multiple times'),
)

class Purpose(models.Model):
    purpose = models.CharField(max_length=50)

    def __str__(self):
        return self.purpose

    def get_absolute_url(self):
        return reverse("purposes_detail", kwargs={"pk": self.id})

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    purposes = models.ManyToManyField(Purpose)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"sneaker_id": self.id})

class Release(models.Model):
    date = models.DateField('release date')
    amount = models.CharField(
        max_length=1,
        choices=AMOUNT,
        default=AMOUNT[0][0]
        )
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Released {self.get_amount_display()} by {self.date}"

    class Meta:
        ordering = ['-date']