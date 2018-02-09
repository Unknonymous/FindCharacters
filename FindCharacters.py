word_list = ['hello','world','my','name','is','Ray']
char = "o"
#assign test case values

def FindChars(lst, achar):                 #define function
    NewList = []
    i = 0
    for i in range (0, len(lst)):           #loop through words 
        w = 0
        for w in range (0, len(lst[i])):    #loop through characters
            if lst[i][w] == achar:          #check for character match
                NewList.append(lst[i])      #log confirmed match
                break
    print NewList
    

FindChars(word_list, char)