from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category in the system.
    """

    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = 'Category'


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
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('user', 'menu_item')
        verbose_name_plural = 'Cart'


class CartItem(models.Model):
    """
    Represents an item in a cart.

    Attributes:
        cart (Cart): The cart to which this item belongs.
        menu_item (MenuItem): The menu item associated with this cart item.
        quantity (int): The quantity of the menu item in the cart.
        unit_price (Decimal): The unit price of the menu item.
        price (Decimal): The total price of the cart item.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Cart Item'


class Order(models.Model):
    """
    Represents an order made by a user.

    Attributes:
        user (FK): The user who placed the order.
        delivery_crew (FK): The delivery crew assigned to the order (optional).
        status (BooleanField): The status of the order.
        total (DecimalField): The total amount of the order.
        date (DateTimeField): The date and time when the order was created.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    delivery_crew = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='delivery_crew',
        null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, db_index=False)

    class Meta:
        verbose_name_plural = 'Order'


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
