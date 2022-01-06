from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Packages, Bookings, Profile
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password']
		extra_kwargs = {'password': {'write_only': True, 'required': True}}

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'

class PackagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Packages
		fields = '__all__'

class BookingsSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = Bookings
		fields = '__all__'   
		