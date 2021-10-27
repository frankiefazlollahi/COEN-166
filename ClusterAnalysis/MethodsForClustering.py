# this file contains methods that each of the clustering algorithms use

from math import *
import csv


def print_clustering(clusters):
    print("New Clustering:")
    for cluster in clusters:
        cluster.sort()
        for data_point in cluster:
            print(data_point)
        print("=========================================================================================")


# returns euclidean distance between data points a and b
def edistance(a, b):
    sum = 0
    # accumulating the sum of differences squared
    for i in range(1, (len(a) - 1)):
        sum = sum + (float(a[i]) - float(b[i]))**2
    return sqrt(sum)


#works for files named "name.data"
#opens file & returns list of each data point's data & a list of what will be our cluster list
def open_file(filename):
    mark = ','
    with open(filename + ".data", newline='') as file:
        reader = csv.reader(file, delimiter=mark)
        data = list(reader)
    # delete last data point if it was made from an empty line at end of file
    if len(data[len(data) - 1]) == 0:
        del(data[len(data) - 1])
    clusters = list()
    for i in range(0, len(data)):
        d = data[i]
        # moving the classification (first element of the line) to the end for consistency
        if filename == "balance-scale" or filename == "wine":
            d.append(d[0])
        if filename == "glass" or filename == "balance-scale" or filename == "wine":
            del d[0]
        #giving each data point an ID (just the number of the line they came from in the respective file)
        d.insert(0, i)
        new_list = list()
        new_list.append(d)
        clusters.append(new_list)
    return data, clusters


# goes through every point and checks whether it is in a particular cluster or out of the cluster in each clustering,
# and returns the total number of disagreements divided by total number of edges
def hamming_distance(data, clustering1, clustering2):
    h1, h2 = 0, 0
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            cluster1, cluster2, cluster3, cluster4 = -1, -1, -1, -1
            # for each data point, see if it is in clustering1's x cluster
            for x in range(0, len(clustering1)):
                for data_point in clustering1[x]:
                    if data_point[0] == data[i][0]:
                        cluster1 = x
                    if data_point[0] == data[j][0]:
                        cluster2 = x
                    if cluster1 != -1 and cluster2 != -1:
                        break
            # for each data point, see if it is in clustering2's x cluster
            for x in range(0, len(clustering2)):
                for data_point in clustering2[x]:
                    if data_point[0] == data[i][0]:
                        cluster3 = x
                    if data_point[0] == data[j][0]:
                        cluster4 = x
                    if cluster3 != -1 and cluster4 != -1:
                        break
            if cluster1 == cluster2 and cluster3 != cluster4:
                h1 = h1 + 1
            if cluster3 == cluster4 and cluster1 != cluster2:
                h2 = h2 + 1
    return (h1 + h2) / comb(len(data), 2)


# returns what the true clustering of what the data set is
def find_true_clustering(data):
    labels = list()
    # getting the possible labels a data point can be classified as
    for data_point in data:
        exists = False
        if len(labels) == 0:
            labels.append(data_point[len(data_point) - 1])
            continue
        for cluster in labels:
            if data_point[len(data_point) - 1] == cluster:
                exists = True
        if exists == False:
            labels.append(data_point[len(data_point) - 1])
    true_clustering = list()
    # for each label, put all data points of a particular label in a single cluster
    for lab in labels:
        cluster = list()
        for data_point in data:
            if data_point[len(data_point) - 1] == lab:
                cluster.append(data_point)
        true_clustering.append(cluster)
    return true_clustering
