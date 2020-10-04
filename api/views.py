# from rest_framework import status
# from rest_framework.views import APIView
#
# from rest_framework.response import Response
# from .models import MovieModel
# from .serializers import MovieSerialaizer
#
#
# class MovieView(APIView):
#     def get(self, request, *args, **kwargs):
#         movies = MovieModel.objects.all()
#         data = MovieSerialaizer(movies, many=True).data
#         return Response(data, status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         serializer = MovieSerialaizer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors)
#         serializer.save()
#         return Response(serializer.data)

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MovieSerialaizer
from .models import MovieModel


# class MovieView(ListCreateAPIView):
#     serializer_class = MovieSerialaizer
#     queryset = MovieModel.objects.all()

class MovieView(ListCreateAPIView):
    serializer_class = MovieSerialaizer

    def get_queryset(self):

        qs = MovieModel.objects.all()
        req = self.request
        query = req.query_params.get('filter')
        if query:
            return qs.filter(title__icontains=query)
        return qs


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerialaizer
    queryset = MovieModel.objects.all()
