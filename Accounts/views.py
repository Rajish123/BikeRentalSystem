from multiprocessing import context
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status,permissions,mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import RegisterSerializer,UserSerializer,LogoutSerializer

# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        refresh= RefreshToken.for_user(user)

        return Response({
            # UserSerializer is used to retrive particular values of the users.
            'user':UserSerializer(user).data,
            'status':status.HTTP_201_CREATED,
            'message':'User successfully created',
            'refresh': str(refresh),
        '   access': str(refresh.access_token),
        })

# Simple JWT blacklist app implements its outstanding and blacklisted token lists using two models: OutstandingToken and BlacklistedToken. 
# Simple JWT will add any generated refresh or sliding tokens to a list of outstanding tokens. 
# blacklist app provides management command, flushexpiredtokens, which will delete any tokens from the outstanding list and blacklist that have expired
# ROTATE_REFRESH_TOKENS if True, if a refresh token is submitted to the TokenRefreshView, a new refresh token will be returned along with the new access token.
# BLACKLIST_AFTER_ROTATION if True, causes refresh tokens submitted to the TokenRefreshView to be added to the blacklist 

# simple jwt is stateless i.e, dont keep user authentication in app's memory
class LogutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)