from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models.subscription_feed_model import SubscriptionFeed
from ..serializers.suscription_feed_serializer import CreateFeedSerializers
from rest_framework.response import Response



class CreateSubscriptionFeedAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = CreateFeedSerializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Succesfully created feed.",
        })        

