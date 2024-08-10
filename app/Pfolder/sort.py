
#Sort by highest score
def SortScore (SymbolIn, ScoreIn):
#   Sorted = np.zeros(2,dtype=float)

  sorted = pd.DataFrame(columns=['Symbol', 'Score'] )#   LOOKS LIKE THIS SHOLD BE GOBEL NOT DONE EACH TIMR
  sorted.append(SymbolIn,ScoreIn)
  print('sorted list',sorted)
  return(sorted)
#    Sorted = np.empty(2)

# # Fill the array with some data
#    Sorted = ( ['Score' ,0],['symbol','XX'])
#    #Sorted['Symbol'] = ['stock1','stock2']

#    print('sorted' , Sorted)
  
#    np.insert(Sorted,ScoreIn,SymbolIn)
#    print( 'sorted loaded', Sorted)
#    return(Sorted)
 #a = a[a[:, 0].argsort()]
    #sort
#import numpy as np

## Create a NumPy array of unsorted numbers
arr = np.array([3, 2, 1, 5,7,9, 4])

## Sort the array
arr.sort()

## Print the sorted array
print(arr)
