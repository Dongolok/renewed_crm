from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class DepartmentsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class DepartmentsById(generics.RetrieveDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class MealCategoriesList(generics.ListCreateAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategoriesSerializer


class MealCategoriesBYId(generics.RetrieveDestroyAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategoriesSerializer


class MealsList(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class ServicePercentageList(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class ServicePercentageById(generics.RetrieveDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class TablesList(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class TablesById(generics.RetrieveDestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusById(generics.RetrieveDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersById(generics.RetrieveDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class MealsToOrderList(generics.ListCreateAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrderSerializer


class MealsToOrderById(generics.RetrieveDestroyAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrderSerializer


class CheckList(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class CheckById(generics.RetrieveDestroyAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
