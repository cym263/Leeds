import netCDF4
ds = netCDF4.Dataset("example_data/ggas2014121200_00-18.nc")
for v in ds.variables:
    print v,

sst = ds.variables["SSTK"]
print 'kkk',sst,

for d in sst.dimensions:
   print d, len(ds.variables[d])

   print sst.shape, sst.size

#for attr in sst.ncattrs():
#   print attr,




