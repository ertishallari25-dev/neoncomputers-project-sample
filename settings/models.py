from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Computers', 'Computers'),
        ('Laptops', 'Laptops'),
        ('Gaming', 'Gaming'),
        ('Accessories', 'Accessories'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(default="https://picsum.photos/200")
    description = models.TextField(default="....")
    specs = models.TextField(blank=True, null=True, help_text="List specifications here")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.ImageField(upload_to='contact_attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Order(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Payment Details
    payment_method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=200)
    card_expiry = models.CharField(max_length=10)
    card_cvv = models.CharField(max_length=10)

    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product_name} - {self.purchased_at}"
    