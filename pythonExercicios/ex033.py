print('--Encontrando o maior e o número--')
nums = [int(input('Informe os três números: ')), int(input()), int(input())]
mn = nums[0]
if nums[1] < nums[0] and nums[1] < nums[2]:
    mn = nums[1]
if nums[2] < nums[0] and nums[2] < nums[1]:
    mn = nums[2]
ma = nums[0]
if nums[1] > nums[0] and nums[1] > nums[2]:
    ma = nums[1]
if nums[2] > nums[0] and nums[2] > nums[1]:
    ma = nums[2]
print('O maior é {} e o menor é {}.'.format(ma, mn))
