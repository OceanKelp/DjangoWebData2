# flow  =  (if todayclose > yesterdaycalose  add (close * vol) to flow  else sub (close * vol )
#The addition is through filter flow = flow +  ((flow - close * vol)/filter constant)
# output is a plot of the flow
# import matplotlib.pyplot as plt
# from app.Pfolder.filter import filter

# def HerbFlow(symbol, df):
#       FilterBy  = 2
#       first = True
#       count = 0
#       cOld = 0
#       cNew = 0

#       negsum = 0
#       plus = 0
#       total = 0
#       #iterate and calculate Money Flow
#       for i in range(0, len(df)):
#         c = df.iloc[i]['Close'].astype(float)
#         v = df.iloc[i]['Volume'].astype(float)
#         CV = c * v
#         cNew = c
#         if first == True:
#           first = False               #close the door

#           cOld = c
#           # set up plot
#           fig, ax = plt.subplots(figsize=(25, 3))
#           ax.grid(axis ='both',linewidth = '4')
#           ax.set_xlabel('x')
#           ax.set_ylabel('y')
#           ax.set_title(symbol)
#           #filter data and plot
#           Fil = filter(CV, CV , FilterBy )
#           ax.plot(count, CV, color='red', linestyle='--', linewidth=2, marker='*')

#         else:
#           if (cNew <= cOld): # price decrease subtract C*V else add
#             CV = -CV
#             negsum = negsum + CV
#           #  print('cv neg ',CV,' Old ',cOld, ' cNew ', cNew ,' First ',first, ' vol ', v)
#           else:
#             plus = plus + CV

#           total = plus + negsum
#           Fil = filter(Fil, total , FilterBy )
#           ax.plot(count, Fil, color='red', linestyle='--', linewidth=2, marker='.')

#           cOld = cNew
#         count = count +1

