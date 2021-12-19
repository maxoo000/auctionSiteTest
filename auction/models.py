from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

auction_status_choices = [("P", "Preparation"),
                          ("A", "Active"),
                          ("F", "Finished")]


# Create your models here.

class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="users_auction")
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    auction_slug = models.SlugField(unique=True, blank=False)

    auction_created_date = models.DateTimeField(default=timezone.now, blank=False, null=False)

    auction_end_date = models.DateTimeField(blank=False, null=False)
    # For the end date, I will have something like a dropdown list with 1/3/7 days options, and based on what the users
    # choose it will add that time to created_date and store it as the end_date

    auction_name = models.CharField(max_length=250, blank=False)

    starting_price = models.FloatField(null=False, default=0)
    minimum_increment = models.FloatField(default=1, null=False)

    has_buy_now = models.BooleanField(default=False)
    buy_now_price = models.FloatField(null=False, default=0)  # If its 0 then it doesn't exist

    status = models.CharField(choices=auction_status_choices, max_length=3, default="P")
