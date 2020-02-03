# NBA-Draft-Suggestion-using-K-Means
Suggesting NBA Draft Players based on K-Means Clustering

# Description

K-means is one of the simplest unsupervised learning algorithms that solve the well known clustering problem. The 
procedure follows a simple and easy way to classify a given data set through a certain number of clusters (assume k clusters) fixed a
priori. The main idea is to define k centroids, one for each cluster. These centroids shoud be placed in a cunning way because of 
different location causes different result. So, the better choice is to place them as much as possible far away from each other. The next 
step is to take each point belonging to a given data set and associate it to the nearest centroid. When no point is pending, the first step
is completed and an early groupage is done. At this point we need to re-calculate k new centroids as barycenters of the clusters resulting 
from the previous step. After we have these k new centroids, a new binding has to be done between the same data set points and the nearest new
centroid. A loop has been generated. As a result of this loop we may notice that the k centroids change their location step by step until no 
more changes are done. In other words centroids do not move any more.
Finally, this algorithm aims at minimizing an objective function, in this case a squared error function.

K-Means clustering is used in python through Kmeans function for our project. Clustering is done on data extracted of draftees from
NBA website. Various physical attributes were used to perform the clustering like height, weight, points scored, matches played and even 
finger length of players. Once clustering is done, the draft players are seggregated into 8 positions (0-7). The result of this algorithm
is then fed to the HTML web page where a user can select which position of players he prefers. Once the selection is made, a list of
players appears along with a short description about them. This list is our suggestion.


Team "Missing-In-Action"
