import csv

class Allergies:
    def __init__(self):	
        self.patientAllergies = {}
        self.allergyArr = []
        with open('trainingSet/training_SyncAllergy.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for a in reader: self.allergyArr.append(a[2])
            self.allergyArr = list(set(self.allergyArr))
            
        with open('trainingSet/training_SyncAllergy.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            for allergyGuid, patientGuid, allergyType, startYear, reactionName, severityName, ndcCode, medicationName, userGuid in reader:
                if patientGuid in self.patientAllergies:
                    self.patientAllergies[patientGuid].append(self.allergyArr.index(allergyType))
                else:
                    self.patientAllergies[patientGuid] = [self.allergyArr.index(allergyType)]
    
    def getAllergies(self, patientGUID):
        results = [0 for i in range(len(self.allergyArr))]
        if not self.patientAllergies.get(patientGUID): return results
        for index in self.patientAllergies.get(patientGUID):
            results[index] = 1
        return results
