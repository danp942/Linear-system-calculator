#Turns fractions into floats
def fraction(num):
  slashpos = num.find('/')
  num = float(num[:slashpos]) / float(num[slashpos+1:]) 
  #for negative decimals devided by negative decimals:
  return num

#determine whether or not the inputs are actual numbers through them only having digits once they're stripped of all mathematical signals
def digit_determine(num):
  if num == '':
    numbutnoextras = '0'
    return numbutnoextras
  if num == '-':
    numbutnoextras = '1' #acts to chop off the signs manually as an exception
    return numbutnoextras
  elif num =='+':
    numbutnoextras = '1'
    return numbutnoextras
  else:
    if num.count('+') > 0:
      numbutnoextras = num.replace('+', '')
      if num.count('.') > 0:
        numbutnoextras = numbutnoextras.replace('.', '')
        if num.count('/') == 1:
          numbutnoextras = numbutnoextras.replace('/', '')
          return numbutnoextras
        else:
          return numbutnoextras
      else:
        if num.count('/') == 1:
          numbutnoextras = numbutnoextras.replace('/', '')
          return numbutnoextras
        else:
          return numbutnoextras
    elif num.count('-') > 0:
      numbutnoextras = num.replace('-', '')
      if num.count('.') > 0:
        numbutnoextras = numbutnoextras.replace('.', '')
        if num.count('/') == 1:
          numbutnoextras = numbutnoextras.replace('/', '')
          return numbutnoextras 
        else:
          return numbutnoextras
      else:
        if num.count('/') == 1:
          numbutnoextras = numbutnoextras.replace('/', '')
          return numbutnoextras
        else:
          return numbutnoextras
    elif num.count('.') > 0:
      numbutnoextras = num.replace('.', '')
      if num.count('/') == 1:
        numbutnoextras = numbutnoextras.replace('/', '')
        return numbutnoextras
      else:
        return numbutnoextras
    elif num.count('/') == 1:
      numbutnoextras = num.replace('/', '')
      return numbutnoextras
    else:
      numbutnoextras = num
      return numbutnoextras

#float converter
def float_convert(num):
  numbutnoextras = digit_determine(num)
  if numbutnoextras.isdigit():
    if num.count('.') > 0:
      if num.count('/') == 1:
        num = fraction(num)
        return num
      else:
        num = float(num)
        return num
    else:
      if num.count('/') == 1:
          num = fraction(num)
          return num
      else:
        if num == '':
          num = 1.0
          return num
        elif num == '+':
          num = 1.0
          return num
        elif num == '-':
          num = -1.0
          return num
        else:
          num = float(num)
          return num
  else:                      
    return print('Make sure you\'ve entered numbers of some kind for the slope and y-int. Even -x works.') 
#detects if the order of m and b has been switched. If so, it turns them into the appropriate value
def switcheroo(line): #have to error hadnle here because it's the first bit of code that runs
  if line[0:line.find('=')] != 'Y' or line.count('X') == 0: 
    print('Make sure it\'s in proper y-intercept form: y = mx+b. Order of slope & y-int and spaces are irrelevant.')
    return 'string', 'string' #Needs to return something that's not a float so it gets caught in the if statment on line 148.
  else: #For detecting the substrings according to variable
    if line[-1] == 'X':
      if line.count('-') == 2:
        after1stneg = line[line.find('-')+1:]
        sndnegpos = line[after1stneg].find('-')
        slope = line[sndnegpos:line1.find('X')]
        yint = line[line.find('=')+1:sndnegpos]
        return slope, yint
      elif line.count('-') == 1 and line.count('+') ==1:
        if line.find('-') < line.find('+'):
          slope = line[line.find('+'):line.find('X')]
          yint = line[line.find('=')+1:line.find('+')]
          return slope, yint
        else:
          slope = line[line.find('-'):line.find('X')]
          yint = line[line.find('=') + 1:line.find('-')]
      elif line.count('-') == 1:
        slope = line[line.find('-'):line.find('X')]
        yint = line[line.find('=')+1:line.find('-')]
        return slope, yint
      else:
        slope = line[line.find('+'):line.find('X')]
        yint = line[line.find('=')+1:line.find('+')]
        return slope, yint
    else: #wil also return slope and y-intercept of a non-switched line
      slope = line[line.find('=')+1:line.find('X')]
      yint = line[line.find('X')+1:]
      return slope, yint
  

#main program
line1 = input('Please enter the equation of the first line:\n')
line2 = input('Please enter the equation of the second line:\n')
#Takes out spaces
line1 = line1.replace(' ', '')
line2 = line2.replace(' ', '')
#Makes y and x capitals to increase their input, so the user can input a capital x or capital y and the program will still run.
line1 = line1.replace('y', 'Y')
line2 = line2.replace('y', 'Y')
line1 = line1.replace('x', 'X')
line2 = line2.replace('x', 'X')

slope1, yint1 = switcheroo(line1)
slope = slope1
yint = yint1
slope2, yint2 = switcheroo(line2)
slope = slope2
yint = yint2
#Testing if the element between 0 and '=' is y, and also if x is mentioned in either lines.

if line1[0:line1.find('=')] != 'Y' or line2[0:line2.find('=')] != 'Y' or line1.count('X') == 0 or line2.count('X') == 0: 
  print('Make sure it\'s in proper y-intercept form: y = mx+b. Spaces are irrelevant.')
else:
  #Converts to floats
  slope1 = float_convert(slope1)
  slope2 = float_convert(slope2)
  yint1 = float_convert(yint1)
  yint2 = float_convert(yint2)

  #final barricade to make sure incorrect outputs don't access the equation solver 
if type(slope1) != float or type(slope2) != float or type(yint1) != float or type(yint2) != float:
  print('Make you\'ve entered numbers of some kind.')
else: #finds PoI as well as the other outputs required for if the slope and y-intecept were numbers of some sort
  slope1 = float(slope1)
  slope2 = float(slope2)
  yint1 = float(yint1)
  yint2 = float(yint2)
  if slope1 == slope2:
    if yint1 == yint2:
      print('They are the same line')
    else: 
      print('They are parallel but not the same line.')
  elif slope2 == -1 / slope1:
    poiX = (yint2-yint1)/(slope1-slope2)
    poiY = slope1*poiX + yint1
    print('The lines are perpendicular and intersect at (' + str(poiX) +', ' + str(poiY) + ')')
  else:
    poiX = (yint2-yint1)/(slope1-slope2)
    poiY = slope1*poiX + yint1
    print('They are neither parallel nor perpendicular and intersect at (' + str(poiX) +', ' + str(poiY) + ')')
 