from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet, ModelViewSet
from django_filters import rest_framework as filters

from comment.filters import CommentFilter
from comment.models import Comment
from comment.paginations import LargeResultsSetPagination
from comment.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CommentFilter
    pagination_class = LargeResultsSetPagination
    permission_classes = []


    description = openapi.Parameter('description', openapi.IN_QUERY,
                                    description="field you want to order by to",
                                    type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[description, ])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    #     search = self.request.query_params.get("search")
    #     end_date = self.request.query_params.get("end_date")
    #     start_date = self.request.query_params.get("start_date")
    #     comments = Comment.objects.all().order_by('-created_at')
    #     if search:
    #         comments = Comment.objects.filter(description__icontains=search).order_by('-created_at')
    #     if end_date and not start_date:
    #         comments = comments.filter(created_at__lte=end_date)
    #     if start_date and not end_date:
    #         comments = comments.filter(created_at__gte=start_date)
    #     if start_date and end_date:
    #         comments = comments.filter(created_at__gte=start_date, created_at__lte=end_date)
    #
    #     return comments

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


    # @action(detail=False, methods=['get'], url_path="la")
    # def search_comments(self, request):
    #     search = request.query_params.get("search")
    #     comments = Comment.objects.all().order_by('-created_at')
    #     if search:
    #         comments = Comment.objects.filter(description__icontains=search).order_by('-created_at')
    #
    #     serializer = self.get_serializer(comments, many=True)
    #     return Response(serializer.data)