'''
@author: Ruan Neves
'''
from skimage import feature, io
import numpy as np
from os import listdir
from os.path import isfile, join
import csv

params = ['energy', 'contrast', 'homogeneity', 'energy', 'correlation']

def extract(label, directory, spamwriter):

	files = [f for f in listdir(directory) if isfile(join(directory, f))]

	
	for name in files:
		results = [label]  
		image = directory + "\\" + name
		img = io.imread(image)
		glcm = feature.greycomatrix(img, [1], [0, np.pi/4, np.pi/2, (3*(np.pi/4)), np.pi, (5*(np.pi/4)), (6*(np.pi/4)), (7*(np.pi/4))], normed=True)
		for param in params:
			temp = feature.greycoprops(glcm, prop = param)

			for value in temp[0]:
				results.append(str(value))

		spamwriter.writerow(results)


if __name__ == '__main__':

	with open('results.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		extract('cancro', 'D:\\OneDrive\\research\marcassa\\ruan\\laranja\\multiclasses\\images\\Citrus_Canker_550', spamwriter)
		extract('greening', 'D:\\OneDrive\\research\marcassa\\ruan\\laranja\\multiclasses\\images\\HLB_550', spamwriter)
		extract('ver_zn', 'D:\\OneDrive\\research\marcassa\\ruan\\laranja\\multiclasses\\images\\Verrugose_550', spamwriter)
		extract('ver_zn', 'D:\\OneDrive\\research\marcassa\\ruan\\laranja\\multiclasses\\images\\Def. de Zinco_550', spamwriter)
		
		
	

