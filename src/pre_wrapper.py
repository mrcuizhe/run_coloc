#/usr/bin/python

# pre_wrapper.py
# Caleb Matthew Radens
# 2016_1_26
# modified by YoSon

# This script parses the eQTL tissue files to prepare them for 
#  wrapper.R
#
# Note: this script depends on helper_functions.py and folderize_by_column

from helper_functions import make_consign_job_command, submit_consign_job
from subprocess import call
import sys
import os

print "Starting pre_wrapper.py"

home_base = str(sys.argv[1])
eqtlfile = str(sys.argv[2])

data = home_base+"data/"
log = home_base+"log/"
script = home_base+"script/"

generally_useful = script+"generally_useful.py"
folderize_by_column = "folderize_by_column.py"

# Add my script folder to the path (just in case some nincompoop tries to use
#  this scipt in the future and gets errors because they didn't properly 
#  import my helper_functions.py module...
sys.path.append(generally_useful)

if not os.path.isfile(script+folderize_by_column):
	raise StandardError(folderize_by_column+" wasn't found in script/ folder.")

# Build the command line argument for fodlerize_by_column
#  Note: keeping only those columns needed for coloc analysis.
extra = eqtlfile + " 0 " + home_base + " keep_0_1_2_3_8_9"
command = make_consign_job_command(
		Script=folderize_by_column,
		ScriptDir=script,
		ErrOut=True,
		ErrOutDir = log,
		Extra=extra)
print "Command for input file looks like:\n"+str(command)

submit_consign_job(command)

