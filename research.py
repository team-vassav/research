import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import time

fig, ax = plt.subplots()

while True:
	r = requests.get('https://api.thingspeak.com/channels/1739457/feeds.csv?results=1')
	contents = r.text
	contents = contents.split("\n")
	x,y = contents[1][28:].split(',')
	plt.scatter(float(x), float(y), linewidth=4.0)
	st.pyplot(fig)
	time.sleep(5)
