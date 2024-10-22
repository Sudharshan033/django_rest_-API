from rest_framework import viewsets
from .serializers import projectserializer
from .models import project_details
class permissionviewset(viewsets.ModelViewSet):
	queryset=project_details.objects.all()
	serializer_class=projectserializer