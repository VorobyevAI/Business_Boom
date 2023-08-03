from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions import IsOwnerOrReadOnly
from .models import CustomUser, Post
from .serializers import UserSerializer, PostSerializer
from rest_framework.response import Response


class UserAPIView(APIView):
    """
        Вывод списка пользователей

        """
    renderer_classes = [TemplateHTMLRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    template_name = 'home.html'

    def get(self, request):
        users = CustomUser.objects.all()
        return Response({'serializer': UserSerializer(users, many=True).data, 'users': users})


class PostAPIView(APIView):
    """
        Вывод списка постов для указанного пользователя

        """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list_post.html'

    def get(self, request, user_id):
        queryset = Post.objects.filter(user__id=user_id)
        return Response({'serializer': PostSerializer(queryset, many=True).data, 'posts': queryset})

    def post(self, request, user_id):
        request.data["user_id"] = user_id
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Response({'post': serializer.data})
        return render(request, "list_post.html")


class PostAdd(APIView):
    """
        Добавление поста

        """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = [TemplateHTMLRenderer]
    success_url = reverse_lazy('/home')
    template_name = 'post_add.html'

    def get(self, request, user_id):
        if request.user.is_authenticated:
            return Response({"status":200})
        else:
            return HttpResponseRedirect("/")

    def post(self, request, user_id):
        request.data._mutable = True
        request.data['user'] = request.user.id
        request.data._mutable = False
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponseRedirect(redirect_to=f"/user/{user_id}/post_list/")



class RegistationUser(APIView):
    """
        Регистрация новго пользователя

        """
    renderer_classes = [TemplateHTMLRenderer]
    success_url = reverse_lazy('/home')
    template_name = 'signup.html'

    def get(self, request):
        return Response({"status":200})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        request.data._mutable = True
        request.data["password"] = make_password(request.data["password"])
        request.data._mutable = False
        if serializer.is_valid():

            serializer.save()
            return HttpResponseRedirect(redirect_to=f"/")
        else:
            return HttpResponseRedirect(redirect_to=f"/signup/")



class PostAPIUpdate(generics.UpdateAPIView):
    """
    Обновление данных в БД

    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class PostAPIDelete(generics.DestroyAPIView):
    """
       Удаление данных из БД

       """
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

