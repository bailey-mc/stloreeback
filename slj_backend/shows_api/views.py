from rest_framework import generics
from .models import Show
from .serializers import ShowSerializer

# Create your views here.


class ShowList(generics.ListCreateAPIView):
    queryset = Show.objects.all().order_by('id')
    serializer_class = ShowSerializer

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all().order_by('id')
    serializer_class = ShowSerializer
