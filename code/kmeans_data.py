# we will have K clusters
K = 3

#each cluster will have equal prior probability
#   the [] make the fraction a 'list' of length 1, mutliplying a list repeats it
rho = [1.0/K] *K

# we will draw N samples
N = 100

# we will work in D dimensions
D = 2

# our cluster centers will be as below
#    these hard coded centers will have to change if D or K change
mu = np.asarray([[-6,6],[1,6],[6,-1]])

# first we draw the cluster assignment variables
#  we will sample from a list of 0,1,..., K-1 with replacement with
#       probabilities from rho
y_opts = range (K)
y = np.random.choice(y_opts,size =(N,),p=rho)

# now we can sample our data points from a normal distribution
#   this returns a list, using a list comprehension on the outside []
#   it sampels a mvn random # using the y_i th row, and an identity covariance
#   it iterates over the elements in y
x = np.asarray([np.random.multivariate_normal(mu[y_i],2*np.eye(D)) for y_i in y])
