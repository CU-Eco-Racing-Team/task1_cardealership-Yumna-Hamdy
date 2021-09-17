from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination



#some features are not complete yet

class RespondPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

@api_view(['POST','GET'])   
def Add_Dealer(request):
    if request.method == 'POST':
        serializer = Dealers_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        try:

            get_dealer = Dealers.objects.all()
        
        except:
        
            return Response(status=status.HTTP_404_NOT_FOUND)

    #  for pagination
    Paginator = RespondPagination()
    results = Paginator.paginate_queryset(get_dealer, request)
    Dealer = Dealers_serializer(results, many=True).data
    return Paginator.get_paginated_response({'Dealer': Dealer})

   

@api_view(['PUT'])
def Edit_Dealer(request, SSN):
    try:
        get_list = Dealers.objects.get(SSN=SSN)
        
        serializer = Dealers_serializer(get_list, data=request.data)
        if serializer.is_valid():
                
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def Promote_Dealer(request, SSN):
    try:
        get_list = Dealers.objects.get(SSN=SSN)
        
        serializer = Dealers_serializer(get_list, data=request.data)
        if serializer.is_valid():
            get_list.Can_change_price=True #promoting the dealer to be able to sell and buy cars
            get_list.Can_sell_car=True
            get_list.Can_sign_contract=True
            get_list.save()
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
#buying a car

@api_view(['POST'])
def Add_Car(request, SSN, Name):
    try:
        get_dealer = Dealers.objects.get(SSN=SSN)
        get_industry= Industries.objects.get(Name=Name)

    except:
         return Response(status=status.HTTP_404_NOT_FOUND)
    if get_dealer.Can_sign_contract==False: #making sure that the dealer is promoted
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    contract_obj=Contract.objects.create()# a contract object
    Contract_ser= Contract_serializer(data=request.data)
    serializer = Cars_serializer(data=request.data)
    if serializer.is_valid() and Contract_ser.is_valid():
        serializer.save(Industries=get_industry, Contract=contract_obj)
        Contract_ser.save()
        
        get_dealer.Contract.add(contract_obj)#adding the contract done to get a car
        return Response(serializer.data and Contract_ser.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
@api_view(['POST'])
def Add_Industry(request):
    serializer = Industries_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#selling a car

@api_view(['POST'])   #adding a customer to the database
def Add_Customer(request,id):
    try:
        get_car = Cars.objects.get(id=id)
        

    except:
         return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = Customers_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Sell_Car(request,SSN, id):
    try:
        get_customer = Customers.objects.get(SSN=SSN)
        get_car = Cars.objects.get(id=id)
        
        serializer = Dealers_serializer(get_car, data=request.data)
        if serializer.is_valid():
                
            serializer.save(Customer=get_customer)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT']) #to dismiss a dealer and also keep his records in database
def Dismiss_Dealer(request, SSN):
    try:
        get_list = Dealers.objects.get(SSN=SSN)
        
        serializer = Dealers_serializer(get_list, data=request.data)
        if serializer.is_valid():
            get_list.IS_available= False
            get_list.save()
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
