import requests
#import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

while True:
	r = requests.get('https://api.thingspeak.com/channels/1739457/feeds.csv?results=1')
	contents = r.text
	contents = contents.split("\n")
	x,y = contents[1][28:].split(',')
	'''f = plt.figure()
	f.set_figwidth(4)
	f.set_figheight(1)'''
	
	plt.scatter(float(x), float(y), linewidth=4.0)
	plt.show()
