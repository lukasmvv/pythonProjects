# see https://matplotlib.org/tutorials/index.html


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
	
	
import numpy as np
from matplotlib import pyplot as plt

#fig = plt.figure()  # an empty figure with no axes
x = np.arange(0, 4*np.pi, 0.02)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x-np.pi)
y4 = np.cos(x-np.pi)
fig, ax = plt.subplots()
ax.plot(x, y1)
plt.show()


fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is 
#ax_lst[0][0].plot(x,y1)
#ax_lst[0][1].plot(x,y2)
#ax_lst[1][0].plot(x,y3)
#ax_lst[1][1].plot(x,y4)
my_plotter(ax_lst[0][0],x,y1,{'marker': 'x'})
my_plotter(ax_lst[0][1],x,y2,{'marker': 'x'})
my_plotter(ax_lst[1][0],x,y3,{'marker': 'x'})
my_plotter(ax_lst[1][1],x,y4,{'marker': 'x'})


hist = plt.figure()









plt.show()