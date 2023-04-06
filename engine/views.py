from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from engine.models import Machine
from engine.serializers import MachineSerializer


class MachineList(APIView):
    """
    List all machines, or create a new machine.
    """

    def get(self, request, format=None):
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachineDetail(APIView):
    """
    Retrieve, update or delete a machine.
    """
    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        machine = self.get_object(pk)
        serializer = MachineSerializer(machine)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        machine = self.get_object(pk)
        serializer = MachineSerializer(machine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        machine = self.get_object(pk)
        machine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)