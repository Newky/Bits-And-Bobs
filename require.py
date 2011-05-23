#!/usr/bin/env python

import sys,os,hashlib,re

#Assume Base dir is the current working directory of script
base_dir = os.getcwd() 
#Empty hash initialisation
files = {}

def gen_file_list():
	'''
	Initialises the hash of files
	by doing a recursive path walk from the base dir of the running script!
	'''
	nodeNumber = 0
	for root, dirs, files_list in os.walk(base_dir):
		for name in files_list:
			filename = os.path.join(root, name)
			filename_hash = hashlib.sha1(filename).hexdigest()
			#Each Object will have (filename, listoffilehashes)
			files[filename_hash] = [filename, None, nodeNumber]
			nodeNumber += 1


def gen_dependencies_list():
	'''
	Generates the dependency list for the files in the already generated directory file list
	get list (not really happy with this I dont know exactly what its doing, creating a new list? )
	Me no understand python underlying operations :)
	'''
	for k,v in files.iteritems():
		if(v[0] != None):
			v[1] = get_dependencies(v[0])

def get_dependencies(file_name):
	'''
	Function which gets dependencies by parsing the file!!
	'''
	if ".php" in file_name:
		f = open(file_name, "r")
		#print "Processing " + file_name
		#With last / not included
		curdir = file_name[:file_name.rfind("/")]
		dependlist = []
		for line in f.readlines():
			p = re.compile('(require|include)(?:_once)*\({0,1}\s*["|\']([\w\W]*)\.php["|\']\){0,1}')
			test= p.search(line)
			if test != None:
				included_file = test.group(2)
				if included_file != None:
					included_file += ".php"
					included_file_dir = get_real_dir(curdir, included_file)
					included_file = re.sub("\.\./", "", included_file)
					included_file = included_file_dir + included_file
					filename_hash = hashlib.sha1(file_name).hexdigest()
					dependlist.append(included_file);
		return dependlist

def get_file_dependencies(file_name):
	'''
	For single file dependency lookup
	'''
	print "File Dependencies on "+file_name+":\n"
	for i in get_dependencies(file_name):
		print i

def get_real_dir(curdir, file_name):
	'''
	This does a nice little thing
	It finds a ../ indicating the parent directory and then cuts one directory of the curdir
	returning the correct path for the filename
	Example filename:../../file.php
	curdir: /home/richy/blah/this/
	returned curdir: /home/richy
	'''
	real_path = ""
	res = file_name.rfind("../")
	while res != -1:
		file_name = file_name[3:]
		curdir = curdir[:curdir.rfind("/")]
		res = file_name.rfind("../")
	return curdir + "/"

def lookup(filename):
	'''
	This does the lookup for a certain filename on the large generated dependency hash
	'''
	print "File Dependencies on "+filename+":\n"
	try:
		dependlist = files[hashlib.sha1(filename).hexdigest()][1]
	except KeyError:
		return
	if dependlist == None:
		print "No dependencies or else error on dependency parse"
		return
	else:
		for depend in dependlist:
			print depend
	
#def generate_graph():
	'''
	Experimental graph support
	too resource intensive for now
	'''
	#G =nx.Graph()
	#for k,v in files.iteritems():
		#if v[1] != None:
			#G.add_node(v[2])
			#for neighbour in v[1]:
				#try:
					#nodenum =files[hashlib.sha1(neighbour).hexdigest()][2]
					#G.add_edge(v[2], nodenum)
				#except KeyError:
					#pass
	#print "Node Number "+ str(len(G.nodes()))
	#nx.draw(G)
	#plt.show()

if __name__ == "__main__":
	if len(sys.argv) > 1:
		file_name= sys.argv[1] 
		get_file_dependencies(file_name)
	else:
		print "Loading ...................."
		gen_file_list()
		gen_dependencies_list()
		#generate_graph()
		filename = raw_input(">>>")
		while filename:
			lookup(filename)
			filename = raw_input(">>>")
