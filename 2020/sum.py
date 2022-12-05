numsfile = open("nums.txt", "r")

nums = []

for aline in numsfile:
    values = aline.strip()
    nums.append(int(values))

numsfile.close()


for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i]+nums[j]+nums[k] == 2020:
                print(nums[i]*nums[j]*nums[k])
                print(str(nums[i]) + "*"+ str(nums[j]) + "*" +str(nums[k]))
