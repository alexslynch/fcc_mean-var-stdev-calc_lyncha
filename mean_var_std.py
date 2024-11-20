import numpy as np
from regex import R

def calculate(l):
    #check 'l' for number of elements
    temp = []
    for i in range(9):
         temp.append("")
    for i in range(len(l)):
          temp[i] = l[i]
    l = temp
    #print("l = ", l)
    #print("The type of 'list' is: ", type(l))
    try:
        for elem in l:
            numbercheck = float(elem)
    except:
            raise ValueError("List must contain nine numbers.")
    
    #create 3x3 array
    a = np.array([[l[0], l[1], l[2]],
                  [l[3], l[4], l[5]],
                  [l[6], l[7], l[8]]])
    # print("3x3 array = ", a)
    #initialize results dictionary
    calculations = {}
    
    # axis1 = np.array([a[:,0], a[:,1], a[:,2]]) 
    # axis2 = np.array([a[0,:], a[1,:], a[2,:]])

    #compute mean
    axis1means = np.mean(a, axis=0).tolist()
    #print("The type of {axis1means} is ", type(axis1means))
    axis2means = np.mean(a, axis=1).tolist()
    flattenedmeans = np.mean(a).tolist()
    calculations.update({'mean':[axis1means, axis2means, flattenedmeans]})

    #compute variance
    axis1var = np.var(a, axis=0).tolist()
    axis2var = np.var(a, axis=1).tolist()
    flattenedvar = np.var(a)
    calculations.update({'variance':[axis1var, axis2var, flattenedvar]})

    #compute standard deviation
    axis1stdev = np.std(a, axis=0).tolist()
    axis2stdev = np.std(a, axis=1).tolist()
    flattenedstdev = np.std(a)
    calculations.update({'standard deviation':[axis1stdev, axis2stdev, flattenedstdev]})

    #compute max
    axis1max = np.max(a, axis=0).tolist()
    axis2max = np.max(a, axis=1).tolist()
    flattenedmax = np.max(a)
    calculations.update({'max':[axis1max, axis2max, flattenedmax]})

    #compute min
    axis1min = np.min(a, axis=0).tolist()
    axis2min = np.min(a, axis=1).tolist()
    flattenedmin = np.min(a)
    calculations.update({'min':[axis1min, axis2min, flattenedmin]})

    #compute sum
    axis1sum = np.sum(a, axis=0).tolist()
    axis2sum = np.sum(a, axis=1).tolist()
    flattenedsum = np.sum(a)
    calculations.update({'sum':[axis1sum, axis2sum, flattenedsum]})


    return calculations