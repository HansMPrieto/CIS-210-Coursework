'''
CIS 210 Project 8 Fall 2018

Author: Hans Prieto

Credits: N/A

Use file processing and data mining to
discover patterns of earthquake activity
around the world over the past year; plot
results on a world map.

Practice with
- data mining and file processing
- reading, understanding, and revising a
program that has mostly been already written.
'''

import math
import random
from turtle import*

def readFile(filename):
    '''
    (str) -> dict

    Returns a dictionary of earthquake
    latitudes and longitudes from a file
    of earthquake information.

    >>> readFile('earthquakes_short.txt')
    {1: [43.756, -125.815], 2: [42.2915, -122.0086667], 3: [42.3575, -122.0583333]}
    '''
    
    datafile = open(filename, "r")
    datadict = {}
    datafile.readline()
    key = 0
    
    for aline in datafile:
        items = aline.strip().split(',')
        key = key + 1
        lat = float(items[1])
        lon = float(items[2])
        datadict[key] = [lon,lat]
            
    return datadict

def euclidD(point1, point2):
    '''
    (list, list) -> float
    
    Computes the distance between
    two points, where each point is
    defined as a list of n coordinate values.

    >>> euclidD((3, 7), (1, 5))
    2.8284271247461903

    >>> euclidD((10, 8, 2), (1, 7, 5))
    9.539392014169456
    
    >>> euclidD((23, 44, 12, 76, 34), (67, 55, 85, 23, 24))
    101.46427942877237
    '''
    
    total = 0   #total is initalized to 0.
    for index in range(len(point1)):    #iterate through the coordinate list
        diff = (point1[index]-point2[index]) ** 2   #computes the square of the difference
        total = total + diff    #adds that value to the running total

    euclidDistance = math.sqrt(total)   #square root is computed
    return euclidDistance   #square root is returned

def createCentroids(k, datadict):
    '''
    (int, dict) -> list

    Implements the centroid selection process,
    where it creates a list of k randomly selected
    data points.

    Because we do not want to use a specific key
    twice, a list is stored for the selected keys,
    and each key is randomly checked against this list.

    If key is already in the list, its data point is not
    included as a centroid, and instead, continue on to
    pick another key randomly.

    Process continues until k centroids have been selected.

    >>> createCentroids(1, {1: [43.756, -125.815], 2: [42.2915, -122.0086667], 3: [42.3575, -122.0583333]})
    [[42.3575, -122.0583333]]

    >>> createCentroids(2, {1: [43.756, -125.815], 2: [42.2915, -122.0086667], 3: [42.3575, -122.0583333]})
    [[42.2915, -122.0086667], [42.3575, -122.0583333]]

    >>> createCentroids(1, {1: [43.756, -125.815], 2: [42.2915, -122.0086667]})
    [[42.2915, -122.0086667]]
    '''
    
    centroids = [] #creates an empty list of centroids.
    centroidCount = 0 #initial centroidCount
    centroidKeys = [] #empty list for centroidKeys
    
    while centroidCount < k: #goes through selection process until k centroids have been selected.
        rkey = random.randint(1, len(datadict)) #selects a random key from datadict.
        if rkey not in centroidKeys: #determines whether or not a key is already in the centroidKeys list.
            centroids.append(datadict[rkey]) #adds the data point of a certain key to the list of centroids.
            centroidKeys.append(rkey) #adds the key to the centroidKeys list. 
            centroidCount = centroidCount + 1 #centroidCount is incremented.

    return centroids #returns the list of centroids filled with k randomly selected data points.

