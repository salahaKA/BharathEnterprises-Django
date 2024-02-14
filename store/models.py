from django.urls import reverse
from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

# variation_category_choice= (
#     ('color','color'),
#     ('size','size')   
# )

# class variation(models.Model):
#     product= models.ForeignKey(Product, on_delete= models.CASCADE)
#     variation_category= models.CharField(MAX_LENGTH=100,CHOICES=variation_category_choice)
#     variation_value= models.CharField(max_length=100)
#     is_active      = models.BooleanField(default=True)
#     created_date= models.DateField(auto_now=True)

#     def __str__(self):
#         return self.product
    

    # def averageReview(self):
    #     reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
    #     avg = 0
    #     if reviews['average'] is not None:
    #         avg = float(reviews['average'])
    #     return avg

    # def countReview(self):
    #     reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
    #     count = 0
    #     if reviews['count'] is not None:
    #         count = int(reviews['count'])
    #     return count

