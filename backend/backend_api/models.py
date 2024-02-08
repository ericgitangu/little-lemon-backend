from django.db import models
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Category(models.Model):
    """
    Represents a category in the system.
    """

    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title
    


class MenuItem(models.Model):
    """
    Represents a menu item.

    Attributes:
        title (str): The title of the menu item.
        price (Decimal): The price of the menu item.
        featured (bool): Indicates if the menu item is featured.
        category (Category): The category to which the menu item belongs.
    """
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='menu_items')

    class Meta:
        verbose_name_plural = 'Menu Item'

    def __str__(self) -> str:
        return self.title


class Cart(models.Model):
    """
    Represents a cart item in the backend API.

    Attributes:
        user (User): The user who owns the cart item.
        menu_item (MenuItem): The menu item added to the cart.
        quantity (int): The quantity of the menu item in the cart.
        unit_price (Decimal): The unit price of the menu item.
        price (Decimal): The total price of the cart item.

    Meta:
        unique_together (tuple): A tuple specifying that the combination
        of user and menu_item should be unique.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'menu_item')
        verbose_name_plural = 'Cart'

    def __str__(self) -> str:
        return f'{self.user.username} - {self.menu_item.title}'


class Order(models.Model):
    """
    Represents an order made by a user.

    Attributes:
        user (FK): The user who placed the order.
        delivery_crew (FK): The delivery crew assigned to the order (optional).
        delivery status (BooleanField): The delivery status of the order.
        total (DecimalField): The total amount of the order.
        date (DateTimeField): The date and time when the order was created.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    delivery_crew = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='delivery_crew',
        null=True)
    delivered = models.BooleanField(db_index=False, default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, db_index=False)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self) -> str:
        return f'{self.user.username} - {self.date}'


class OrderItem(models.Model):
    """
    Represents an item in an order.

    Attributes:
        order (Order): The order to which this item belongs.
        menu_item (MenuItem): The menu item associated with this order item.
        quantity (int): The quantity of the menu item in the order.
        unit_price (Decimal): The unit price of the menu item.
        price (Decimal): The total price of the order item.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')
        verbose_name_plural = 'Order Item'

    def __str__(self) -> str:
        return f'{self.order.user.username} - {self.menu_item.title}'

class DeliveryCrewUser(models.Model):
    """
    Represents a delivery crew user in the system.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, db_index=True)

    class Meta:
        verbose_name_plural = 'Delivery Crew User'

    def __str__(self) -> str:
        return self.user.username
    

class UserToken(models.Model):
    """
    Represents a user token in the system.

    Attributes:
        user (User): The user associated with the token.
        token (CharField): The token string.
        created_at (DateTimeField): The date and time when the token was created.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Token'

    def __str__(self) -> str:
        return f'{self.user.username} - {self.token}'