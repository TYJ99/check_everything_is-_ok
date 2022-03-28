#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def checkCodeword(x,H):
    for i in range(H.shape[0]):
    #print(H[i]&x)
        if(np.sum(H[i,:]&x)%2==1):
            return False
    return True;
    H = np.asarray(([1,0,0,0,1,1,1,0,0,0,1,1,1,0,1],
    [0,1,0,0,1,0,0,1,1,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1,1,0,1,1,1],
    [0,0,0,1,0,0,1,0,1,1,0,1,1,1,1]))
    x1 = np.asarray([1,1,1,1,1,1,1,0,0,1,0,0,0,0,0]).transpose()
    x2 = np.asarray([1,0,0,1,1,0,0,1,0,1,0,0,0,0,0]).transpose()
    x3 = np.asarray([1,0,0,0,1,0,0,0,0,0,0,0,0,0,1]).transpose()
    print(checkCodeword(x1,H))
    print(checkCodeword(x2,H))
    print(checkCodeword(x3,H))


# In[2]:


def buildTable(H):
    shape = H.shape
    E = np.zeros((shape[1],shape[1]+1),dtype = int)
    E[:shape[1],:shape[1]] = np.eye(shape[1])
    S = np.zeros((shape[0],shape[1]+1),dtype=int);
    for i in range(shape[0]):
        for j in range(shape[1]+1):
            S[i,j] = np.sum(H[i,:]&E[:,j])%2
    return E,S


# In[3]:


import copy
def channelDecode(r):
    E,S = buildTable(H)
    s = np.zeros((H.shape[0],1),dtype = int)
    for i in range(H.shape[0]):
        s[i] = np.sum(H[i,:].transpose()&r)%2
        x = copy.deepcopy(r);
        for i in range(H.shape[1]+1):
            if(np.sum((S[:,i,np.newaxis]-s)**2)==0):
                x ^= E[:,i]
                return E[:,i],x
    return np.zeros_like(E[0]),r #this line will not reach


# In[4]:


x = np.asarray([1,1,1,1,1,0,0,0,0,1,0,0,0,0,0]).transpose()
def test1bit(x):
    count = 0
    for i in range(x.shape[0]):
        r = copy.deepcopy(x)
        r[i]^=1
        e,rec_x = channelDecode(r)
    ### if not recover succed
        if(np.array_equal(rec_x,x)):
            count+=1
    return count


# In[5]:


x = np.asarray([1,1,1,1,1,0,0,0,0,1,0,0,0,0,0]).transpose()
def test2bit(x):
    count = 0
    for i in range(x.shape[0]-1):
        for j in range(i+1,x.shape[0]):
            r = copy.deepcopy(x)
            r[i]^=1
            r[j]^=1
            e,rec_x = channelDecode(r)
            if(np.array_equal(rec_x,x)):
                count+=1
    return count


# In[ ]:




