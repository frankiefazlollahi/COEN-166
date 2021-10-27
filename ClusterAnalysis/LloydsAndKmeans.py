# this file contains methods for the Lloyd's method and K-means++ algorithms

import MethodsForClustering
import sys
import random


# selects k initial random centers for lloyd's method
def pick_centers(data, k):
    random.seed()
    centers = list()
    while len(centers) < k:
        data_point = random.choice(data)
        new_center = data_point[:]
        new_center[0] = len(centers)
        centers.append(data_point)
    centers.sort()
    return centers


# given that D(x) is the distance between a point and its nearest center, we pick the initial centers for K-means++
# by picking a random point and continue finding the next points with probability D(x)^2/(Sum(D(x)^2) for all x)
def pick_kmeanspp_centers(data, k):
    # list of centers
    centers = list()
    random.seed()
    # picking random point to be 1st center
    data_point = random.choice(data)
    new_center = data_point[:]
    new_center[0] = len(centers)
    centers.append(new_center)
    while len(centers) < k:
        distances = list()
        # making list of all distances of each data point to its closest center
        for data_point in data:
            min_point_to_center_distance = sys.maxsize
            for c in centers:
                point_to_center_dist = MethodsForClustering.edistance(c, data_point)
                if point_to_center_dist < min_point_to_center_distance:
                    min_point_to_center_distance = point_to_center_dist
            distances.append(min_point_to_center_distance ** 2)
        # sum of all minimum distances between each data point & its nearest center
        distances_sum = sum(distances)
        for i in range(0, len(distances)):
            distances[i] = distances[i] / distances_sum
            if i > 1:
                distances[i] = distances[i] + distances[i - 1]
        # returns random floating point number in range [0.0, 1.0)
        r = random.random()
        for i in range(0, len(distances)):
            if r < distances[i]:
                new_center = data[i][:]
                new_center[0] = len(centers)
                centers.append(new_center)
                break
    return centers


# finding the "new" centers of given clustering
def find_centers(data, clusters):
    centers = list()
    for cluster in clusters:
        center = list()
        total = [0] * len(data[0])
        if len(cluster) != 0:
            for data_point in cluster:
                for j in range(1, len(data_point) - 1):
                    total[j] = total[j] + float(data_point[j])
            for i in range(0, len(total)):
                center.append(total[i] / len(cluster))
        else:
            for thing in total:
                thing = 0
                center.append(thing)
        center[0] = len(centers)
        centers.append(center)
    centers.sort()
    return centers


# pick list of centers depending on which version of kmeans we are using (either LLoyd's method or Kmeans++. Then
# assign each point in data to cluster based on its closest center. Then find the new centers of these clusters.
# Continues this process until clusters of 2 consecutive iteration don't change
def kmeans(data, k, version):
    # picking centers based on version of kmeans
    if version == 'lloyds':
        centers = pick_centers(data, k)
    if version == 'kmeanspp':
        centers = pick_kmeanspp_centers(data, k)

    while True:
        clusters = list()
        for i in range(0, k):
            cluster = list()
            clusters.append(cluster)
        # for each data point we find its distance to each cluster's center & add it to the cluster that has the minimum
        # distance between the cluster's center and the data point
        for data_point in data:
            min_point_to_center_distance = sys.maxsize
            min_center = -1
            for j in range(0, len(centers)):
                distance = MethodsForClustering.edistance(data_point, centers[j])
                if distance < min_point_to_center_distance:
                    min_point_to_center_distance = distance
                    min_center = j
            clusters[min_center].append(data_point)
        new_centers = find_centers(data, clusters)
        # check if the new clusters don't change after 2 consecutive iterations
        if new_centers == centers:
            break
        else:
            centers = new_centers
    return clusters, centers


# this function runs the kmeans function n times and selects the clustering with the lowest kmeans cost
def run_kmeans(filename, k, version, n):
    data, clusters = MethodsForClustering.open_file(filename)
    min_cost = sys.maxsize
    for i in range(n):
        clusters, centers = kmeans(data, k, version)
        cost = kmeans_cost(clusters, centers)
        if cost < min_cost:
            min_cost = cost
            best_cluster = clusters
    MethodsForClustering.print_clustering(best_cluster)
    # find target truth clustering
    true_clustering = MethodsForClustering.find_true_clustering(data)
    # compute hamming distance of Average Linkage clustering & target truth clustering
    ham_distance = MethodsForClustering.hamming_distance(data, clusters, true_clustering)
    print("Hamming distance from true clustering:", ham_distance, "\n")
    return ham_distance


# calculates the sum of square distances between each point and its closest center
def kmeans_cost(clusters, centers):
    cost = 0
    for i in range(len(clusters)):
        for data_point in clusters[i]:
            cost += MethodsForClustering.edistance(data_point, centers[i])**2
    return cost
