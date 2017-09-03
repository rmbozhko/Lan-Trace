import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# data to plot
bus_name = str(['bus-09-85'])
days = ('27-08-2017', '28-08-2017', '29-08-2017', '30-08-2017', '31-08-2017', '1-09-2017', '2-09-2017')
days = [dt.datetime.strptime(d,'%d-%m-%Y').date() for d in days]

unique_conn = [138, 170, 164, 101, 0, 0, 0]
total_conn = [232, 258, 265, 141, 0, 0, 0]
plt.xlabel('Дата')
plt.ylabel('К-сть підключень')
plt.title('Кількість підключень автобуса: ' + bus_name[bus_name.index('s') + 2 : bus_name.index(']') - 1])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(days, total_conn, color="#3182bd", linewidth=2.5, label="Заг. к-сть підключень")
plt.plot(days, unique_conn, color="#cccccc",  linewidth=2.5, linestyle="--", label="Унк. підключення")
plt.gcf().autofmt_xdate()
plt.legend(loc='upper right')
plt.savefig('bar_chart_1.png')

'''
import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
bus_name = str(['bus-09-85'])
days = ['27', '28', '29', '30', '31', '1', '2']
#unique_conn = [138, 170, 164, 101, 0, 0, 0]
#total_conn = [232, 258, 265, 141, 0, 0, 0]
unique_conn = [138, 170, 164, 101, 144, 181, 125]
total_conn = [232, 258, 265, 141, 224, 241, 189]
n_groups = len(days)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 1#0.8
 
rects1 = plt.bar(index, unique_conn, bar_width,
                 alpha=opacity,
                 color='#3182bd',
                 label='Унк. підключення')
 
rects2 = plt.bar(index + bar_width, total_conn, bar_width,
                 alpha=opacity,
                 color='#cccccc',
                 label='Заг. к-сть підключень')
 
plt.xlabel('Дата')
plt.ylabel('К-сть підключень')
plt.title('Кількість підключень автобуса: ' + bus_name[bus_name.index('s') + 2:bus_name.index(']') - 1])
plt.xticks(index + bar_width, days)
plt.legend()
 
plt.tight_layout()
plt.savefig('bar_chart_1.png')
'''