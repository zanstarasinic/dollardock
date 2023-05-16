from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    # Retrieve the user's authentication token
    token = Token.objects.get(user=request.user)

    # Delete the token to log out the user
    token.delete()

    return Response({'message': 'Logout successful'})

@api_view(['POST'])
def register_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_account(request):
    # Retrieve the user's account
    try:
        account = Account.objects.get(owner=request.user)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_account_transactions(request, account_id):
    try:
        account = Account.objects.get(id=account_id, owner=request.user)
        transactions = Transaction.objects.filter(account=account)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({'message': 'Transanctions not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_transaction(request, account_id):
    account = Account.objects.get(id=account_id)
    data = request.data.copy()  # Make a copy of the request data
    data['account'] = account.id  # Set the account ID in the data
    # Create a new transaction associated with the account
    serializer = TransactionSerializer(data=data)
    if serializer.is_valid():
        # Set the account field of the transaction to the retrieved account
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)