def createClusters(k, centroids, datadict, repeats):
    '''
    (int, list, dict, int) -> list of lists

    Returns a list of clusters for the
    earthquake data for latitudes and longitudes.

    >>> createClusters(3, [[-84.0888, -41.4839], [141.5594, 32.4901],
    [144.8897, 38.0555], [45.5993, 34.9144], [73.9098,
    38.2556], [168.5847, -21.5194]], {1: [144.8897, 38.0555], 2: [45.5993,
    34.9144], 3: [45.9411, 34.8857], 4: [58.2176, 9.1259], 5: [168.5847, -21.5194],
    6: [-14.0995, -11.7482], 7:[168.4966, -21.4067], 8: [73.9098, 38.2556], 9:
    [129.9681, -7.0579], 10: [-84.0888, -41.4839], 11: [168.5912, -21.5266],
    12: [141.5594, 32]}, 3)
    [[6, 10], [2, 3, 4, 8], [1, 5, 7, 9, 11, 12]]
    '''
    
    for apass in range(repeats):
        #print("***PASS", apass, "****")
        clusters = []
        for i in range(k): 
            clusters.append([]) #creates the list of k clusters. 

        for akey in datadict:
            distances = [] #creates an empty list of distances.
            for clusterIndex in range(k):  
                dist = euclidD(datadict[akey], centroids[clusterIndex]) #compute the distance between datapoint and centroid.
                distances.append(dist) #appends that distance to the distances list.

            mindist = min(distances) #looks for the smallest value from the distances list.
            index = distances.index(mindist) #uses the list method index to find where the minimum occured in the distance list.

            clusters[index].append(akey) #uses index to access list of clusters and append key to the proper clusters.

        dimensions = len(datadict[1])
        for clusterIndex in range(k): #implements the centroid recalculation.
            sums = [0] * dimensions #sums represent a list of runing sums that include a sum for each dimension of the data point.
            #dimensions is the number of dimensions within the data point.
            
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)): #calculate the running sum of the components.
                    sums[ind] = sums[ind] + datapoints[ind]
                    
            for ind in range(len(sums)): #computes the average.
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind] / clusterLen

            centroids[clusterIndex] = sums #assigns the average to the proper position in the centroids list.

        #for c in clusters: #prints out the contents of the cluster after each pass.
            #print("CLUSTER")
            #for key in c:
                #print(datadict[key], end=" ")
            #print()

    return clusters

def eqDraw(k, eqDict, eqClusters):
    '''
    (int, dict, list of lists) -> None

    Plots the results of the clusters
    from the k-means analyis.

    >>> eqDraw(3, {1: [144.8897, 38.0555], 2: [45.5993,
    34.9144], 3: [45.9411, 34.8857], 4: [58.2176, 9.1259], 5: [168.5847, -21.5194],
    6: [-14.0995, -11.7482], 7:[168.4966, -21.4067], 8: [73.9098, 38.2556], 9:
    [129.9681, -7.0579], 10: [-84.0888, -41.4839], 11: [168.5912, -21.5266],
    12: [141.5594, 32]}, [[6, 10], [2, 3, 4, 8], [1, 5, 7, 9, 11, 12]])
    plots the clusters from a dictionary onto a world map.
    '''
    
    quakeWin = Screen()
    quakeWin.bgpic("worldmap1800_900.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    hideturtle()
    up()
    speed('fastest')


    colorlist = ["red", "green", "blue", "orange", "cyan", "yellow",
    "lime", "black", "purple", "turquoise", "navy", "gold",
    "brown", "grey", "pink", "olive", "apricot", "beige",
    "mint", "teal", "lavender"]

    for clusterIndex in range(k):
        color(colorlist[clusterIndex])
        for akey in eqClusters[clusterIndex]:
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            goto(lon*wFactor, lat*hFactor)
            dot()
    quakeWin.exitonclick()


def visualizeQuakes(k, r, dataFile):
    '''
    (int, int, file) -> None

    Calls the function eqDraw to
    plot the clusters from the
    k-means analysis to the
    world map.

    >>> visualizeQuakes(6, 7, 'earthquakes.txt')
    plots clusters of the file 'earthquakes.txt'
    on a world map
    '''
    
    datadict = readFile(dataFile) #creates a dictionary of earthquake latitudes and longitudes from an earthquake file.
    quakeCentroids = createCentroids(k, datadict) #creates centroids with a list of k randomly selected points.
    clusters = createClusters(k, quakeCentroids, datadict, r) #creates clusters for the earthquake data, which includes latitudes and longitudes.

    eqDraw(k, datadict, clusters) #plots the clusters on a world map.

    return None #None value is returned.

def main():
    '''
    Assigns values to k, r and
    f and calls the function
    visualizeQuakes to plot the clusters
    of the earthquake data on a world map.

    None value is returned.
    '''
    
    k = 6
    r = 7
    f = 'earthquakes.txt'
    visualizeQuakes(k, r, f)

    return None

main()


                
            
                    
