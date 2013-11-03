import csv

class Medications:
    def __init__(self):	
        self.patientMeds = {}
        self.medArr = []
        with open('trainingSet/training_SyncMedication.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for a in reader: self.medArr.append(a[3])
            self.medArr = list(set(self.medArr))
            
        with open('trainingSet/training_SyncMedication.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            for medicationGuid, patientGuid, ndcCode, medicationName, medicationStrength, Scheudle, DiagnosisGuid, userGuid in reader:
                if patientGuid in self.patientMeds:
                    self.patientMeds[patientGuid].append(self.medArr.index(medicationName))
                else:
                    self.patientMeds[patientGuid] = [self.medArr.index(medicationName)]
    
    def getMedications(self, patientGUID):
        results = [0 for i in range(len(self.medArr))]
        if not self.patientMeds.get(patientGUID): return results
        for index in self.patientMeds.get(patientGUID):
            results[index] = 1
        return results