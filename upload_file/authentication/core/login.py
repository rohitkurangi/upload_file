from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data.pop('refresh', None)  # remove refresh from the payload
        data['access'] = str(refresh.access_token)
        # Add extra responses here
        data['username'] = self.user.username
        data['group'] = str(self.user.groups.first())
        data['user_id'] = self.user.id
        return data
