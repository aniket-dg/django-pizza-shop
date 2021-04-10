from rest_framework import generics, mixins, status
from order.models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import filters
class ListOrder(generics.ListAPIView, filters.BaseFilterBackend):
    '''
    get:
    Return a List of all Orders

    delete:
    Delete all orders

    '''
    model = Order
    serializer_class = OrderSerializer
    filter_fields = ('pizza_size', 'pizza_type')
    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def delete(self, request ,*args, **kwargs):
        queryset = self.model.objects.all().delete()
        return Response(
            {"res":"All Orders Deleted"},
            status=status.HTTP_200_OK
        )

class CreateOrder(generics.CreateAPIView, mixins.CreateModelMixin):
    '''
    Create a new Order
    '''
    model = Order   
    serializer_class = OrderSerializer

    
class ModifyOrder(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin ,generics.GenericAPIView):
    '''
    get:
    Returns a Specific Order.

    delete:
    Delete the order with specific id.

    put:
    Update the existing Order
    '''
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request ,*args, **kwargs):
        order_instance = self.get_object()
        if not order_instance:
            return Response(
                {"res":"Order with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance.delete()
        return Response(
            {"res":"Order Deleted"},
            status=status.HTTP_200_OK
        )
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)