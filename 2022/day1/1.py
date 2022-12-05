file = open("input.txt", "r")
total_cal_max = 0
total_cal_cur = 0
for line in file:
  if line.strip() == "":
    if total_cal_cur > total_cal_max:
      total_cal_max = total_cal_cur
    total_cal_cur = 0
  else:
    total_cal_cur = total_cal_cur + int(line.strip())
file.close()

print(total_cal_max)

