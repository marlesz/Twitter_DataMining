__author__ = 'ML'
import numpy, scipy
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt

file = open('hosp_wsp.txt','r')
#save the column/row headers (conditions/genes) into an array

dataMatrix = []

for line in file:
	data = line.strip().split(', ')
	#rowHeaders.append(data[0])
	dataMatrix.append([float(x) for x in data[0:]])
#convert native data array into a numpy array
dataMatrix = numpy.array(dataMatrix)
#print dataMatrix
file.close()
distanceMatrix = dist.pdist(dataMatrix, 'euclidean')
#distanceMatrix =  numpy.ndarray(distanceMatrix)
print len(distanceMatrix)
#numpy.set_printoptions(threshold='nan')
#print distanceMatrix
# y : ndarray	A condensed or redundant distance matrix. A condensed distance matrix is a flat array containing the upper triangular of the distance matrix.
# This is the form that pdist returns. Alternatively, a collection of m observation vectors in n dimensions may be passed as an m by n array.
linkageMatrix = hier.linkage(dataMatrix, 'centroid', 'euclidean')

clust = hier.fcluster(linkageMatrix,0.05 , criterion = 'distance')

dendro = scipy.cluster.hierarchy.dendrogram(linkageMatrix, no_plot=False)
#plt.show()


result = []
for i in range(len(clust)):
	result = result + [[clust[i], dataMatrix[i][0], dataMatrix[i][1]]]
result.sort()
result = numpy.array(result)
#print result

meanx = result[0][1]
meany = result[0][2]
count = 1
final = []

for i in range(len(clust)):
        if i < len(clust)-1:
                if result[i][0] == result[i+1][0]:
                        meanx = meanx + result[i+1][1]
                        meany = meany + result[i+1][2]
                        count = count +1
                else:
                        meanx = meanx/count
                        meany = meany/count
                        meanxy = [meanx, meany]
                        final.append(meanxy)
                        count = 1
                        meanx = result[i+1][1]
                        mean = result[i+1][2]
        else:
                if result[i][0] == result[i-1][0]:
                        meanx = meanx/count
                        meany = meany/count
                        meanxy = [meanx, meany]
                        final.append(meanxy)
                else:
                        meanx = result[i][1]
                        meany = result[i][2]
                        meany = [meanx, meany]
                        final.append(meanxy)

#print final

file2 = open('final.txt', 'w')
for i in range(len(final)):
        file2.writelines(str(final[i]))
        file2.writelines("\n")
file2.close()

