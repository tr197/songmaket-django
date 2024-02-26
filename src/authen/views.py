from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User
from rest_framework.response import Response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if "access" in response.data:
            try:
                access_token = response.data["access"]
                token = RefreshToken(access_token)
                user = User.objects.get(id=token["user_id"])

                user_data = {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
                response.data["user"] = user_data
            except User.DoesNotExist:
                pass
        return response
