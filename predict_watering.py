#!/usr/bin/env

import sys
import argparse
import parser



def train_alg():
	if args.verbose: print("Reading in training data")



def pull_web_data(): pass

def make_prediction(): 

	if args.alg == "kNN": pass
	elif args.alg == "naiveBayes": pass


def parse_args():
	"""
	Take command line input, parse, and return to main.
	args is defined as global 
	"""
	parser = argparse.ArgumentParser(description='Inputs from command line.')
	parser.add_argument("-v", "--verbose", action="store_true",
                    help="Increase output verbosity")
	parser.add_argument("--alg",type=str,choices=["kNN"],default="kNN",required=False,
                    help="Prediction algorithm")
	parser.add_argument("--train", 
		help='Read in training set and train algorithm',action="store_true")
	global args
	args = parser.parse_args()


def main():

	# Parse command line input, global var "args" is created
	parse_args()

	if args.train:
		if args.verbose: print("Training algorithm...looking for training set")
		train_alg()

	if args.verbose: print("Gathering web data for prediction")	
	# https://stackoverflow.com/questions/19978707/historical-weather-data-from-noaa
	pull_web_data()

	make_prediction()	




if __name__ == "__main__": main()

