#!/usr/bin/env python
#    github marquee
#    Copyright (C) 2013  Jason Pruitt
#
#    This program is free software: you can redistribute it and/or modify
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
###########################################################################

import os
import sys
from time import time, strftime, sleep
from datetime import datetime
from subprocess import Popen, PIPE
from fonts import fonts

day_sec = 60.0 * 60.0 * 24.0
week_sec = day_sec * 7.0
year_sec = day_sec * 365.0

cur_time = time()
cur_day = cur_time - year_sec
char_days = 7.0 * 4.0 * day_sec

def ts_to_date(ts):
	# time stamp to date string
	return datetime.fromtimestamp(ts).strftime('%a %b %d %H:%M:%S %Y')

def commit(ts):
	# make a commit
	# multi commit for darker color
	for i in xrange(0, 10):
		with open('committer', 'w') as f:
			f.write(str(ts+i))
		date = ts_to_date(ts+i)
		p = Popen(['env','GIT_AUTHOR_DATE=%s' % date, 'git', 'commit', '-a', '-m', str(ts)], stdout=PIPE)
		# This is here just to burn up some time as git might get overwhelmed.
		print p.stdout.read()
		sleep(.05)


def print_char(char, pos):
	# convert font to date and commit each "bit"
	font = fonts[ord(char)]
	start_day = cur_day + float(pos) * char_days
	day = start_day
	d = 0.0
	for line in font:
		for i in xrange(0, 8):
			bit = (line >> i) & 0x01
			if bit:
				commit(day)
			day += week_sec
		d += 1.0
		day = start_day + (d * day_sec)

if __name__ == '__main__':
	# c is the character offset from -1 year
	# chars are 4 "bits/weeks" wide
	c = 3
	for s in sys.argv[1]:
		print_char(s, c)
		c += 1
			
