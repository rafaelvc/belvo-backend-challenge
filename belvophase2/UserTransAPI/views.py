from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, UsersAgeSerializer, TransactionsSerializer
from .models import User, Transactions
from django.db.models import Sum
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

@api_view(['GET'])
def user_age_sum(request):
    instance = User.objects.aggregate(Sum('age'))
    serializer = UsersAgeSerializer(instance)
    return Response(serializer.data)

@api_view(['POST'])
def transactions_bulk_create(request):
    transactions = request.data
    serializer = TransactionsSerializer(data=request.data, many=True)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_transactions_balance(request):
    """
    """
    try:
        user_id = request.query_params.get('user_id', None)
        if user_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_trans = Transactions.objects.filter(user_id=user_id)

        date_begin = request.query_params.get('date_begin', None)
        date_end = request.query_params.get('date_end', None)
        if date_begin and date_end:
            date_begin = datetime.strptime(date_begin, "%Y-%m-%d")
            date_end = datetime.strptime(date_end, "%Y-%m-%d")
            user_trans = user_trans.filter(date__range=[date_begin, date_end])

        inflow_trans = user_trans.filter(type="inflow")
        outflow_trans = user_trans.filter(type="outflow")

        inflow_by_account = inflow_trans.values('account').annotate(total_inflow=Sum('amount')).order_by()
        outflow_by_account = outflow_trans.values('account').annotate(total_outflow=Sum('amount')).order_by()

        output = []
        for acc in inflow_by_account:
            entry = {}
            entry["account"] = acc['account']
            outflow_account = outflow_by_account.filter(account=acc['account'])
            outflow = 0
            if len(outflow_account) > 0:
               outflow = outflow_account[0]['total_outflow'] 
            entry["balance"] = acc['total_inflow'] + outflow
            entry["total_inflow"] = acc['total_inflow']
            entry["total_outflow"] = outflow
            output.append( entry )

    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(output)

@api_view(['GET'])
def user_transactions_category(request):
    """
    """
    try:
        user_id = request.query_params['user_id']
        if user_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_trans = Transactions.objects.filter(user_id=user_id)

        inflow_trans = user_trans.filter(type="inflow")
        outflow_trans = user_trans.filter(type="outflow")

        # import pdb; pdb.set_trace()
        inflow_by_category = inflow_trans.values('category').annotate(Sum('amount')).order_by()
        outflow_by_category = outflow_trans.values('category').annotate(Sum('amount')).order_by()

        output = {"inflow" : {}, "outflow" : {}}
        for category in inflow_by_category:
            output["inflow"][category['category']] = category['amount__sum']

        for category in outflow_by_category:
            output["outflow"][category['category']] = category['amount__sum']
    
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(output)
