# Derived from https://github.com/sanger-pathogens/Fastaq
# Author: Martin Hunt
# Copyright (c) 2013 - 2017 by Genome Research Ltd.
# GNU GPL version 3	
	
class Read:
	def __init__(self, id = '', seq = '', qual = ''):
		self.id = id
		self.seq = seq
		self.qual = qual
		
	def subsequence(self, start,end):
		return Read(id = self.id+"_"+str(start)+"_"+str(end), seq = self.seq[start:end], qual = self.qual[start:end])
		
	def __str__(self):
		return '@' + self.id + '\n' + self.seq + '\n+\n' + self.qual + '\n'

	def get_next_from_file(self, f):
		line = f.readline()
		
		while line == '\n':
			line = f.readline()
		
		if not line:
			return False
		
		self.id = line.rstrip()[1:]
		line = f.readline()
		
		self.seq = line.strip()
		line = f.readline()
		line = f.readline()
		
		self.qual = line.rstrip()
		return self