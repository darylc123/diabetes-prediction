import csv
from sklearn.naive_bayes import GaussianNB

states = {
	'WA':0, 'WI':1, 'WV':2, 'FL':3, 'WY':4, 'NH':5, 'NJ':6, 'NM':7,
	'NC':8, 'ND':9, 'NE':10, 'NY':11, 'RI':12, 'NV':13,
	'CO':14,
	'CA':15,
	'GA':16,
	'CT':17,
	'OK':18,
	'OH':19,
	'KS':20,
	'SC':21,
	'KY':22,
	'OR':23,
	'SD':24,
	'DE':25,
	'HI':26,
	'TX':27,
	'LA':28,
	'TN':29,
	'PA':30,
	'VA':31,
	'AK':32,
	'AL':33,
	'AR':34,
	'VT':35,
	'IL':36,
	'IN':37,
	'IA':38,
	'AZ':39,
	'ID':40,
	'ME':41,
	'MD':42,
	'MA':43,
	'UT':44,
	'MO':45,
	'MN':46,
	'MI':47,
	'MT':48,
	'MS':49,
	'PR':50,
	'DC':51
}

class Patient:
	def __init__(self, csvfileReaderRow, data):	
		row = csvfileReaderRow
		self.PatientGuid = row[0]
		if data == "TRAIN":s
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
			"""
			if p.hasDiabetes == 1 and p.gender == 1:
				mDiabetic += 1
			if p.hasDiabetes == 0 and p.gender == 1:
				mNon += 1
			if p.hasDiabetes == 1 and p.gender == 0:
				fDiabetic += 1
			if p.hasDiabetes == 0 and p.gender == 0:
				fNon += 1
		
		print mDiabetic
		print mNon
		print fDiabetic
		print fNon
		"""
		
	model = GaussianNB()
	
	correctArr = []
	incorrectArr = []
	for j in range(0, 5):
		section = len(X) / 5
		newX = X[0:j*section] + X[(j+1)*section+1:]
		newY = Y[0:j*section] + Y[(j+1)*section+1:]
		
		model.fit(newX, newY)
		yes = 0
		no = 0
		index = 0
		for i in X[j*section: (j+1)*section]:
			if model.predict(i) == Y[index]:
				yes += 1
			else: no += 1
			index += 1
		
		correctArr.append(float(yes) / (yes + no))
		print float(yes) / (yes + no)
		incorrectArr.append(float(no) / (yes + no))
	
	print sum(correctArr) / 5
	print sum(incorrectArr) / 5
	
	"""
	return model

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
model = train()
#test(model)

