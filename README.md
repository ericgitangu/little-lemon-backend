# Django API Endpoints 

## Using Djoser and DRF for Authentication on the project level - Coursera META specialization certification for the API final project

## User Endpoints note only admins can change users (IsAdmin)

## Users can only update their own info when authenticated (IsAuthenticated)

## API throttling implemented for unauthenticated users to 10 calls/min and 20 calls/mins for authenticated uses.

### List all users

- Endpoint: `/users/`
- Method: GET
- View: `UserListView`
- Name: `user-list`

### Get user details

- Endpoint: `api/users/<int:pk>/`
- Method: GET
- View: `UserDetailView`
- Name: `user-detail`

### Register a new user

- Endpoint: `api/register/`
- Method: POST
- View: `UserRegistrationView`
- Name: `user-registration`

### Create a new user

- Endpoint: `api/users/create/`
- Method: POST
- View: `UserCreateView`
- Name: `user-create`

### Update a user

- Endpoint: `api/users/update/<int:pk>/`
- Method: PUT/PATCH
- View: `UserUpdateView`
- Name: `user-update`

### Delete a user

- Endpoint: `api/users/delete/<int:pk>/`
- Method: DELETE
- View: `UserDeleteView`
- Name: `user-delete`

### Get current user details

- Endpoint: `api/current-user/`
- Method: GET
- View: `CurrentUserView`
- Name: `current-user`

### User login

- Endpoint: `api/token/login`
- Method: POST
- View: `UserTokenView`
- Name: `user-login`

### User logout

- Endpoint: `api/token/logout`
- Method: POST
- View: `UserTokenView`
- Name: `user-logout`

## Menu Item Endpoints

### List all menu items

- Endpoint: `api/menu-items/`
- Method: GET
- View: `MenuItemListView`
- Name: `menu-item-list`

### Get menu item details

- Endpoint: `api/menu-items/<int:pk>/`
- Method: GET
- View: `MenuItemDetailView`
- Name: `menu-item-detail`

### Create a new menu item

- Endpoint: `api/menu-items/create/`
- Method: POST
- View: `MenuItemCreateView`
- Name: `menu-item-create`

### Update a menu item

- Endpoint: `api/menu-items/update/<int:pk>/`
- Method: PUT/PATCH
- View: `MenuItemUpdateView`
- Name: `menu-item-update`

### Delete a menu item

- Endpoint: `api/menu-items/delete/<int:pk>/`
- Method: DELETE
- View: `MenuItemDeleteView`
- Name: `menu-item-delete`

## Manager User Endpoints

### List all manager users

- Endpoint: `api/manager-users/`
- Method: GET
- View: `ManagerUserListView`
- Name: `manager-user-list`

### Create a new manager user

- Endpoint: `api/manager-users/create/`
- Method: POST
- View: `ManagerUserCreateView`
- Name: `manager-user-create`

### Delete a manager user

- Endpoint: `api/manager-users/delete/<int:pk>/`
- Method: DELETE
- View: `ManagerUserDeleteView`
- Name: `manager-user-delete`

## Delivery Crew User Endpoints

### List all delivery crew users

- Endpoint: `api/delivery-crew-users/`
- Method: GET
- View: `DeliveryCrewUserListView`
- Name: `delivery-crew-user-list`

### Create a new delivery crew user

- Endpoint: `api/delivery-crew-users/create/`
- Method: POST
- View: `DeliveryCrewUserCreateView`
- Name: `delivery-crew-user-create`

### Delete a delivery crew user

- Endpoint: `/delivery-crew-users/delete/<int:pk>/`
- Method: DELETE
- View: `DeliveryCrewUserDeleteView`
- Name: `delivery-crew-user-delete`

## Cart Item Endpoints

### List all cart items

- Endpoint: `api/cart/`
- Method: GET
- View: `CartItemListView`
- Name: `cart-list`

### Get cart item details

- Endpoint: `api/cart/<int:pk>/`
- Method: GET
- View: `CartItemListView`
- Name: `cart-detail`

### Create a new cart item

- Endpoint: `api/cart/create/`
- Method: POST
- View: `CartItemListView`
- Name: `cart-create`

### Update a cart item

- Endpoint: `api/cart/update/<int:pk>/`
- Method: PUT/PATCH
- View: `CartItemListView`
- Name: `cart-update`

### Delete a cart item

- Endpoint: `api/cart/delete/<int:pk>/`
- Method: DELETE
- View: `CartItemListView`
- Name: `cart-delete`

## Order Endpoints

### List all orders

- Endpoint: `api/orders/`
- Method: GET
- View: `OrderListView`
- Name: `order-list`

### Get order details

- Endpoint: `api/orders/<int:pk>/`
- Method: GET
- View: `OrderDetailView`
- Name: `order-detail`

### Create a new order

- Endpoint: `api/orders/create/`
- Method: POST
- View: `OrderCreateView`
- Name: `order-create`

### Update an order

- Endpoint: `api/orders/update/<int:pk>/`
- Method: PUT/PATCH
- View: `OrderUpdateView`
- Name: `order-update`

### Delete an order

- Endpoint: `api/orders/delete/<int:pk>/`
- Method: DELETE
- View: `OrderDeleteView`
- Name: `order-delete`

## Category Endpoints

### List all categories

- Endpoint: `api/categories/`
- Method: GET
- View: `CategoryListView`
- Name: `category-list`

### Get category details

- Endpoint: `api/categories/<int:pk>/`
- Method: GET
- View: `CategoryDetailView`
- Name: `category-detail`

### Create a new category

- Endpoint: `api/categories/create/`
- Method: POST
- View: `CategoryCreateView`
- Name: `category-create`

### Update a category

- Endpoint: `api/categories/update/<int:pk>/`
- Method: PUT/PATCH
- View: `CategoryUpdateView`
- Name: `category-update`

### Delete a category

- Endpoint: `api/categories/delete/<int:pk>/`
- Method: DELETE
- View: `CategoryDeleteView`
- Name: `category-delete

## Models

1. Category - verbose_name_plural 'Category'
2. MenuItem - verbose_name_plural 'Menu Item'
3. Cart - verbose_name_plural 'Cart'
4. CartItem - verbose_name_plural 'Cart Item'
5. Order - verbose_name_plural 'Order'
6. OrderItem - - verbose_name_plural 'Order Item'

## Databases

1. sqlite
2. MySQL (use --database mysql to migrate to your mysql instance)

## Project URLs

1. admin
2. api
3. api-auth - (rest_framework endpoints)
4. auth - (djoser - urls, authtokens)

## Project

- backend

## App

- backend_api

## Set up

1. cd backend
2. pipenv shell
3. pipenv install
4. make migrations
5. migrate (you can use the sqlite DB or change the credential settings to use your mysql instance)
6. create a super user 'createsuper'
7. run server
8. Test the endpoints as documented above, note the super user has priviledges to make changes to models as you 
   would in the admin panel.
