# this file contains methods for the Single Linkage clustering algorithm


import MethodsForClustering


# returns list of all distances between 2 points sorted by smallest to largest distance
def distances_and_sort(data):
    distances_list = list()
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            distance = MethodsForClustering.edistance(data[i], data[j])
            # list of lists that contains IDs of the 2 data points being compared & their distance
            distances_list.append([i, j, distance])
    # sorting by the distances
    distances_list.sort(key=lambda d: d[2])
    return distances_list


# Takes the clusters which contains the two closest points (that arent in same cluster) and merges them,
# until k clusterings remain
def single_linkage(filename, k):
    data, clusters = MethodsForClustering.open_file(filename)
    distances_list = distances_and_sort(data)
    # find 2 closest clusters with sorted distance list
    while len(clusters) > k:
        for i in range(0, len(clusters)):
            for data_point in clusters[i]:
                # finding indexes of 2 closest clusters
                if data_point[0] == distances_list[0][0]:
                    index1 = i
                if data_point[0] == distances_list[0][1]:
                    index2 = i
        del(distances_list[0])
        if index1 == index2 or index1 == -1:
            continue
        # merge the two clusters & remove the unmerged cluster
        for data_point in clusters[index2]:
            clusters[index1].append(data_point)
        del(clusters[index2])
    MethodsForClustering.print_clustering(clusters)
    # find target truth clustering
    true_clustering = MethodsForClustering.find_true_clustering(data)
    # compute hamming distance of Single Linkage clustering & target truth clustering
    ham_distance = MethodsForClustering.hamming_distance(data, clusters, true_clustering)
    print("Hamming distance from true clustering:", ham_distance, "\n")
    return ham_distance
