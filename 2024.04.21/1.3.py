def numbers_strip(numbers: list, n: int = 1, num_copy: bool = False) -> list | None:
	for i in range(n):
		numbers.remove(max(numbers))
		numbers.remove(min(numbers))
	if num_copy:
		edit_stripped = numbers.copy()
		return  edit_stripped
		
	else:
		return sample


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped = numbers_strip(sample, 2, num_copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False
