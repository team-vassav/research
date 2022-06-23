import requests
import streamlit as st
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

import time
from random import randint
from matplotlib.animation import FuncAnimation

'''while True:
	r = requests.get('https://api.thingspeak.com/channels/1739457/feeds.csv?results=1')
	contents = r.text
	contents = contents.split("\n")
	x,y = contents[1][28:].split(',')
	plt.scatter(float(x), float(y), linewidth=4.0)
	time.sleep(5)
	st.pyplot(fig=plt, clear_figure=True)
ani = animation.FuncAnimation(fig, animate, interval=1000)'''

'''x = []
y = []

fig, ax = plt.subplots()

def animate(i):
    pt = randint(1,9)
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,100])
    ax.set_ylim([0,10])

ani = FuncAnimation(fig, animate, frames=100, interval=500, repeat=False)

plt.show()'''

x=1
plt.ylim(1,8)
plt.xlim(1,8)

while True:
	y = randint(1,9)
	x += 1
	plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
	time.sleep(1)
	st.pyplot(fig=plt, clear_figure=True)
