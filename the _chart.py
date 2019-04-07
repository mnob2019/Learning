import datetime
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 16


today = datetime.datetime.today().date()
num_days = 90
three_months = [today - datetime.timedelta(days=x) for x in range(num_days, 0, -1)]

y_data = sorted(list(np.random.rand(num_days)))

plt.plot(three_months, y_data, color='red', linestyle=':', linewidth=5)
plt.plot(three_months, sorted (y_data), color='black', label='tea')
plt.title("Random")
plt.legend(loc='upper left')
plt.ylabel("consumption")
plt.show()