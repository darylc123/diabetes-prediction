from patient import Patient
from medications import Medications
from createData import *
import csv
from sklearn.naive_bayes import GaussianNB

def evaluateKFolds(data, classifier):
    avPrecision = []
    avRecall = []
    avFscore = []
    avAccuracy = []
    for training, test in data:
            X = []
            Y = []
            for patient in training:
                X.append(patient.featureVector)
                Y.append(patient.hasDiabetes)
            classifier.fit(X, Y)
            
            TP, FP, TN, FN = 0.0, 0.0, 0.0, 0.0
            for patient in test:
                trueClass = patient.hasDiabetes
                predictedClass = classifier.predict(patient.featureVector)
                if predictedClass == trueClass and trueClass == 1: TP += 1
                if predictedClass == trueClass and trueClass == 0: TN += 1
                if predictedClass != trueClass and trueClass == 1: FN += 1
                if predictedClass != trueClass and trueClass == 0: FP += 1
    
            if (TP + FP) == 0: precision = 0.0
            else: precision = TP / (TP + FP)
            if (TP + FN) == 0: recall = 0.0
            else: recall = TP / (TP + FN)
            if precision + recall == 0: f_score = 0.0
            else: f_score = 2*precision*recall / (precision + recall)
            
            accuracy = (TP + TN) / (TP + TN + FP + FN)
            
            print "Precision: " + str(precision)
            print "Recall: " + str(recall)
            print "F1 Score: " + str(f_score)
            print "Accuracy: " + str(accuracy) + "\n"
            
            avPrecision.append(precision)
            avRecall.append(recall)
            avFscore.append(f_score)
            avAccuracy.append(accuracy)
    
    print "Average Precision: " + str(sum(avPrecision) / len(avPrecision) * 100) + "%"
    print "Average Recall: " + str(sum(avRecall) / len(avRecall) * 100) + "%"
    print "Average F1 Score: " + str(sum(avFscore) / len(avFscore) * 100) + "%"
    print "Average Accuracy: " + str(sum(avAccuracy) / len(avAccuracy) * 100) + "%"          

def main():
    FOLD_COUNT = 5
    data = getData(FOLD_COUNT)
    evaluateKFolds(data, GaussianNB())

if __name__ == "__main__":
    main()
