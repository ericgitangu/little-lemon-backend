# Django API Endpoints - META Backend Final Project for the Backend Specialization

## Project objectives

1. Using Djoser and DRF for Authentication on the project level - Coursera META specialization certification for the API final project

2. User Endpoints note only admins can change users, my menu items, and assign users to specific groups, managers, delivers etc (IsAdmin)

3. Users can only update their own info when authenticated (IsAuthenticated)

4. API throttling implemented for unauthenticated users to 10 calls/min and 20 calls/mins for authenticated uses.

5. Endpoints - Users, Menu-items, Cart, Categories, Orders, Delivery Crews, Managers with granular access, users, managers and admins

## User Endpoints

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

### Change featured item

- Endpoint: `api/manager-featured-item/<int:pk>/`
- Method: GET
- View: `ChangeFeaturedItemView`
- Name: `change-featured-item`

### Manager Assign Order

- Endpoint: `api/manager-assign-order/<int:pk>/`
- Method: GET
- View: `AssignOrderView`
- Name: `assign-order`

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

### Change order status by the delivery crew user

- Endpoint: `api/delivery-crew/change-status/<int:pk>/`
- Method: GET
- View: `ChangeOrderStatusView`
- Name: `change-order-status`

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

## Groups endpoints

### List all manager users from the groups

- Endpoint: `api/groups/manager/users/`
- Method: GET
- View: `ManagerUserListView`
- Name: `manager-user-list`

### Create a manager user in a group

- Endpoint: `api/groups/manager/users/create/`
- Method: POST
- View: `ManagerUserCreateView`
- Name: `manager-user-create`

### Manager User Delete

- Endpoint: `api/groups/manager/users/delete/<int:pk>/`
- Method: DELETE
- View: `ManagerUserDeleteView`
- Name: `manager-user-delete`

### Delivery Crew User List

- Endpoint: `api/groups/delivery-crew/users/`
- Method: GET
- View: `DeliveryCrewUserListView`
- Name: `delivery-crew-user-list`

### Delivery Crew User Create

- Endpoint: `api/groups/delivery-crew/users/create/`
- Method: POST
- View: `DeliveryCrewUserCreateView`
- Name: `delivery-crew-user-create`

### Delivery Crew User Delete

- Endpoint: `api/groups/delivery-crew/users/delete/<int:pk>/`
- Method: DELETE
- View: `DeliveryCrewUserDeleteView`
- Name: `delivery-crew-user-delete`

### Assign Order

- Endpoint: `api/groups/manager/assign-order/<int:pk>/`
- Method: GET
- View: `AssignOrderView`
- Name: `assign-order`

### Change Featured Item

- Endpoint: `api/groups/manager/featured-item/<int:pk>/`
- Method: GET
- View: `ChangeFeaturedItemView`
- Name: `change-featured-item`

### Change Order Status

- Endpoint: `api/groups/delivery-crew/change-status/<int:pk>/`
- Method: GET
- View: `ChangeOrderStatusView`
- Name: `change-order-status`

### Cart List

- Endpoint: `api/groups/cart/`
- Method: GET
- View: `CartItemListView`
- Name: `cart-list`

### Cart Detail

- Endpoint: `api/groups/cart/<int:pk>/`
- Method: GET
- View: `CartItemListView`
- Name: `cart-detail`

### Cart Create

- Endpoint: `api/groups/cart/create/`
- Method: POST
- View: `CartItemCreateView`
- Name: `cart-create`

### Cart Update

- Endpoint: `api/groups/cart/update/<int:pk>/`
- Method: PUT/PATCH
- View: `CartItemUpdateView`
- Name: `cart-update`

### Cart Delete

- Endpoint: `api/groups/cart/delete/<int:pk>/`
- Method: DELETE
- View: `CartItemDeleteView`
- Name: `cart-delete`

### Order List

- Endpoint: `api/groups/orders/`
- Method: GET
- View: `OrderListView`
- Name: `order-list`

### Order Detail

- Endpoint: `api/groups/orders/<int:pk>/`
- Method: GET
- View: `OrderDetailView`
- Name: `order-detail`

### Order Create

- Endpoint: `api/groups/orders/create/`
- Method: POST
- View: `OrderCreateView`
- Name: `order-create`

### Order Update

- Endpoint: `api/groups/orders/update/<int:pk>/`
- Method: PUT/PATCH
- View: `OrderUpdateView`
- Name: `order-update`

### Order Delete

- Endpoint: `api/groups/orders/delete/<int:pk>/`
- Method: DELETE
- View: `OrderDeleteView`
- Name: `order-delete`

### Category List

- Endpoint: `api/groups/categories/`
- Method: GET
- View: `CategoryListView`
- Name: `category-list`

### Category Detail

- Endpoint: `api/groups/categories/<int:pk>/`
- Method: GET
- View: `CategoryDetailView`
- Name: `category-detail`

### Category Create

- Endpoint: `api/groups/categories/create/`
- Method: POST
- View: `CategoryCreateView`
- Name: `category-create`

### Category Update

- Endpoint: `api/groups/categories/update/<int:pk>/`
- Method: PUT/PATCH
- View: `CategoryUpdateView`
- Name: `category-update`

### Category Delete

- Endpoint: `api/groups/categories/delete/<int:pk>/`
- Method: DELETE
- View: `CategoryDeleteView`
- Name: `category-delete`

### User List

- Endpoint: `api/groups/users/`
- Method: GET
- View: `UserListView`
- Name: `user-list`

### User Detail

- Endpoint: `api/groups/users/<int:pk>/`
- Method: GET
- View: `UserDetailView`
- Name: `user-detail`

### User Create

- Endpoint: `api/groups/users/create/`
- Method: POST
- View: `UserCreateView`
- Name: `user-create`

### User Update

- Endpoint: `api/groups/users/update/<int:pk>/`
- Method: PUT/PATCH
- View: `UserUpdateView`
- Name: `user-update`

### User Delete

- Endpoint: `api/groups/users/delete/<int:pk>/`
- Method: DELETE
- View: `UserDeleteView`
- Name: `user-delete`

### Current User

- Endpoint: `api/groups/current-user/`
- Method: GET
- View: `CurrentUserView`
- Name: `current-user`

### User Login

- Endpoint: `api/groups/token/login`
- Method: GET
- View: `UserTokenView`
- Name: `user-login`

### User Logout

- Endpoint: `api/groups/token/logout`
- Method: GET
- View: `UserTokenView`
- Name: `user-logout`

### Menu Item List

- Endpoint: `api/groups/menu-items/`
- Method: GET
- View: `MenuItemListView`
- Name: `menu-item-list`

### Menu Item Detail

- Endpoint: `api/groups/menu-items/<int:pk>/`
- Method: GET
- View: `MenuItemDetailView`
- Name: `menu-item-detail`

### Menu Item Create

- Endpoint: `api/groups/menu-items/create/`
- Method: POST
- View: `MenuItemCreateView`
- Name: `menu-item-create`

### Menu Item Update

- Endpoint: `api/groups/menu-items/update/<int:pk>/`
- Method: PUT/PATCH
- View: `MenuItemUpdateView`
- Name: `menu-item-update`

### Menu Item Delete

- Endpoint: `api/groups/menu-items/delete/<int:pk>/`
- Method: DELETE
- View: `MenuItemDeleteView`
- Name: `menu-item-delete`

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
5. api/token - (JWT, obtain an access & refresh token)
6. api/token/refresh - (Renew an access token using a refresh token)
7. api/token/verify - Takes a token and indicates if it is valid.

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
