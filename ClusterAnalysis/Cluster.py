from Data import Data

class Cluster:
    #clust is a list of Data that are grouped together
    def __init__(self, clust_list):
        self.clust_list = clust_list
        #self.clust_list = []
        #for i in self.clust:
        #    self.clust_list.append(i)
    """
    def joinClusters(self, c2):
        newList = []
        for i in self.clust_list:
            newList.append(i)
        for i in c2.clust_list:
            newList.append(i)
        c3 = Cluster(newList)
        return c3
        #for i in c2.clust:
            #self.clust_list.append(i)
    """
    def printCList(self):
        print("labels:")
        for i in self.clust_list:
            print(i.label)
        print("\n")
