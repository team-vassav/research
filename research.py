import requests
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate():
	r = requests.get('https://api.thingspeak.com/channels/1739457/feeds.csv?results=1')
	contents = r.text
	contents = contents.split("\n")
	x,y = contents[1][28:].split(',')
	plt.scatter(float(x), float(y), linewidth=4.0)
	time.sleep(5)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
