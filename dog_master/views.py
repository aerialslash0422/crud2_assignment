import json

from django.views import View
from django.http import JsonResponse

from dog_master.models import Owner, Dog


class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Owner.objects.create(
            name     = data['name'],
            email    = data['email'],
            age      = data['age']
        )
        return JsonResponse({"message" : "SUCCESS"}, status = 201)
    
    def get(self, request):
        owners = Owner.objects.all()
        result = []
        for owner in owners:
            result.append(
                {
                'name'  : owner.name,
                'email' : owner.email,
                'age' : owner.age
                }
            )
            
        return JsonResponse({"owners" : result}, status=200)

class OwnerWithDogView(View):
    def get(self,request):
        owners = Owner.objects.all()
        
        result = []
        
        for owner in owners:
            dogs_list = [
                {'dog_name':dog.name} for dog in Dog.objects.filter(owner_id=owner.id)
                        ]
            # 리스트 컴프리헨션 사용
            # filter method를 통해서 dogs와 owner.id 연결(if문을 사용하는 것이 아니다)
            result.append(
                {
                    'name'  : owner.name,
                    'email' : owner.email,
                    'age' : owner.age,
                    'dogs' : dogs_list
                }
            )
            
        return JsonResponse({"MESSAGE" : result}, status=200)
        

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Dog.objects.create(
            owner = Owner.objects.get(name=data["owner"]), #
            name     = data["name"],
            age      = data["age"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status = 201)
    
    def get(self,request):
        dogs = Dog.objects.all()
        result = []
        for dog in dogs:
            
                result.append(
                    {
                    'dog_name' : dog.name,
                    'dog_age' : dog.age,
                    'owner' : dog.owner.name # dog.owner.name 외부키 가져옴
                    }
            )
            
        return JsonResponse({"dogs" : result}, status=200)