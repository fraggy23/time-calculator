def add_time(start, duration, wk = None):
  
  def divhours(num1):
    return divmod(int(num1),24)

  def divmin(num2):
    return divmod(int(num2),60)

  def divweekday(num3):
    return divmod(int(num3),7)

  
  if wk != None:
    wk = str(wk[0].upper()) + str(wk[1:].lower())
    

  #print(wk,'wk')

  print(start,duration,wk)
  

  weekdays = ['Monday', 'Tuesday' ,'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', '']

  
  wkcheck = 0  
  wkn = 0
  pmam = 0
  newpmam = 'AM'
  newmin = 0
  newhours = 0
  days = 0 
  starthours = start[:-6]
  startmin = start[-5:-2]
  startpmam = start[-2:]
  durationhours = duration[:-3]
  durationmin = duration[-2:]
  newday = ''
  futuredays = ''
  newtimestr= ''
  pmampmam = 'AM'

  for i in range(0, 7):
    
    if wk == weekdays[i]:
      wkcheck = 1
      wkn = i
      #print(i,wkn,'weekdaynumber')

  #print(wkn,'wkn')
  
  
  
  if startpmam == 'AM' and starthours == 12:
   pmam = -12
  
  if startpmam == 'PM' and starthours != 12:
   pmam = 12

  
  
  addmin =  int(durationmin) + int(startmin)
  #print(addmin, 'himin',divmin(addmin))

  newmin = divmin(int(durationmin) + int(startmin))[1]
  #print (newmin,'newmin')

  twentyfourhours = divhours(int(starthours) + int(durationhours) + pmam + divmin(addmin)[0])[1]
  
  #print( divhours(int(starthours) + int(durationhours) + pmam + divmin(addmin)[0]),'hihours', twentyfourhours)

  days = divhours(int(starthours) + int(durationhours) + pmam + divmin(addmin)[0])[0]

  #print(days,'days')
  
    

  if wkcheck == 1:
    newday  = divweekday(days + wkn)[1]
    #print(newday,'newday','wkcheck')


  if twentyfourhours >= 12 and twentyfourhours != 0:
   pmampmam = 'PM'
   #print(f'pmampmam is {pmampmam}')

  pmam = 0
  
  if twentyfourhours > 12:
    pmam = -12

  if twentyfourhours == 0:
    pmam = 12

  if days == 1:
    futuredays = '(next day)'

  if days > 1:
    futuredays = f'({days} days later)'

  if wk != None:
    weekdays = [', Monday', ', Tuesday' ,', Wednesday', ', Thursday', ', Friday', ', Saturday', ', Sunday', '']
    
  
  #print(futuredays,weekdays, twentyfourhours + pmam)
    
  #print(wk,'wk')
  
  if wk != None:
    newtimestr = f'{twentyfourhours + pmam}:{newmin:02d} {pmampmam}{weekdays[newday]} {futuredays}'
    #print('wk is not None')

  if wk == None:
    newtimestr = f'{twentyfourhours + pmam}:{newmin:02d} {pmampmam} {futuredays}'
    #print('wk is None')

  if futuredays == '' and wk == None:
    newtimestr = f'{twentyfourhours + pmam}:{newmin:02d} {pmampmam}'
    #print('futuredays = 0')

  if wk != None and futuredays == '':
    newtimestr = f'{twentyfourhours + pmam}:{newmin:02d} {pmampmam}{weekdays[newday]}{futuredays}'
    

  
  

  print(newtimestr)
  print('newtimestr')
  if newtimestr == "5:42 PM, Monday ":
    print('hello?!!?')
  
  
  
    









  return newtimestr