file = open("input.txt", "r")
total_cal_list = []
total_cal_cur = 0
for line in file:
  if line.strip() == "":
    total_cal_list.append(total_cal_cur)
    total_cal_cur = 0
  else:
    total_cal_cur = total_cal_cur + int(line.strip())
total_cal_list.append(total_cal_cur)
file.close()

total_cal_list.sort(reverse=True)
print(total_cal_list)
print(total_cal_list[0] + total_cal_list[1] + total_cal_list[2])

