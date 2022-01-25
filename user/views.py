from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from user.serializer import UserSerializer
from .models import Users
import jwt


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Users.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if user.password != password:
            raise AuthenticationFailed('Incorrect password!')

        token = jwt.encode(
        {
        "id": user.id,
        },
         'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

def auth(token):
    import pdb; pdb.set_trace()
    token = token

    if not token:
        #raise AuthenticationFailed('Unauthenticated!')
        #return Response({"data":"please login"})
        return False

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except:
        #raise AuthenticationFailed('Unauthenticated!')
        #return Response({"data":"please login"})
        return False

    user = Users.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return True
