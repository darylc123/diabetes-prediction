import csv
from sklearn.naive_bayes import GaussianNB

states = {
	'WA':0, 'WI':1, 'WV':2, 'FL':3, 'WY':4, 'NH':5, 'NJ':6, 'NM':7,
	'NC':8, 'ND':9, 'NE':10, 'NY':11, 'RI':12, 'NV':13, 'CO':14, 'CA':15,
	'GA':16, 'CT':17, 'OK':18, 'OH':19, 'KS':20,
	'SC':21,'KY':22,'OR':23,'SD':24,'DE':25,'HI':26,'TX':27,'LA':28,'TN':29,
	'PA':30,'VA':31,'AK':32,'AL':33,'AR':34,'VT':35,'IL':36,'IN':37,'IA':38,
	'AZ':39,'ID':40,'ME':41,'MD':42,'MA':43,'UT':44,'MO':45,'MN':46,'MI':47,
	'MT':48,'MS':49,'PR':50,'DC':51
}

class Patient:
	def __init__(self, csvfileReaderRow, data):	
		row = csvfileReaderRow
		self.PatientGuid = row[0]
		if data == "TRAIN":
			self.hasDiabetes = int(row[1])
			if row[2] == "M": self.gender = 1
			else: self.gender = 0
			self.year_of_birth = int(row[3])
			
			self.state = row[4]
			self.DoctorGuid = row[5]
			
			self.featureVector = [self.gender, self.year_of_birth, states[self.state]]
			#self.featureVector = [self.gender, self.year_of_birth, self.state]
		if data == "TEST":
			if row[1] == "M": self.gender = 1
			else: self.gender = 0
			self.year_of_birth = int(row[2])
			self.state = row[3]
			self.DoctorGuid = row[4]
			self.featureVector = [self.gender, self.year_of_birth, states[self.state]]
		
	
	def featureVector(self):
		return self.featureVector


def train():
	X = [] #Feature Vectors
	Y = [] #Classifications
	with open('training_syncPatient.csv', 'r+') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		mDiabetic = 0
		mNon = 0
		fDiabetic = 0
		fNon = 0
		
		for row in reader:
			p = Patient(row, "TRAIN")
			X.append(p.featureVector)
			Y.append(p.hasDiabetes)
	return (X, Y)

"""
def test(model):
	X = [] #Feature Vectors
	with open('test.csv', 'r+') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		for row in reader:
			p = Patient(row, "TEST")
			X.append(p.featureVector)
	count0 = 0
	count1 = 0
	for i in X:
		if model.predict(i) == 0: count0 += 1
		else: count1 += 1
	print "No diabetes: " + str(count0)
	print "Has diabetes: " + str(count1)
"""

FOLD_COUNT = 50

def crossFoldValidation(X, Y):
	model = GaussianNB()
	correctArr = []
	#incorrectArr = []
	section = len(X) / FOLD_COUNT
	for j in range(0, FOLD_COUNT):
		newX = X[0:j*section] + X[(j+1)*section+1:]
		newY = Y[0:j*section] + Y[(j+1)*section+1:]
	
		testX = X[j*section: (j+1)*section+1]
		testY = Y[j*section: (j+1)*section+1]
		
		model.fit(newX, newY)
		
		Correct = 0
		Incorrect = 0
		for i in range(len(testX)):
			if model.predict(testX[i]) == testY[i]: Correct += 1
			else: Incorrect += 1
		accuracy = float(Correct) / (Correct + Incorrect)
		correctArr.append(accuracy)
		#incorrectArr.append(float(Incorrect) / (Correct + Incorrect))
		print "Run " + str(j+1) + ": " + str(accuracy)
	
	print "Average Accuracy: " + str(float(sum(correctArr)) / FOLD_COUNT)
	
t = train()
crossFoldValidation(t[0], t[1])
#test(model)

