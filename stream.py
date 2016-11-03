import functools

class Stream:

	def __init__(self, iterable=None):
		if iterable is None:
			iterable = itertools.count(0)
		self.it = iter(iterable)

	def __iter__(self):
		return self.it

	def filter(self, func):
		return Stream(filter(func, self.it))

	def map(self, func):
		return Stream(map(func, self.it))

	def find_first(self):
		return next(self.it)

	def sum(self):
		return sum(self.it)

	def max(self):
		return max(self.it)

	def min(self):
		return min(self.it)

	def all_match(self, func):
		return all(map(func, self.it))

	def any_match(self, func):
		return any(map(func, self.it))

	def sorted(self, key=None):
		if key is None:
			key = lambda ele : ele
		return Stream(sorted(self.it, key=key))

	def list(self):
		return list(self.it)

	def tuple(self):
		return tuple(self.it)

	def reduce(self, accumulator, seed=0):
		return functools.reduce(accumulator, self.it, seed)

	def limit(self, max_size):
		return Stream(itertools.islice(self.it, max_size))

	@staticmethod
	def iterate(seed, incrementor):
		return Stream(iterator(seed, incrementor))


def iterator(seed, incrementor):
	i = seed
	while True:
		yield i
		i = incrementor(i)


if __name__ == '__main__':
	import itertools
	from fractions import Fraction
	import operator

	L = [1,2,3,5,4]

	print(Stream(L).filter(lambda ele: ele > 3)
				   .map(lambda ele: ele * 2)
				   .sorted()
				   .reduce(operator.mul, seed=1))
	

	# Start with an infinite stream [0,1,2, ...]
	print(Stream().map(Fraction) # Turn everything into a fraction
				  .map(lambda ele: 13 * ele / 3) # Divide everything by 2
				  .map(str) # Turn everything into strings
				  .limit(5) # Only use the first 5 elements
				  .list()) # Return stream as list


	print(Stream.iterate(-5, lambda prev: prev + 2)
				.limit(10)
				.list())



