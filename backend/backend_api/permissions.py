from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class that allows only the owner of an object to modify it,
    while allowing read-only access to other users.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class IsManager(permissions.BasePermission):
    """
    Custom permission class that allows only users in the Manager group to access the view.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()
    
class IsDeliveryCrew(permissions.BasePermission):
    """
    Custom permission class that allows only users in the Delivery Crew group to access the view.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery Crew').exists()
    
class IsCustomer(permissions.BasePermission):
    """
    Custom permission class that allows only users in the Customer group to access the view.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Customer').exists()