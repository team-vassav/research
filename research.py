import requests
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

while True:
	r = requests.get('https://api.thingspeak.com/channels/1739457/feeds.csv?results=1')
	#pprint.pprint(r.text)
	contents = r.text
	contents = contents.split("\n")
	data = {}
	for i in range(1,len(contents)-1):
		points = contents[i][28:]
		data[float(points[:3])] = float(points[4:])
	#print(data)
	data = pd.DataFrame(list(data.items()),columns = ['column1','column2']) 
	
	#st.dataframe(data[:10])
		
	st.line_chart(data)
