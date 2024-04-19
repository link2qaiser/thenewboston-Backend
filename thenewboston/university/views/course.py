from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from thenewboston.general.pagination import CustomPageNumberPagination

from ..models import Course
from ..models.base import PublicationStatusStatus
from ..serializers.course import CourseReadSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.filter(publication_status=PublicationStatusStatus.PUBLISHED).order_by('-created_date')
    serializer_class = CourseReadSerializer
