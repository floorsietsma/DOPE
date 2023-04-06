from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from engine.models import Machine
from engine.serializers import MachineSerializer


class MachineList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all machines, or create a new machine.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MachineDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a machine.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)