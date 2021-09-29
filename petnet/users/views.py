from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)