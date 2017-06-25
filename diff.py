class Header(object):
	"""docstring for ClassName"""
	allele = ['REF', 'ALT', 'GT']
	def __init__(self, diff0, diff1):
		self.contents = []
		head0 = next(diff0)
		head1 = next(diff1)
		it1 = iter(head1)
		for el in head0:
			if el != next(it1):
				raise AttributeError
			self.contents.append(el)
		print(self.contents)
	def at(self, line, str):
		def cti(s):
			if s == 'X':
				return 24
			return int(s)
		if(str == 'CHROM' or str == 'POS'):
			return cti(line[self.contents.index(str)])
		return line[self.contents.index(str)]
	def congruent(self, line0, line1):
		for col in Header.allele:
			if self.at(line0, col) != self.at(line1, col):
				return False
		return True
class Writer():
	def __init__(self, target):
		self.pen = csv.writer(target, delimiter='\t')
	def write(self, line):
		self.pen.writerow(line)



def main():
	with open('normal.txt', newline='') as file0:
		with open('brother.txt', newline='') as file1:
			with open('diff_normal_brother.txt', 'w', newline='') as out:
				diff0 = csv.reader(file0, delimiter='\t')
				diff1 = csv.reader(file1, delimiter='\t')
				headers = Header(diff0, diff1)
				scribe = Writer(out)
				other = next(diff1)
				for line in diff0:
					try:
						while (headers.at(line, 'CHROM') == headers.at(other, 'CHROM') and headers.at(other, 'POS') < headers.at(line, 'POS')) or headers.at(other, 'CHROM') < headers.at(line, 'CHROM'):
							scribe.write(other)
							other = next(diff1)
						if headers.at(other, 'CHROM') == headers.at(line, 'CHROM') and headers.at(other, 'POS') == headers.at(line, 'POS'):
							if not headers.congruent(line, other):
								scribe.write(line)
								scribe.write(other)
							else:
								print('congruency found at chromosome ' + str(headers.at(line, 'CHROM')) + ' at base # ' + str(headers.at(line, 'POS')))
							other = next(diff1)
						else:
							scribe.write(line)
					except StopIteration:
						scribe.write(line)
				try:
					while True:
						scribe.write(other)
						other = next(diff1)
				except StopIteration:
					return
					
import csv
main()
