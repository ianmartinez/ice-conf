# Defines core functions for dealing with IceWM
import subprocess
import sys
import configparser

# IceWm preference files have no sections, but
# configparser requires one, so add a dummy section
# for parsing
def add_dummy_section(properties_file):
	yield '[{}]\n'.format("dummysection")
	
	for line in properties_file:
		yield line

# Read from a properties file 
def read_properties_file(properties_file):
	prop_file = open(properties_file)
	prop_config = configparser.ConfigParser(strict=False)
	prop_config.read_file(add_dummy_section(prop_file))
	return prop_config

# Get a property from the properties_config 
# returned by read_properties_file
def get_property(properties_config, key):
	return properties_config["dummysection"][key]

	
# TODO: If preferences file doesn't exist, copy 
# /usr/share/icewm/preferences file to
# ~/.icewm/preferences


#props = read_properties_file("/usr/share/default.theme")
#print(get_property(props,"ColorScrollBar"))

# Obviously, I must be missing something, because
# --replace argument for icewmbg does precisely nothing
# despite the documentation saying it should make the new
# icewmbg being called replace the old one.

# Instead, I'll have linux kill it before changing anything so it
# can't complain that another instance is running
def kill_icewmbg():
	subprocess.run(["pkill", "icewmbg"])

# Invoke the program icewmbg and pass arguments to it to
# change wallpaper settings, but be sure to kill the old
# icewmbg first 
def icewmbg(args):
	kill_icewmbg()
	subprocess.Popen(["icewmbg", "--replace"] + args)
