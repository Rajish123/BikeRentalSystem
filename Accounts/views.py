from multiprocessing import context
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status,permissions,mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import RegisterSerializer,UserSerializer,LogoutSerializer,ChangePasswordSerializer

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
            'access': str(refresh.access_token),
        })

# Simple JWT blacklist app implements its outstanding and blacklisted token lists using two models: OutstandingToken and BlacklistedToken. 
# Simple JWT will add any generated refresh or sliding tokens to a list of outstanding tokens. 
# blacklist app provides management command, flushexpiredtokens, which will delete any tokens from the outstanding list and blacklist that have expired
# ROTATE_REFRESH_TOKENS if True, if a refresh token is submitted to the TokenRefreshView, a new refresh token will be returned along with the new access token.
# BLACKLIST_AFTER_ROTATION if True, causes refresh tokens submitted to the TokenRefreshView to be added to the blacklist 

# simple jwt is stateless i.e, dont keep user authentication in app's memory
# body:refresh:key
class LogutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({
            'status':status.HTTP_200_OK,
            'message':'Successful Logout'

        })

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self,queryset = None):
        obj = self.request.user
        return obj

    def update(self,request,*args,**kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
        
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'message':'Wrong Password'
                })
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status':status.HTTP_202_ACCEPTED,
                'message':'Password Changed Successfully',
                'data':serializer.data
            }
            return Response(response)
        
        return Response(serializer.errors)

