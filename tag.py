### tag.py ###
### crypto diary ###
from io import BytesIO
import sys
# Usage
# $python tag.py
# $*text text text [ENTER] *text text text [ENTER] *endex
# --->>> diary.endex entry will be writen to materials/diary.endex
class Materials:
	def __init__(self):
		# create header from date, login
		self.head = input('message head *').encode()
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

	def unlock(self):
		# read the diary per head
		pass

	def _ciph(self, ordl):
		# more advanced cryptos here, mw it is +14
		if ordl + 14 > 255: return ordl + 14 - 256
		else: return ordl + 14


	def _save(self):
		# append BytesIO to materials/diary.endex
		self.size = sys.getsizeof(self.stream)
		self.stream.seek(0)
		with open('materials/diary.endex', 'ab') as diary:
			diary.write('\n'.encode())
			diary.write(self.stream.read())

	def put(self):
		# create textdocument
		textline = ''
		while textline != 'endex':
			textline = input('*')
			if textline != 'endex': self._write(textline)
		self._save()
		print('..diary safed.')

if __name__ == '__main__':

	if len(sys.argv()) == 1:
		m = Materials()
		m.put()
		exit()
	elif 'unlock' in sys.argv[1]:
		pass
		
