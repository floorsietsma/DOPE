from rest_framework import generics
from engine.models import Machine
from engine.serializers import MachineSerializer


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
