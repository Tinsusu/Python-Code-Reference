import numpy as np
import random
import handin5_project
anomaly_data = np.genfromtxt("Land_and_Ocean_summary.txt",comments='%')
#anomaly_data = anomaly_data.astype('object')
#anomaly_data[:,0] = anomaly_data[:,0].astype('int')
#anomaly_data[:,0] = anomaly_data[:,0].astype('str') #convert type of the first column
#print(anomaly_data[:,1])
#normalize data to be between 0 -1
#anomaly_data = anomaly_data[:,1] #"Land + Ocean anomaly using air temperature above sea ice"
normalize_data = (anomaly_data[:,1] - np.min(anomaly_data[:,1])) / (np.max(anomaly_data[:,1]) - np.min(anomaly_data[:,1]))
#print(normalize_data)

color_mapper = handin5_project.ColorMapper(normalize_data)

#print(color_mapper.get_color(0))
#print(color_mapper.get_color(0.5))
#print(color_mapper.get_color(1))

rectangles = handin5_project.construct_rectangles(anomaly_data[:,0],anomaly_data[:,1])


#print(rectangles)
plot = handin5_project.plot_stripes(rectangles,color_mapper)



