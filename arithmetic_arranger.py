import re
def arithmetic_arranger(problems,displayAnswers=False):
  #Errors
  if(len(problems)>5):
    return('Error: Too many problems.')
  for(expression) in problems:
    if(re.search(' / ',expression)):
      return("Error: Operator must be '+' or '-'.")
    if(re.search('\d[^\s\+\-\d:]+\d',expression)):
      return('Error: Numbers must only contain digits.')

  topNum=list()
  sign=list()
  bottomNum=list()
  finalstring=''
  for expression in problems:
    topNum.append(re.findall('([0-9]+) ',expression)[0])
    bottomNum.append(re.findall(' ([0-9]+)',expression)[0])
    if '+' in expression:
      sign.append('+')
    if '-' in expression:
      sign.append('-')
  for i in range(len(sign)):
    if(len(topNum[i])>4):
      return('Error: Numbers cannot be more than four digits.')
    if(len(bottomNum[i])>4):
      return('Error: Numbers cannot be more than four digits.')

  for i in range(len(sign)):
    numOfWhitespaces=2+max(len(topNum[i]),len(bottomNum[i]))-len(topNum[i])
    finalstring+=' '*numOfWhitespaces
    finalstring+=topNum[i]
    if(i==len(sign)-1):
      continue
    finalstring+=' '*4
  finalstring+='\n'
  for i in range(len(sign)):
    finalstring+=sign[i]
    numOfWhitespaces=1+max(len(topNum[i]),len(bottomNum[i]))-len(bottomNum[i])
    finalstring+=' '*numOfWhitespaces
    finalstring+=bottomNum[i]
    if(i==len(sign)-1):
      continue
    finalstring+=' '*4
  finalstring+='\n'
  for i in range(len(sign)):
    numOfWhitespaces=2+max(len(topNum[i]),len(bottomNum[i]))
    finalstring+='-'*numOfWhitespaces
    if(i==len(sign)-1):
      continue
    finalstring+=' '*4
  if displayAnswers==True:
    finalstring+='\n'
    for i in range(len(sign)):
      if sign[i]=='+':
        sum=int(topNum[i])+int(bottomNum[i])
      if sign[i]=='-':
        sum=int(topNum[i])-int(bottomNum[i])
      numOfWhitespaces=2+max(len(topNum[i]),len(bottomNum[i]))-len(str(sum))
      finalstring+=' '*numOfWhitespaces
      finalstring+=str(sum)      
      if(i==len(sign)-1):
        continue
      finalstring+=' '*4  
  arranged_problems= finalstring
  # print(finalstring)
  return arranged_problems