import matplotlib.pyplot as plt

# adjust file_to_read value if your txt file has a different name
file_to_read = 'data/10-4-Experiment-complete.txt'
custom_csv_file_name = 'experiment_file.csv'

time_header_idx, temp_header_idx, mass_header_idx = 0, 7, 1

# read data
f = open(file_to_read,'r')
headers = f.readline().split(',')

f.readline() # skip the first line with different timestamp
data = []
time = []
temp = []
mass = []
for row in f:
    row = row.split(',')
    if (len(row) == len(headers) + 1):
        # timestring = row[time_header_idx]
        # pt = datetime.strptime(timestring,'%H:%M:%S')
        # time.append(pt)
        time.append(row[time_header_idx])
        temp.append(float(row[temp_header_idx]))
        mass.append(float(row[mass_header_idx]))

# plot temperature
fig, ax = plt.subplots()
ax.plot(time, temp, color = 'red', marker="o", label = 'Temperature Data')
  
ax.set_xlabel('Time', fontsize = 12)
ax.set_ylabel('Temperature (C)', color="red", fontsize = 12)

# adjust this spacing if x axis labels are too cluttered or sparse
spacing = 25
plt.xticks(rotation=90)
visible = ax.xaxis.get_ticklabels()[::spacing]
for label in ax.xaxis.get_ticklabels():
    if label not in visible:
        label.set_visible(False)
  
# plot mass
ax2=ax.twinx()
ax2.plot(time, mass, color="blue", marker="o")
ax2.set_ylabel("Mass (kg)", color="blue", fontsize=14)

plt.title('Time vs Temperature and Mass', fontsize = 16)
plt.show()

# save the plot as a file
fig.savefig('timeVsTempAndMass.png',
            format='png',
            dpi=100,
            bbox_inches='tight')