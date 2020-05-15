#!/usr/bin/python 
import sys,math 

#function which takes as input the training/testing datasets and returns a list 
#with e-value and classification number (0,1) for each UniProtID
def get_data(filename):
	f = open(filename,"r")
	flist = []
	for line in f: 
		l = []
		line = line.rstrip().split()
		l.append(float(line[1]))
		l.append(int(line[2]))
		flist.append(l)
	return(flist)

#function that calculates the confusion matrix for a given threshold value
def get_cm(data,th):
	cm = [[0,0],[0,0]]
	for line in data: 
		if line[0] >= th and line[1] == 1: 
			cm[1][0] += 1
			print(line)
		if line[0] < th and line[1] == 1:
			cm[0][0] += 1
		if line[0] >= th and line[1] == 0:
			cm[1][1] += 1
		if line[0] < th and line[1] == 0:
			cm[0][1] += 1
			print(line)
	return(cm) 

#function which calculates the accuracy, given a confusion matrix
def acc(cm):
	accuracy = (cm[0][0] + cm[1][1])/(cm[0][0] + cm[1][1]+ cm[0][1]+ cm[1][0])
	return(accuracy)

#function which returns the Matthew correlation coefficient for a given confusion matrix	
def mcc(cm):
	d = float((cm[0][0]+cm[1][0])*(cm[0][0]+cm[0][1])*(cm[1][1]+cm[1][0])*(cm[1][1]+cm[0][1]))
	mcc = ((cm[0][0]*cm[1][1])-(cm[0][1]*cm[1][0]))/math.sqrt(d)
	return(mcc)



if __name__ == "__main__":
	filename = sys.argv[1]
	data = get_data(filename)
	#print(data)
	for i in range(21):
		th = 10**(-i)
		cm = get_cm(data,th)
		accuracy = acc(cm)
		matthew = mcc(cm)
		print('THRESHOLD',th,'CONFUSION MATRIX',cm,'ACCURACY',accuracy,'MCC',matthew)


	
	