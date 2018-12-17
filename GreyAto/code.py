# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
path

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

data = np.genfromtxt(path, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census = np.concatenate((data,new_record),axis=0)

#Code starts here



# --------------
#Code starts here
from numpy import array

age = array(census[:,0],dtype='int')
print(age)
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()

print(max_age)
print(min_age)
print(age_mean)
print(age_std)



# --------------
#Code starts here
import numpy as np
from numpy import array

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

minority_race = 3


# --------------
#Code starts here

from numpy import array

senior_citizens = array(census[census[:,0]>60], dtype='int')
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens[:,6])
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)




# --------------
#Code starts here

high = array(census[census[:,1]>10],dtype='int')
low = array(census[census[:,1]<=10],dtype='int')

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_low/avg_pay_high)


