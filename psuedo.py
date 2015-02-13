#preparing OBIS data for deepdive
#in python
#parseobis(obis):
	#capture species name 
	#capture latitude coordinate
	#capture longitude coordinate
	#return a text file that is species name plus laittude and longitude coordinates
	#count number of species
	#count the number of data points for each species
	#return a text file that is the data points for each species
	#return a text file that is all the latitude longitude corridinates withou names
	#return a text file for each species coordinates 

#using deepdive to determine relatedness and sptial closeness of data points between species
#need phylogenetic divergence information on the species (times, closeness of relation, etc., for this purpose it might only be possible to test a few species to begin wiht dpeending on the quality of the data that can be acquired)

#create new applicaiton folder for application (spatdiv)
#move in to folder
#use applicaiton.conf to as entry point and create a home for applicaton
#copy run.sh to applicaiton home
#move into app home directory 
#make directroy for data
#move into data directory 
#import data files
#implement data flow
#using an extractor extract relaiton between species (extremely related, highly related, related, poorly related, not related)
#using an extractor extract geographic relation bewteen lat long coordinates of the species on a scale of (0-5)
#deepdive, preparing deepdive for data
#creating application, in home directory
#create directory in which application skeleton will be tested
##mkdir -p app/spatdiv
#move into directory
#cd app/spatdiv
#upload database connection through file applucation.conf
#cp ../../examples/template/application.conf .
#cp ../../examples/template/run.sh .
#cp ../../examples/template/env.sh .
#in env.sh modify the place holder, modify to use database of application
#export DBNAME=deepdive_spatdiv
#make sure database is created
#bash createdb deepdive_spatdiv
#verify everything is working with run.sh script
#./run.sh
#import data 
#Apply extractor
