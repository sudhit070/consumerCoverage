from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

from App_User.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


# -------------------- Function Base Api -----------------------
@api_view(['GET'])
def get_book(request):
    book_list = Book.objects.all()
    print(book_list)
    json_book = BookSerializer(book_list, many=True)
    print(json_book)
    print(json_book.data)
    return Response({'status': 200, 'Data': json_book.data})


@api_view(['GET'])
def home(request):
    student_list = Student.objects.all()
    json_student = StudentSerializer(student_list, many=True)
    return Response({'status': 200, 'Data': json_student.data})


@api_view(['POST'])
def post_student(request):
    data = request.data
    data_serializers = StudentSerializer(data=request.data)
    if data_serializers.is_valid():
        data_serializers.save()
        return Response({'status': 200, 'message': "Your Data Successfully Added!"})

    return Response({'status': 403, 'payload': data_serializers.errors, 'message': "Something Went Wrong!"})


@api_view(['PATCH', 'PUT'])
def update_student(request, userid):
    try:
        print(request.method)
        student_obj = Student.objects.get(id=userid)

        if request.method == 'PUT':
            data_serializers = StudentSerializer(student_obj, data=request.data)
        else:
            data_serializers = StudentSerializer(student_obj, data=request.data, partial=True)

        if not data_serializers.is_valid():
            return Response({'status': 404, 'error': data_serializers.errors, 'message': 'Something Went Wrong!'})

        data_serializers.save()
        return Response({'status': 200, 'message': 'Data Successfully Updated!'})

    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'Invalid Id'})


@api_view(['DELETE'])
def delete_student(request, userid):
    try:
        student_obj = Student.objects.get(id=userid)
        student_obj.delete()
        return Response({'status': 200, 'message': 'Data Successfully Deleted!'})
    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'Invalid Id'})


# -------------------- Class Base Api -----------------------
class StudentAPI(APIView):

    def get(self, request):
        student_list = Student.objects.all()
        json_student = StudentSerializer(student_list, many=True)
        return Response({'status': 200, 'Data': json_student.data})

    def post(self, request):
        data = request.data
        print(data)
        data_serializers = StudentSerializer(data=data)
        if data_serializers.is_valid():
            data_serializers.save()
            return Response({'status': 200, 'message': "Your Data Successfully Added!"})

        return Response({'status': 403, 'payload': data_serializers.errors, 'message': "Something Went Wrong!"})

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])

            if request.method == 'PUT':
                data_serializers = StudentSerializer(student_obj, data=request.data)
            else:
                data_serializers = StudentSerializer(student_obj, data=request.data, partial=True)

            if not data_serializers.is_valid():
                return Response({'status': 404, 'error': data_serializers.errors, 'message': 'Something Went Wrong!'})

            data_serializers.save()
            return Response({'status': 200, 'message': 'Data Successfully Updated!'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid Id'})

    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({'status': 200, 'message': 'Data Successfully Deleted!'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid Id'})
