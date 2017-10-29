from sklearn import tree
#1=smooth and 0 =bumpy
features = [[140, 1], [130, 1], [150, 0],[170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#1=orange and 0=apple
print clf.predict([[150, 0]])
