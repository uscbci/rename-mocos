import flywheel
import re
import json

#Find MocoSeries scans and rename them to have the name of the related acquisition


# Grab Config
CONFIG_FILE_PATH = '/flywheel/v0/config.json'
with open(CONFIG_FILE_PATH) as config_file:
    config = json.load(config_file)

api_key = config['inputs']['api_key']['key']
session_id = config['destination']['id']


fw = flywheel.Flywheel(api_key)
session = fw.get_session(session_id)

#loop through acquisitions
for acquisition in session.acquisitions():
	if acquisition.label == "MoCoSeries":
		print("Found moco series at %s",acquisition.timestamp) 
		#Find correponding original file
		for candidate in session.acquisitions():
			if candidate.timestamp == acquisition.timestamp:
				print("Matched to %s at %s" % (candidate.label,candidate.timestamp))
				#we found it, set the name
				newname = "%s MocoSeries" % candidate.label
				print("Will rename to %s" % newname)
				acquisition.update(label=newname)
