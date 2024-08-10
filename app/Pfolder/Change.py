
#test for change above or below

# def TestChange(SPX, Ind  ):
#   Alreadybelow = JustWentBelow = JustWentabove = BeenAbove = False
#   first = True
#   print(SPX, Ind)
 
#   for xv in SPX[ Ind]:
    
    
#     if first:
#       first = False #close the door
#       FirstVal = xv #day before last day

#     else: #second time
#       first = True  #open first
#       LastVal = xv  # get last

#       if FirstVal < 0 and LastVal < 0:   #if first is neg already below
#         Alreadybelow = True
#       if FirstVal > 0 and LastVal < 0:    # just went below
#         JustWentBelow = True    #'just went below '
#       if FirstVal < 0 and LastVal > 0:  # first is neg Last is plus
#         JustWentabove = True  #'just went above '
#       if FirstVal > 0 and LastVal > 0:   # both are pos
#           BeenAbove = True # 'been above '
#       first = True
#   return( Alreadybelow , JustWentBelow , JustWentabove , BeenAbove )



# #test for change
# def TestChange(SPX, Ind  ):
#   Alreadybelow = JustWentBelow = JustWentabove = BeenAbove = False
#   first = True
 
#   # for xv in SPX[Ind]:

#  # for xv in SPX[Ind]:does not need smbol
#   for xv in SPX['Close']:  
#     if first:
#       first = False #close the door
#       FirstVal = xv #day before last day

#     else: #second time
#       first = True  #open first
#       LastVal = xv  # get last

#       if FirstVal < 0 and LastVal < 0:   #if first is neg already below
#         Alreadybelow = True
#       if FirstVal > 0 and LastVal < 0:    # just went below
#         JustWentBelow = True    #'just went below '
#       if FirstVal < 0 and LastVal > 0:  # first is neg Last is plus
#         JustWentabove = True  #'just went above '
#       if FirstVal > 0 and LastVal > 0:   # both are pos
#           BeenAbove = True # 'been above '
#       first = True
#   return( Alreadybelow , JustWentBelow , JustWentabove , BeenAbove )


#test for change
def TestChange(SPX, Ind  ):
  Alreadybelow = JustWentBelow = JustWentabove = BeenAbove = False
  first = True

  for xv in SPX[ Ind]:
    print(Ind)
    if first:
      first = False #close the door
      FirstVal = xv #day before last day

    else: #second time
      first = True  #open first
      LastVal = xv  # get last

      if FirstVal < 0 and LastVal < 0:   #if first is neg already below
        Alreadybelow = True
      if FirstVal > 0 and LastVal < 0:    # just went below
        JustWentBelow = True    #'just went below '
      if FirstVal < 0 and LastVal > 0:  # first is neg Last is plus
        JustWentabove = True  #'just went above '
      if FirstVal > 0 and LastVal > 0:   # both are pos
          BeenAbove = True # 'been above '
      first = True
  return( Alreadybelow , JustWentBelow , JustWentabove , BeenAbove )
