from rest_framework import serializers
from .models import project_details
class projectserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=project_details
		fields=('projectname','objective','studentname','department')