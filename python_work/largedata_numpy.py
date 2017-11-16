import os
dir(os)
os.listdir('.')
with open('ecmwf_temp_2000_monthly_mean.dat') as reader:
     data = reader.read()
     print data



 

