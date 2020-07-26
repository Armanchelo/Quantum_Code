def f(txt):
	txt = txt.split(' ')
	nums = []
	signs = []
	for item in txt:
		try:
			nums.append(int(item))
		except ValueError:
			signs.append(item)
	for n in range(len(nums) - 1):
		if signs[n] == '<=':
			if nums[n] > nums[n + 1]: return False
		elif signs[n] == '>=':
			if nums[n] < nums[n + 1]: return False
		elif signs[n] == '<':
			if nums[n] >= nums[n + 1]: return False
		elif signs[n] == '>':
			if nums[n] <= nums[n + 1]: return False
	return True