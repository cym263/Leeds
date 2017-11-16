import os
dir(os)
os.listdir('.')
# with open('cym02_python.txt') as reader:
# data = reader.read()

def process_dir(dr):
#  with open(fname) as reader:  
# print len(reader.read())
  for fname in os.listdir(dr):
#  process_file(fname)
#  print fnameprocess_file(fname)
     if os.path.isfile(fname) and fname.endswith('.txt'):
         print fname

     #return process_file(fname)


process_dir(".")

