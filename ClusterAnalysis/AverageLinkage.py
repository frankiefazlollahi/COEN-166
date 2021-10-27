# this file contains methods for the Average Linkage clustering algorithm

import MethodsForClustering
import sys


# returns n*n matrix of distances between all data points
def make_distances_matrix(data):
    distances_matrix = list()
    for i in range(0, len(data)):
        row = list()
        for j in range(0, len(data)):
            distance = MethodsForClustering.edistance(data[i], data[j])
            row.append(distance)
        distances_matrix.append(row)
    return distances_matrix


# Merges 2 clusters with smallest average distance between them, until k clusters remain
def average_linkage(filename, k):
    data, clusters = MethodsForClustering.open_file(filename)
    distances_matrix = make_distances_matrix(data)
    while len(clusters) > k:
        min_average = sys.maxsize
        index1, index2 = -1, -1
        # finding indexes of 2 clusters with smallest average distance
        for i in range(0, len(clusters)):
            for x in range(i+1, len(clusters)):
                sum = 0
                for j in range(0, len(clusters[i])):
                    for y in range(0, len(clusters[x])):
                        sum += distances_matrix[clusters[i][j][0]][clusters[x][y][0]]
                average = sum / (len(clusters[i])*len(clusters[x]))
                if average < min_average:
                    min_average = average
                    index1 = i
                    index2 = x
        if index1 == index2 or index1 == -1:
            continue
        # merging the 2 clusters & remove unmerged cluster
        for data_point in clusters[index2]:
            clusters[index1].append(data_point)
        del(clusters[index2])
    MethodsForClustering.print_clustering(clusters)
    # find target truth clustering
    true_clustering = MethodsForClustering.find_true_clustering(data)
    # compute hamming distance of Average Linkage clustering & target truth clustering
    ham_distance = MethodsForClustering.hamming_distance(data, clusters, true_clustering)
    print("Hamming distance from true clustering:", ham_distance, "\n")
    return ham_distance
