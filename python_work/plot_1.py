
import matplotlib.pyplot as plt
times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', label = "Some data")
plt.plot(times, [1, 2, 3, 4],  'r', label = "Other data")
plt.title('Concentration of Chlorine vs Time')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.legend(loc=2)
plt.show()
plt.savefig("myplot.png")