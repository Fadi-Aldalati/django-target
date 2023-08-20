from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model
# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields = ['id','username','email','first_name','last_name','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        return get_user_model().objects.get(id=1)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]