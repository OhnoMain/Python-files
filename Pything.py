import matplotlib.pyplot as plt
 
volume = [15, 14, 13, 12, 11, 10, 9, 8]
temp1 = [396, 370, 345, 317, 291, 265, 239, 213]
temp2 = [396, 370, 345, 317, 291, 264, 239, 213]
mean = [396, 370, 345, 317, 291, 264.5, 239, 213]
 
plt.plot(volume, temp1, label='Temp (K) 1')
plt.plot(volume, temp2, label='Temp (K) 2')
plt.plot(volume, mean, label='Mean', linestyle='--')
 
plt.xlabel('Volume (nm³)')
plt.ylabel('Temperature (K)')
plt.title('Temperature vs. Volume')
plt.legend()
plt.show()
