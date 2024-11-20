from rest_framework import viewsets, filters
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated
                                        )

from posts.models import Post, Group, Follow
from .serializers import (PostSerializer,
                          GroupSerializer,
                          CommentSerializer,
                          FollowSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.select_related('author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backend = (filters.SearchFilter,)
    search_fields = ('following__username')

    def get_queryset(self):
        queryset = self.request.user.follower.all()
        search_param = self.request.query_params.get('search', None)
        if search_param:
            queryset = queryset.filter(
                following__username=search_param)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        following_user = serializer.validated_data['following']

        if user == following_user:
            raise ValidationError(
                {
                    'detail':
                    'Вы не можете подписаться на самого себя.'
                }
            )

        if Follow.objects.filter(user=user,
                                 following=following_user).exists():
            raise ValidationError(
                {
                    'detail':
                    'Вы уже подписаны на этого пользователя.'
                }
            )
        serializer.save(user=user)
