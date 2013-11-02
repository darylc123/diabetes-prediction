import csv

#Gets the age group by decade a patient was born in
def AgeGroup(year_of_birth):
	dec = year_of_birth - 1900
	if dec < 10: return 0
	if dec < 20: return 1
	if dec < 30: return 2
	if dec < 40: return 3
	if dec < 50: return 4
	if dec < 60: return 5
	if dec < 70: return 6
	if dec < 80: return 7
	if dec < 90: return 8
	if dec < 100: return 9

def US_Region(state):
	WEST = ['WA', 'OR', 'WY', 'MT', 'ID', 'CO', 'UT', 'NV', 'AZ', 'CA','NM', 'AK', 'HI']
	MIDWEST = ['ND', 'SD', 'MN', 'WI', 'MI', 'NE', 'IA', 'IL', 'IN', 'OH', 'KS', 'MO']
	SOUTH = ['TX', 'OK', 'AR', 'LA', 'WV', 'MD', 'DE', 'DC', 'KY', 'VA', 'TN', 'NC', 'MS', 'AL', 'GA', 'SC', 'FL', 'PR']
	NORTHEAST = ['ME', 'NH', 'VT', 'NY', 'MA', 'RI', 'CT', 'NJ', 'PA']

	if state in WEST: return 0
	if state in MIDWEST: return 1
	if state in SOUTH: return 2
	if state in NORTHEAST: return 3
	raise Exception(state + " not found in any region")

class Patient:
	def __init__(self, csvfileReaderRow):	
		row = csvfileReaderRow
		self.PatientGuid = row[0]
		self.DoctorGuid = row[5]
		
		self.featureVector = []
		
		#Do they have diabetes
		self.hasDiabetes = (int(row[1]))
		
		#Gender Test, 1 for Male, 0 for female
		if row[2] == "M": self.featureVector.append(1)
		else: self.featureVector.append(0)
		
		#Age test, see AgeGroup for details
		self.featureVector.append(AgeGroup(int(row[3])))
		
		#Region test, see US_Region for details
		self.featureVector.append(US_Region(row[4]))

	def featureVector(self):
		return self.featureVector

	def classification():
		return self.hasDiabetes
	

def train():
	X = [] #Feature Vectors
	Y = [] #Classifications
	with open('trainingSet/training_SyncPatient.csv', 'r+') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		
		#Create the patients
		for row in reader:
			p = Patient(row)
			print p.featureVector
			X.append(p.featureVector)
			Y.append(p.hasDiabetes)
	return (X, Y)

FOLD_COUNT = 50

train()