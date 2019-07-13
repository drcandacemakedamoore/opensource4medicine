#example of a simple pie chart maker in python
import matplotlib.pyplot as plt

labels = 'type A', 'type B', 'type C', Type D', 'Type E'
#sizes will be % of pie, so here A is 7, B is 30...
sizes = [7, 30, 45, 10, 8]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
