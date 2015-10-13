import matplotlib.pyplot as pyplot

s_frac = 0.1
p_max = 128

speed_up = []
efficiency = []

for i in range(1, p_max + 1):
	cur_speedup = 1 / (s_frac + ((1 - s_frac) / i))
	speed_up.append(cur_speedup)
	efficiency.append(cur_speedup/i)

p_limits = [i for i in range(1, p_max + 1)]

pyplot.plot(p_limits,speed_up)
pyplot.title('Speedup vs Processors - Amdahl\'s Law')
#pyplot.show()
pyplot.savefig('speedup.png')
pyplot.close()
pyplot.plot(p_limits,efficiency)
pyplot.title('Efficiency vs Processors - Amdahl\'s Law')
#pyplot.show()
pyplot.savefig('efficiency.png') 