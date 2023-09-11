from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import  CreateAPIView

from .serializers import Transfers,TransferSerializer
from apps.transfers.models import User

class TransferView(CreateAPIView):
    serializer_class = TransferSerializer
    def post(self, request):
        who_transfer_id = request.data.get('who_transfer')
        who_get_id = request.data.get('who_get')
        how_much = request.data.get('how_much')
        try:
            who_transfer = User.objects.get(id=who_transfer_id)
            who_get = User.objects.get(id=who_get_id)
            if float(how_much) > float(who_transfer.balance):
                return Response({'detail': 'Недостаточно средств для перевода'}, status=status.HTTP_400_BAD_REQUEST)
            who_transfer.balance = float(who_transfer.balance) - float(how_much)
            who_get.balance = float(who_get.balance) + float(how_much)
            who_transfer.save()
            who_get.save()
            transfer = Transfers.objects.create(who_transfer=who_get, who_get=who_get, how_much=how_much)
            serializer = TransferSerializer(transfer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'detail': 'Неверный формат суммы перевода'}, status=status.HTTP_400_BAD_REQUEST)
