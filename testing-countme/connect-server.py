import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt


num_requests = 20
while(num_requests > 0):
# for i in range(1,20):
	r = requests.get("http://192.168.5.206/xml")
	#192.168.5.206

	soup = BeautifulSoup(r.content)
	data_sensor = soup.prettify()

	print("------------------------------------------")
	print(data_sensor)
	# print("")
	# newdata = np.squeeze(data_sensor) # Shape is now: (10, 80)
	# plt.plot(newdata) # plotting by columns
	# plt.show()
	print("------------------------------------------")


	
	pass

# result = s.recv(4096)


