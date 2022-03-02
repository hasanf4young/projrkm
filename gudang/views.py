from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib import messages
import json
import requests
from . models import Barang

'''

def index(request):
    yoko = requests.get('https://api.github.com/users/raybesiga')
    lisht = []
    lisht.append(yoko.json())
    cleanedData = []
    yokogaoData = {}
    for data in lisht:
        yokogaoData['name'] = data['name']
        yokogaoData['blog'] = data['blog']
        yokogaoData['email'] = data['email']
        yokogaoData['public_gists'] = data['public_gists']
        yokogaoData['public_repos'] = data['public_repos']
        yokogaoData['avatar_url'] = data['avatar_url']
        yokogaoData['followers'] = data['followers']
        yokogaoData['following'] = data['following']
        yokogaoData['location'] = data['location']
        yokogaoData['created_at'] = data['created_at']
        yokogaoData['updated_at'] = data['updated_at']
    cleanedData.append(yokogaoData)
    return render(request, 'yokogao/index.html', {'data': yokogaoData})







{
  "data": {
     "current_condition": [{
        "cloudcover": "0",
        "humidity": "54",
        "observation_time": "08:49 AM",
        "precipMM": "0.0",
        "pressure": "1025",
        "temp_C": "10",
        "temp_F": "50",
        "visibility": "10",
        "weatherCode": "113",
        "weatherDesc": [{
            "value": "Sunny"
        }],
        "weatherIconUrl": [{
            "value": "http:\/\/www.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0001_sunny.png"
        }],
        "winddir16Point": "E",
        "winddirDegree": "100",
        "windspeedKmph": "22",
        "windspeedMiles": "14"
    }]        
 }
}
wjdata = requests.get('url').json()
print wjdata.get('data').get('current_condition')[0].get('temp_C')

json_dict = json.loads(json_str)
for domain_dict in json_dict['sip_domains']['domain']:
  print 'domain : %s' % (domain_dict['name'])


	result  = {
		"sip_domains":{
		    "prefix":[{"name":""}],
		    "domain":[{"name":"k200.com"},{"name":"Zinga.com"},{"name":"rambo.com"}]
		},
		"sip_security":{"level":2},
		"sip_trusted_hosts":{"host":[]},
		"sip_proxy_mode":{"handle_requests":1}
	}

	from this i just wanted the output to print to my screen :

	domain : k200.com 
	domain : Zinga.com 
	domain : rambo.com 

    json_dict = json.loads(json_str)
    for domain_dict in json_dict['sip_domains']['domain']:
        print 'domain : %s' % (domain_dict['name'])

'''

def tbdata(request):
    data_barang = Barang.objects.all()
    return render(request, 'gudang/vtable.html',{'tbl_barang':data_barang})

def vdata(request):
    data = requests.get('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
    content = data.json()
    
    ls = []
    for a in content['members']:
        ls.append(a)
    print(ls)
    return render(request, 'gudang/vdata.html',{'content': ls })
