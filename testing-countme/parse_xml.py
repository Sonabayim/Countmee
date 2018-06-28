import numpy as np
import xml.etree.ElementTree as ET
from collections import defaultdict
import requests
import xmltodict
# import urllib2

# import urllib2

import urllib.request
url = "http://api.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id&start=1&rows=100"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')
# print (data)

# def homepage(request):
#     file = urllib2.urlopen('https://www.goodreads.com/review/list/20990068.xml?key=nGvCqaQ6tn9w4HNpW8kquw&v=2&shelf=toread')
#     data = file.read()
#     file.close()

#     data = xmltodict.parse(data)
#     return render_to_response('my_template.html', {'data': data})




# r = urllib2.urlopen("http://192.168.1.101/xml")
# data = r.read()
# r.close()
root = ET.parse(data).getroot()
# data = xmltodict.parse(data)

# data = defaultdict(list)

# group into rows of (col, val) tuples
for val in root.iter('Value'):
	data[int(val.attrib['Row'])].append((int(val.attrib['Col']), val.text))

# sort columns and format into a space separated string
rows = []
for row in data:
	rows.append(' '.join([cols[1] for cols in sorted(data[row])]))

# build array from matrix string
matrix = np.array(np.mat(';'.join(rows)))

