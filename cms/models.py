from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=50 ,blank=True, null=True)
    trading_style = models.CharField(max_length=100 ,blank=True, null=True)
    pricing = models.DecimalField(max_digits=15, decimal_places=2 ,blank=True, null=True)
    roi = models.CharField(max_length=50 ,blank=True, null=True)
    LastProfit = models.CharField(max_length=50 ,blank=True, null=True)
    LastProfitWinRate = models.CharField(max_length=50 ,blank=True, null=True)
    TotalProfits = models.DecimalField(max_digits=15, decimal_places=4 ,blank=True, null=True)
    TotalCopyTraders = models.CharField(max_length=50 ,blank=True, null=True)
    AUM = models.CharField(max_length=50 ,blank=True, null=True)
    telegram = models.CharField(max_length=200 ,blank=True, null=True)
    telegram_visible = models.BooleanField(default=False, null=False)
    discord = models.CharField(max_length=200 ,blank=True, null=True)
    discord_visible = models.BooleanField(default=False, null=False)
    youtube = models.CharField(max_length=200 ,blank=True, null=True)
    youtube_visible = models.BooleanField(default=False, null=False)
    twitch = models.CharField(max_length=200 ,blank=True, null=True)
    twitch_visible = models.BooleanField(default=False, null=False)
    full = models.BooleanField(default=False, null=False)

class SystemData(models.Model):
    name = models.ForeignKey(System, verbose_name="System", on_delete=models.CASCADE)

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
    system = models.ForeignKey(System, verbose_name="System", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.system.pricing
    

class CopyTrader(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    orderid = models.CharField(max_length=255, null=True, blank=True, verbose_name="Unique order ID")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    system = models.ForeignKey(System, verbose_name="System", on_delete=models.CASCADE)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Not Paid"
        )
    
    @property
    def valid_till(self):
        return self.ordered_date  #implement logic to add validitty 
    
class Wallet(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2 ,blank=False, null=True)

TRANSACTION_CHOICES = (
    ('Deposit', 'Deposit'),
    ('Transfer', 'Transfer'),
    ('Withdraw', 'Withdraw'),
)

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, verbose_name="Wallet", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2 ,blank=False, null=True)
    transaction_type = models.CharField(
        choices=TRANSACTION_CHOICES,
        max_length=50,
        default='Deposit'
        )

class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="Service Title")
    slug = models.SlugField(max_length=160, verbose_name="Service Slug")
    short_description = models.TextField(verbose_name="Short Description")
    detail_description = models.TextField(blank=True, null=True, verbose_name="Detail Description")
    service_image = models.ImageField(upload_to='service', blank=True, null=True, verbose_name="Service Image")
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

class Chat(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

class Reply(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, verbose_name='Chat', on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    
admin.site.register(System)
admin.site.register(SystemData)
admin.site.register(Cart)
admin.site.register(CopyTrader)
admin.site.register(Service)
admin.site.register(Chat)
admin.site.register(Reply)