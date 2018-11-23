from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from . models import User
from . serializer import UserSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10

class UserViewSet(viewsets.ViewSet):

    pagination_class = CustomPagination
    paginate_by = 3
    def create(self, request, *args, **kwargs):
        '''
        create user api endpoint
        '''
        print("-----------create method invoke")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        '''
        get list of users
        '''
        print('------list all users')
        queryset = User.objects.filter(status=1)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        '''
        retrive detail of user
        '''
        print('-----retrive single instance')
        user = User.objects.filter(id=pk, status=1).first()
        if user:
            serializer = UserSerializer(user)
            return  Response(serializer.data, status=status.HTTP_200_OK)
        return Response("User is not exist", status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        '''
        update user api endpoint
        '''
        print('--------update method invoke')
        user = User.objects.filter(id=pk, status=1).first()
        if user:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("User is not exist", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete user endpoint
        '''
        print('-------delete method invoke')
        user = User.objects.filter(id=pk, status=1).first()
        if user:
            user.status=0
            user.save()
            return  Response("User deleted", status=status.HTTP_200_OK)
        return Response("User is not exist", status.HTTP_400_BAD_REQUEST)


