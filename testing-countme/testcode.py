import numpy as np
import math
import time
from matplotlib import pyplot as plt
from scipy.interpolate import griddata
import cv2
# from Adafruit_AMG88xx import Adafruit_AMG88xx
import requests
from bs4 import BeautifulSoup

# sensor = Adafruit_AMG88xx()
# num_requests = 20
# while(num_requests > 0):
# for i in range(1,20):
r = requests.get("http://192.168.1.101/xml")

soup = BeautifulSoup(r.content)
data_sensor = soup.prettify()
print("------------------------------------------")
print(data_sensor)
print("------------------------------------------")
	# pass

# Access an instance of Configuration
# config = channel.config()
# Start sensor

active = True

while(1):
	if active == True:
		# Read pixels, convert them to values between 0 and 1, map them to an 8x8 grid
		# pixels = sensor.readPixels()
		pixmax = max(data_sensor) #pixels
		data_sensor = [x / pixmax for x in data_sensor]
		points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
		grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

		# bicubic interpolation of 8x8 grid to make a 32x32 grid
		bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
		image = np.array(bicubic)
		image = np.reshape(image, (32, 32))
		print(image)
		plt.imsave('color_img.jpg', image)

		# Read image
		img = cv2.imread("color_img.jpg", cv2.IMREAD_GRAYSCALE)
		img = cv2.bitwise_not(img)

		# Setup SimpleBlobDetector parameters.
		params = cv2.SimpleBlobDetector_Params()

		# Change thresholds
		params.minThreshold = 10
		params.maxThreshold = 255

		# Filter by Area.
		params.filterByArea = True
		params.minArea = 5

		# Filter by Circularity
		params.filterByCircularity = True
		params.minCircularity = 0.1

		# Filter by Convexity
		params.filterByConvexity = False
		params.minConvexity = 0.87

		# Filter by Inertia
		params.filterByInertia = False
		params.minInertiaRatio = 0.01

		# Set up the detector with default parameters.
		detector = cv2.SimpleBlobDetector_create(params)

		# Detect blobs.
		keypoints = detector.detect(img)

		for i in range (0, len(keypoints)):
			x = keypoints[i].pt[0]
			y = keypoints[i].pt[1]
			print(x, y)

		# Get the channel setting for interval_ms
		interval = config.get("channel.interval_ms")
		interval = config.get("channel.active")
		# Report the device having set interval_ms
		config.set("channel.interval_ms", interval)
		config.set("channel.active", active)
		channel.send(str(len(keypoints)))
		time.sleep(interval)
		# time.sleep(5)

	else:
		print("idle")
		channel.send("Idle")
		time.sleep(5)
		interval = config.get("channel.active")
		config.set("channel.active", active)