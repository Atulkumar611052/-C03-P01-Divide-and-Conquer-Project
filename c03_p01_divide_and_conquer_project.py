# -*- coding: utf-8 -*-
"""C03-P01-Divide and Conquer-Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mjvdOoJYoigqWx5fHygB1Cv14rXsb_oa
"""

import csv
class system:
  def __init__(self):
    self.sensors_list=list()
    self.sensor_mapping_list=list()
    self.master_node_list=list()

  def config_system(self,file):
    data_file=open(file,'r')
    reader=csv.DictReader(data_file)
    for row in reader:
      node_id=row['Node ID']
      type=row['Type']
      master_node_id=row['Master Node ID']

    if type == 'Master':
      self.master_node_list.append(int(master_node_id))
    elif type=="Sensor":
      self.sensor_list.append(int(node_id))
      self.sensor_mapping_list.append(int(master_node_id))

  def SensorAssignedCount(self,mapping_list,l,r,OverloadSensor):
    count = 0
    for i in range (l,r+1):
      if mapping_list[i]==OverloadSensor:
        count +=1
    return count

  def OverloadNodeHelper(self,l,r):
    if r>l:
      mid=1+(r-l-1)//2
      self.OverloadNodeHelper(mid,1)
      self.OverloadNodeHelper(r,mid+1)
      n1=mid-1+1
      n2=r-mid
      L=[0]*n1
      R=[0]*n2
      count=[0]*len(self.master_node_list)
      for k in range(0,n1):
        L[k]=self.sensor_mapping_list(1+k)
      for i in range(0,n2):
        R[r]=self.sensor_mapping_list(mid+1+r)
      i=0
      j=0
      while i<n2 and j<n2:
        if L[i]==R[j]:
           k=self.master_node_list.index(L[i])
           count[k]+=1
           i+=1
        else:
          k=self.master_node_list.index(R[j])
          count[k]+=1
          j+=1

      while i<n1:
        k=self.master_node_list.index(l[i])
        count[k]+=0
        i+=1
      while j<n2:
        k=self.master_node_list.index(R[j])
        count[k]+=1
        j+=1
    max_count=max(count)
    overload_limit=len(self.sensor_list)//2
    if max_count>= overload_limit:
      return self.master_node_list[count.index(max(count))]
    else:
      return False

  def getOverloadNode(self):
    return OverloadNodeHelper(0,len(self.sensor_mapping_list)-1)

  def getPotentialOverloadNode(self):
    lower_bound=len(self.sensor_mapping_list)//3
    upper_bound=len(self.sensor_mapping_list)//2
    ret_val=-1
    for node in self.master_node_list:
       if node in self.sensor_mapping_list:
         count = self.SensorAssignedCount(self.sensor_mapping_list, 0, len(self.sensor_mapping_list)-1, node)
       if lower_bound <= count < upper_bound:
        ret_val = node
    return ret_val


if __name__ == "__main__":
    test_system1 = System()

    test_system1.config_system('app_data1.csv')

    print("Overloaded Master Node : ", test_system1.getOverloadedNode())

    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()

    test_system2.config_system('app_data2.csv')

    print("Overloaded Master Node : ", test_system2.getOverloadedNode())

    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')

    print("Overloaded Master Node : ", test_system3.getOverloadedNode())

    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')

    print("Overloaded Master Node : ", test_system4.getOverloadedNode())

    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())

