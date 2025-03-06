from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ...models import Category, Post
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import CategorySerializer, PostSerializer

# data = {
#     "id":1,
#     "title":"hello"
# }

# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def postlist(request):
#     if request.method== "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method=="POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
# @api_view(['GET','PUT','DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request,id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     if request.method=="GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE" :
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
# try:
#     post = Post.objects.get(pk=id)
#     serializer = PostSerilalizer(post)
#     return Response(serializer.data)
# except Post.DoesNotExist:
#     return Response({"datail":"post does not exist"},status=status.HTTP_404_NOT_FOUND)

# class PostList(APIView):
#     """getting a list of posts  and creating new posts  """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self,request):
#         """retriveing a list of posts"""
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         """creating a post with provided data"""
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class PostList(ListCreateAPIView):
    """getting a list of posts  and creating new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# class PostDetail(APIView):
#     """getting detail of the post and edit olus removing it"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer


#     def get(self,request,id):
#         """retriveing the post data """
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
#     def put(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = self.serializer_class(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,id):
#         post = get_object_or_404(Post,pk=id,status=True)
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# Example for ViewSet in CBV

# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#     def list(self,request):
#         serializer = self.serializer_class(self.queryset,many = True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk=None):
#         post_object = get_object_or_404(self.queryset,pk=pk)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)

#     def create(self,request):
#         pass

#     def update(self,request,pk=None):
#         pass

#     def partial_update(self,request,pk=None):
#         pass

#     def destroy(self,request,pk=None):
#         pass


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
    # @action(methods=["get"],detail=False)
    # def get_ok(self,request):
    #     return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
