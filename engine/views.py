from rest_framework import generics
from django.contrib.auth.models import User
from engine.models import Machine, Factory, Product, LineStep
from engine.serializers import MachineSerializer, FactorySerializer, \
    UserSerializer, ProductSerializer, LineStepSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MachineList(generics.ListCreateAPIView):
    """
    List all machines, or create a new machine.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer



class MachineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a machine.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class FactoryList(generics.ListCreateAPIView):
    """
    List all machines, or create a new machine.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FactoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a machine.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

class ProductList(generics.ListCreateAPIView):
    """
    List all machines, or create a new machine.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a machine.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LineStepList(generics.ListCreateAPIView):
    """
    List all machines, or create a new machine.
    """
    queryset = LineStep.objects.all()
    serializer_class = LineStepSerializer


class LineStepDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a machine.
    """
    queryset = LineStep.objects.all()
    serializer_class = LineStepSerializer