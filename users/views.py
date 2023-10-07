import traceback
from django.db.models import Q 
# lookup
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import User
# Create your views here.


class user_login(APIView):
    permission_classes = []

    def post(self, request):
        response = {}
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if '@' in user_name:
            try:
                user = get_user_model().objects.get(email=user_name)
                # check_password converts plain password into '###' value
                if user.check_password(password):
                    response['success'] = True
                else:
                    response['success'] = False
            except:
                response['success'] = False
        else:
            user = authenticate(username=user_name, password=password)
            if user is not None:
                response['success'] = True
            else:
                response['success'] = False

        return Response(response)


class user_signup(APIView):
    permission_classes = []

    def post(self, request):
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')


        try:
            if get_user_model().objects.filter(Q(username=user_name)|Q(email=email)).exists():
                # to check the OR condition in ORM we use Q(lookup)
                return Response({
                    'message': f'This {email} or {user_name} already exists.'
                })
            else:
                # user = get_user_model().objects.create_user(username=user_name, email=email, phone=phone, address=address, password=password)
                user = get_user_model().objects.create(username=user_name, email=email, phone=phone, address=address)
                user.set_password(password) 
                # set_password converts plain password into '###' value
                user.save()
                return Response({
                    'messsage': f'This {user_name} or {email} has been created.'
                })
        except:
            return Response(traceback.print_exc())

        

