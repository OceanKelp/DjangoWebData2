# filter new data

from matplotlib import pyplot as plt

def filter(AveragedIn, NewValue , FilterBy ):

  if (AveragedIn < NewValue ):
    DifFilter = (NewValue - AveragedIn)
    DifFilter = DifFilter/FilterBy
    AverageNew = AveragedIn +  DifFilter
  else:
    DifFilter = (AveragedIn - NewValue)
    DifFilter = DifFilter/FilterBy
    AverageNew = AveragedIn -  DifFilter
    #print('Dif ',DifFilter, ' Avg ',AverageNew)
  return(AverageNew)

# # program used to test filter
# #Filter check
# count = 0
# AveragedIn = 110
# NewValue = 2
# FilterBy = 12
# MaxTimes = 50

# fig, ax = plt.subplots(figsize=(25, 3))
# ax.grid(axis ='both',linewidth = '4')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('filter')
# New = filter(AveragedIn, NewValue , FilterBy )
# for x in range(MaxTimes ):
#   ax.plot(count, New, color='red', linestyle='--', linewidth=2, marker='.')
#   count = count + 1
#   New = filter(New, NewValue , FilterBy )

