"""This is a program/script i wrote because i was faced with a situation at work
where i needed to identify ports with a registration failure and then manually lock them.
so this program takes its input as a text.txt file in the format below
    3     1/1/2/3   1539        pstn down         unlocked on-hook          no-testing  registrationfailure       
    3     1/1/2/27  1563        pstn down         unlocked on-hook          no-testing  registrationfailure  
and then outputs a file with the data formated in the following formated
     configure voice cluster 8 equipment 'logical number'  termination 'isam'  admin-status locked
e.g  configure voice cluster 8 equipment 3 termination 1/1/2/3  admin-status locked
"""

fin = open('text.txt')
fout = open('formatted.txt', 'w')

entries = []


for line in fin:
  entries.append(line.split())
  

for entry in entries:
  if entry == [] :
    continue
  if entry[0] == '3' or entry[0] == '2' or entry[0] == '1':
    fout.write(" configure voice cluster 8 equipment %s  termination %s  admin-status locked \n" % (entry[0], entry[1]))
    


fin.close()
fout.close()

  



  
