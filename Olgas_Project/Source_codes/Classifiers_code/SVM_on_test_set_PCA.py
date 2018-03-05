# Import test set input, and train set svm classifier as modules

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

from sklearn.metrics import confusion_matrix

from input_SVM_train_PCA import *

from input_test_set_PCA import *

#  PCA transformation of test data
pca = PCA(n_components = 8)
pca.fit(X_test)
X_PCA_test = pca.transform(X_test)


# Predict the same data just to check if the SVM is actually accurate
(print("Predict the topology of each window on another of data"))

predictions = clfr.fit(X_PCA_train,y_train).predict(X_PCA_test)  # how well can the SVM predict our data?
print(predictions)   # it returns predicted values for the topologies (1-3)
print(clfr.fit(X_PCA_train,y_train).score(X_PCA_test,y_test))  # score for svm predictions over test set

plt.scatter(y_test, predictions)

plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.show()          # Visualizing the true values versus the predictions


print('Predicted topologies')

pretopo = []

for pred in predictions:
    for key, value in struct_labels.items():
        if pred == value:
            pretopo.append(key)
print(pretopo)

# Confusion matrix

# Build a confusion matrix
conf_m = confusion_matrix(y_test, predictions)


# Plot the data

fig = plt.figure(figsize = (8,8))


ax = fig.add_subplot(1,1,1)


residues = ax.imshow(np.array(conf_m), cmap=plt.cm.viridis,
                interpolation='nearest')

hor, ver = conf_m.shape

for i in range(hor):
    for j in range(ver):
        ax.annotate(str(conf_m[i][j]), xy=(j, i),
                    horizontalalignment='center',
                    verticalalignment='center')

bar = fig.colorbar(residues)
labels = ['Globular', 'Signal Peptide', 'Membrane']
plt.xticks(range(hor), labels[:hor])
plt.yticks(range(ver), labels[:ver])
plt.title('Confusion Matrix for a single protein')
plt.xlabel('Predicted Topologies')
plt.ylabel('True Topologies')
plt.show()



