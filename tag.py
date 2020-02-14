### tag.py ###
### crypto diary ###
from io import BytesIO
from os import getlogin, system
from time import gmtime, sleep
import sys
import shutil
# Usage
# $python tag.py
# $*text text text [ENTER] *text text text [ENTER] *endex
# --->>> diary.endex entry will be writen to materials/diary.endex
class Materials:
	def __init__(self):
		# create header from date, login
		log = getlogin()
		logsize = len(log)
		time = gmtime()
		self.head = bytes(str(time[0]) + str(time[1]) + str(time[2]) + '.' + log + '.')
		self.lenght = len(self.head)
		self.size = 0
		# initialize BytesIO
		self.stream = BytesIO()
		# write header to BytesIO
		self.stream.write(self.head)

	def _write(self, plaintext):
		# write document to BytesIO
		feed = list(plaintext)
		lenght = len(feed)
		for k, l in enumerate(feed):
			a = self._ciph(ord(l))
			one = bytearray(b'\x00')
			one[0] += a
			self.stream.write(one)

	def _ciph(self, ordl):
		# more advanced cryptos here, mw it is +14
		if ordl + 14 > 255: return ordl + 14 - 256
		else: return ordl + 14


	def _save(self):
		# append BytesIO to materials/diary.endex
		self.size = sys.getsizeof(self.stream)
		self.stream.seek(0)
		with open('materials/diary.endex', 'ab') as diary:
			diary.write('\n')
			shutil.copyfileobj(self.stream, diary, length=self.size)

	def put(self):
		# create textdocument
		textline = ''
		while textline != 'endex':
			textline = raw_input('*')
			if textline != 'endex': self._write(textline)
		self._save()
		system('clear')
		print '..diary safed.'

if __name__ == '__main__':
	m = Materials()
	m.put()
