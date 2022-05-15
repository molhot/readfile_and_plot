from matplotlib import font_manager, pyplot as plt
import numpy as np

fig, ax = plt.subplots()

#実際の貯金額#
sub_save = open('saving.txt','r',encoding = 'utf-8')
sub_save = sub_save.readlines()
month_list = []
saving_list = []
for save in sub_save:
    save = save.split(' ')
    month_list.append(int(save[0]))
    saving = save[1]
    saving = saving.replace('\n','')
    saving_list.append(int(saving))
#~~~~~~~~~~~~#

#理想的な推移#
ideal_savings = []
duration = len(month_list)
for ideal in range(duration):
    ideal_saving = ideal * 10
    ideal_savings.append(ideal_saving)
print(ideal_savings)
#~~~~~~~~~~~~#

ax.set_xlabel('月',fontname="MS Gothic")
ax.set_ylabel('貯金額',fontname="MS Gothic")

ax.grid()

x = month_list
y1 = saving_list
y2 = ideal_savings
ax.plot(x,y1,color="red",label="now")
ax.plot(x,y2,color="blue",label="ideal")
ax.legend(loc=0)
plt.show()