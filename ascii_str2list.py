import pickle
import os
def word2list(string):
    result = []
    temp = ''
    for i in string:
        if i == '#': 
            temp += '1'
        elif i == ' ': 
            temp += '0'
        elif i == '\n':
            result.append(temp)
            temp = ''
    return result

string = [\
'''  #####   
 ##   ##  
##     ## 
##     ## 
##     ## 
 ##   ##  
  #####   
''',
'''  ##   
####   
  ##   
  ##   
  ##   
  ##   
###### 
''',
''' #######  
##     ## 
       ## 
 #######  
##        
##        
######### 
''',
''' #######  
##     ## 
       ## 
 #######  
       ## 
##     ## 
 #######  
''',
'''##        
##    ##  
##    ##  
##    ##  
######### 
      ##  
      ##  
''',
'''######## 
##       
##       
#######  
      ## 
##    ## 
 ######  
''',
''' #######  
##     ## 
##        
########  
##     ## 
##     ## 
 #######  
''',
'''######## 
##    ## 
    ##   
   ##    
  ##     
  ##     
  ##     
''',
''' #######  
##     ## 
##     ## 
 #######  
##     ## 
##     ## 
 #######  
''',
''' #######  
##     ## 
##     ## 
 ######## 
       ## 
##     ## 
 #######  
''',
'''   ###    
  ## ##   
 ##   ##  
##     ## 
######### 
##     ## 
##     ## 
''',
'''########  
##     ## 
##     ## 
########  
##     ## 
##     ## 
########  
''',
''' ######  
##    ## 
##       
##       
##       
##    ## 
 ######  
''',
'''########  
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
########  
''',
'''######## 
##       
##       
######   
##       
##       
######## 
''',
'''######## 
##       
##       
######   
##       
##       
##       
''',
''' ######   
##    ##  
##        
##   #### 
##    ##  
##    ##  
 ######   
''',
'''##     ## 
##     ## 
##     ## 
######### 
##     ## 
##     ## 
##     ## 
''',
'''#### 
 ##  
 ##  
 ##  
 ##  
 ##  
#### 
''',
'''      ## 
      ## 
      ## 
      ## 
##    ## 
##    ## 
 ######  
''',
'''##    ## 
##   ##  
##  ##   
#####    
##  ##   
##   ##  
##    ## 
''',
'''##       
##       
##       
##       
##       
##       
######## 
''',
'''##     ## 
###   ### 
#### #### 
## ### ## 
##     ## 
##     ## 
##     ## 
''',
'''##    ## 
###   ## 
####  ## 
## ## ## 
##  #### 
##   ### 
##    ## 
''',
''' #######  
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
 #######  
''',
'''########  
##     ## 
##     ## 
########  
##        
##        
##        
''',
''' #######  
##     ## 
##     ## 
##     ## 
##  ## ## 
##    ##  
 ##### ## 
''',
'''########  
##     ## 
##     ## 
########  
##   ##   
##    ##  
##     ## 
''',
''' ######  
##    ## 
##       
 ######  
      ## 
##    ## 
 ######  
''',
'''######## 
   ##    
   ##    
   ##    
   ##    
   ##    
   ##    
''',
'''##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
##     ## 
 #######  
''',
'''##     ## 
##     ## 
##     ## 
##     ## 
 ##   ##  
  ## ##   
   ###    
''',
'''##      ## 
##  ##  ## 
##  ##  ## 
##  ##  ## 
##  ##  ## 
##  ##  ## 
 ###  ###  
''',
'''##     ## 
 ##   ##  
  ## ##   
   ###    
  ## ##   
 ##   ##  
##     ## 
''',
'''##    ## 
 ##  ##  
  ####   
   ##    
   ##    
   ##    
   ##    
''',
'''######## 
     ##  
    ##   
   ##    
  ##     
 ##      
######## 
''',
'''        
        
        
        
        
        
####### 
''',
'''       
  ##   
  ##   
###### 
  ##   
  ##   
''',
'''        
        
        
####### 
        
        
''',
'''#### 
#### 
#### 
 ##  
     
#### 
#### 
''',
''' #######  
##     ## 
      ##  
    ###   
   ##     
          
   ##     
''',
''' #######  
##     ## 
## ### ## 
## ### ## 
## #####  
##        
 #######  
''',
'''  ## ##   
  ## ##   
######### 
  ## ##   
######### 
  ## ##   
  ## ##   
''',
''' ##  
#### 
 ##  
     
 ##  
#### 
 ##  
''',
'''     
     
     
#### 
#### 
 ##  
##   
''',
'''    
    
    
    
    
### 
### 
''',
'''   
   
   
   
   
   
   
''']
word = '0123456789abcdefghijklmnopqrstuvwxyz_+-!?@#:,. '
output = {}
for i in range(len(string)):
    output[word[i]] = word2list(string[i])


dictFile = file('asciiDict.mu', 'wb')
# dictFile = file('asciiDict.mu')
pickle.dump(output, dictFile)
dictFile.close()
# pickleFile = open('asciiDict.mu', 'rb')
# dictA = pickle.load(dictFile)
# print 'out:',dictA
# pickleFile.close()
