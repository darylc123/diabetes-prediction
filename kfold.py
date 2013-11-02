import random

def kFoldsData(data, numFolds):
	# Split data into positive and negative
	posData = [patient for patient in data if patient.hasDiabetes]
	negData = [patient for patient in data if not patient.hasDiabetes]

	# Randomize data
	random.seed(1)
	random.shuffle(posData)
	random.shuffle(negData)

	# Calculate size of each fold
	posFoldSize = len(posData) / numFolds
	negFoldSize = len(negData) / numFolds

	# Create list of training, test data pairs: one pair for each fold
	data = []

	for i in range(numFolds):
		posTest = posData[i * posFoldSize : (i + 1) * posFoldSize]
		negTest = negData[i * negFoldSize : (i + 1) * negFoldSize]
		test = posTest + negTest
		random.shuffle(test)
		
		posLeftBoundary, negLeftBoundary = i * posFoldSize, i * negFoldSize
		posRightBoundary, negRightBoundary = (i + 1) * posFoldSize, (i + 1) * negFoldSize
		posTraining = posData[:posLeftBoundary] + posData[posRightBoundary:]
		negTraining = negData[:negLeftBoundary] + negData[negRightBoundary:]
		training = posTraining + negTraining
		random.shuffle(training)
		data.append((training, test))
	return data
