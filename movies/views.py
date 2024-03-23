from rest_framework import viewsets, mixins

from movies.models import Movie, Director
from movies.serializers import MovieSerializer, DirectorSerializer
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"list": serializer.data})

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(status=202)


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"list": serializer.data})
