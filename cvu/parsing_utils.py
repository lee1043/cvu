#    (C) Roan LaPlante 2013 rlaplant@nmr.mgh.harvard.edu
#
#	 This file is part of cvu, the Connectome Visualization Utility.
#
#    cvu is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

def rreplace(s,old,new,occurrence):
	li=s.rsplit(old,occurrence)
	return new.join(li)

def hemineutral(s):
	lhind=s.find('lh')
	rhind=s.find('rh')
	if lhind>rhind:
		return rreplace(s,'lh','%s',1)
	elif rhind>lhind:
		return rreplace(s,'rh','%s',1)
	else:
		return s

def mangle_hemi(s):
	return s[-2:]+'_'+s[0:-3]

def same_hemi(s1,s2,char=None):
	if char is None: return s1[0]==s2[0]
	else: return s1[0]==s2[0]==char

#ALL FUNCTIONS THAT FOLLOW ARE NEEDED FOR GIFTI PROCESSING ONLY

def str2intlist(s):
	import re
	return re.split(',| |;',s.strip('[]'))

def appendhemis(olddict,hemi):
	return dict(map(lambda (k,v):(k,hemi+str(v)),olddict.items()))

def eqfun(x):
	return lambda y:y==x
