#!/usr/bin/env python
# coding: utf-8

# In[1]:


queue = {
    1:{}, 
    2:{},
    3:{},
    4:{},
    5:{}
}


# In[4]:


class Hospital:
    
    def __init__(self):
        self.name = input("Enter your name: ")
        self.spec = int(input("Enter Specialization 1-5: "))
        self.sta = int(input("Enter status 0-2: "))
        
    def specialization(self):
        if 0 < self.spec < 6:
            if -1 < self.sta < 3:
                for i in range(1,6):
                    if self.spec==i and len(queue[i])<10:
                        queue[i].update({self.name:self.sta})
                        
                        
                        queue[self.spec] = dict(sorted(queue[self.spec].items(), key=lambda item: item[1], reverse=True))
                        
                        
                        print(f"Specialization {self.spec}: {queue[i]}")
                    elif self.spec==i and len(queue[i])==10:
                        print(f"Specialization {self.spec} is full")
            else:
                print(f"Status-{self.sta} is out of range 0-2")
        else:
            print(f"Specialization {self.spec} does not exists")


# In[6]:


f = Hospital()
f.specialization()


# In[ ]:




