from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Systems(models.Model):
    name = models.CharField(max_length=50 ,blank=True, null=True)
    short_description = models.CharField(max_length=100 ,blank=True, null=True)
    pricing = models.DecimalField(decimal_places=2 ,blank=True, null=True)
    roi = models.CharField(max_length=50 ,blank=True, null=True)
    LastProfit = models.CharField(max_length=50 ,blank=True, null=True)
    LastProfitWinRate = models.CharField(max_length=50 ,blank=True, null=True)
    TotalProfits = models.DecimalField(decimal_places=4 ,blank=True, null=True)
    TotalCopyTraders = models.CharField(max_length=50 ,blank=True, null=True)
    AUM = models.CharField(max_length=50 ,blank=True, null=True)
    telegram = models.CharField(max_length=200 ,blank=True, null=True)
    telegram_visible = models.BooleanField(default=False, null=False)
    discord = models.CharField(max_length=200 ,blank=True, null=True)
    discord_visible = models.BooleanField(default=False, null=False)
    youtube = models.CharField(max_length=200 ,blank=True, null=True)
    youtube_visible = models.BooleanField(default=False, null=False)
    full = models.BooleanField(default=False, null=False)

STATUS_CHOICES = (
    ('Not Paid', 'Not Paid'),
    ('Paid', 'Paid'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    system = models.ForeignKey(Systems, verbose_name="Systems", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.system.pricing
    

class CopyTraders(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    orderid = models.CharField(max_length=255, null=True, blank=True, verbose_name="Unique order ID")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    system = models.ForeignKey(Systems, verbose_name="Systems", on_delete=models.CASCADE)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Not Paid"
        )
    
    @property
    def valid_till(self):
        return self.ordered_date  #implement logic to add validitty period
    