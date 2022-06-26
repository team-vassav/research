import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections
import requests
import streamlit as st

def my_function(i):
    r = requests.get(
        'https://api.thingspeak.com/channels/1739457/feeds.csv?results=1')
    contents = r.text
    contents = contents.split("\n")
    x, y = contents[1][28:].split(',')
    # get data
    cpu.popleft()
    cpu.append(float(x))
    #ram.popleft()
    #ram.append(float(y))
    # clear axis
    ax.cla()
    #ax1.cla()
    # plot cpu
    ax.plot(cpu)
    ax.scatter(len(cpu) - 1, cpu[-1])
    ax.text(len(cpu) - 1, cpu[-1] + 2, "{}%".format(cpu[-1]))
    ax.set_ylim(0, 10)
    # plot memory
    #ax1.plot(ram)
    #ax1.scatter(len(ram) - 1, ram[-1])
    #ax1.text(len(ram) - 1, ram[-1] + 2, "{}%".format(ram[-1]))
    #ax1.set_ylim(0, 10)


# start collections with zeros
cpu = collections.deque(np.zeros(10))
#ram = collections.deque(np.zeros(10))
# define and adjust figure
fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
ax = plt.subplot(121)
#ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
#ax1.set_facecolor('#DEDEDE')
# animate
while True:
    ani = FuncAnimation(fig, my_function, interval=1000)
    #my_function()
    #plt.show()
    st.pyplot(fig)
