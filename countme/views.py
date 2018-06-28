from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import urllib.request
import xmltodict
from django.shortcuts import render_to_response



def homepage(request):
	file = urllib.request.urlopen('http://192.168.5.211/xml')
	data = file.read()
	file.close()

	data = xmltodict.parse(data)
	
	length = len(data['response'])
	# print(data['response'])
	# print(data['response'])
	DATA = data['response']
	# DATA = [0] * length
	# some = 0
	# for x in range(0,length):
	# 	DATA[some] = list(data['response'])
	# 	DATA[some] = ''.join(DATA[some])
	# 	some = some + 1
	# print(DATA)

	# for x in data:


	# print(data['response']['result']['doc'])
	# data = data['response']['result']['doc']
	# print('--------------------------------')


	# return render_to_response('my_template.html', {'data': data})
	return render(request,'my_template.html', {'data': DATA})

# User = get_user_model()

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'chart.html', {"customers": 10})

# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'main.html', {})        



# def get_data(request, *args, **kwargs):
#     data = {
#         "sales": 100,
#         "customers": 10,
#     }
#     return JsonResponse(data) # http response


# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         qs_count = User.objects.all().count()
#         labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         default_items = [qs_count, 23, 2, 3, 12, 2]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)
