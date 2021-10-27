import SingleLinkage
import AverageLinkage
import LloydsAndKmeans
import pandas
import sys


# runs each of the clustering algorithms for each dataset and prints out the clusterings of each data set for each
# algorithm in clusterings.txt. & also displays a table of the hamming distances for each of the algorithms in table.csv
def test():
    # file to write to
    sys.stdout = open("clusterings.txt", "w")

    # middle number of data set = k (number of clusters we want)
    datasets = [["iris", 3, "Iris"], ["balance-scale", 3, "Balance-Scale"], ["wine", 3, "Wine"]]
    # another data set for testing: ["glass", 6, "Glass"]

    results = [["Dataset", "Single Linkage", "Average Linkage", "Lloyds(n=1)", "Lloyds(n=100)", "K-means++(n=1)",
                "K-means++(n=100)"]]

    for set in datasets:
        print("Dataset: ", set[2])
        row = [set[2]]

        # running Single Linkage
        print("Clustering Algorithm: ", results[0][1])
        row.append(SingleLinkage.single_linkage(set[0], set[1]))

        # running Average Linkage
        print("Clustering Algorithm: ", results[0][2])
        row.append(AverageLinkage.average_linkage(set[0], set[1]))

        n = 1
        # running Lloyd's Method 1 time
        print("Clustering Algorithm: ", results[0][3])
        row.append(LloydsAndKmeans.run_kmeans(set[0], set[1], "lloyds", n))

        n = 100
        # running Lloyd's method 100 times
        print("Clustering Algorithm: ", results[0][4])
        row.append(LloydsAndKmeans.run_kmeans(set[0], set[1], "lloyds", n))

        n = 1
        # running Kmeans++ 1 time
        print("Clustering Algorithm: ", results[0][5])
        row.append(LloydsAndKmeans.run_kmeans(set[0], set[1], "kmeanspp", n))

        n = 100
        # running Kmeans++ 100 times
        print("Clustering Algorithm: ", results[0][6])
        row.append(LloydsAndKmeans.run_kmeans(set[0], set[1], "kmeanspp", n))

        results.append(row)

    # putting our results into output file
    dataframe = pandas.DataFrame(results)
    dataframe.to_csv("table.csv", index=False)
    print(dataframe)
    sys.stdout.close()


# running test() function
test()
