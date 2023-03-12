import matplotlib.pyplot as plt # Import the matplotlib.pyplot module
x = (-3,-1,0,3,3) # Make some data, x- and y-values
y = (0,-2,0,-1,2)
plt.plot(x,y, ls="-", c="red") # Plot line graph of x and y
plt.plot(x,y, "b*")
plt.title("Sketch of the Cassiopeia star constalation") # Set the title of the graph
plt.xlabel("relative x value from center star") # Set the x-axis label
plt.ylabel("relative y value from center star") # Set the y-axis label
plt.xlim([-4, 4]) # Set the limits of the x-axis
plt.ylim([-3, 3]) # Set the limits of the y-axis
plt.grid()
plt.show()

