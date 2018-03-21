from sklearn import tree
import sklearn

clf = tree.DecisionTreeClassifier()

#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
		[190, 90, 47], [175, 64, 39],	[177, 70, 40], [159, 55, 37], 
		[171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

y_pred = []

clf = clf.fit(X, Y)

for i in range(len(X)):
	prediction = clf.predict([X[i]])
	y_pred.append(prediction)


score = sklearn.metrics.accuracy_score(Y, y_pred, normalize=True, sample_weight=None)
prediction = clf.predict([[190, 70, 43]])
print(prediction)
print (score)