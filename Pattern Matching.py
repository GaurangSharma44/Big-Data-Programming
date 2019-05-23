import re

def PatternMatching():

    take_inputS1 = True
    while(take_inputS1):
        
        S1 = input ("Enter your first string: ")
        m = re.match('^[a-z]+$',S1)
        if m:
            take_inputS1 = False
            #print("String accpeted")
            #print (S1)
        else:
            print("Please enter only alphabets")
            take_inputS1 = True

    take_inputS2 = True
    while(take_inputS2):
        
        S2 = input ("Enter your second string: ")
        o = re.findall("[a-z.*]", S2)
        if o:
            take_inputS2 = False
            #print("String accpeted")
            #print (S2)
        else:
            print("Second string can only contain alphabets, . and *")
            take_inputS2 = True

    S2_array = list(S2)
    S1_array = list(S1)
    temp = []

    print ("S1 array: ",S1_array)
    print ("S2 array: ",S2_array)

    index1 = 0
    index2 = 0
    for j in range(len(S2_array))[index2:]:
        for i in range(len(S1_array))[index1:]:
            if S1_array[i] == S2_array[j]:
                temp.extend(S1_array[i])
                index1 = i+1
                index2 = j+1
                break
            else:
                #'*' can only be the previous character, either 0 or more occurrences
                if S2_array[j] == '*':
                    if S2_array[j-1] == S1_array[i]:
                        temp.extend(S1_array[i])
                        index2 = j+1
                        #n number  of occurrences
                        k = i+1
                        if len(S1_array) > k:
                            if S2_array[j-1] == S1_array[k]:
                                temp.extend(S1_array[k])
                                #index1 = i+1
                                break
                            else:
                                index1 = i+1
                                break
                        else:
                            break
                        break
                    #if '.' is the previous character of '*', it can be either 1 '.' or n number of '.'
                    elif S2_array[j-1] == '.': 
                        temp.extend(S1_array[i])
                        index1 = i+1
                        break
                    #0 occurrences of *
                    else:
                        index2 = j+1
                        break
                #'.' can be any character but only 1 occurrence
                if S2_array[j] == '.':
                    temp.extend(S1_array[i])
                    index1 = i+1
                    index2 = j+1
                    break
                else:
                    temp.extend(S2_array[j])
                    index2 = j+1
                    break

    S3_array = temp
    str1 = ''.join(S1_array)
    str3 = ''.join(S3_array)
    print ("S1: ",str1)
    print ("S3: ",str3)
    
    if bool(re.search(str1,str3))==True: #Searching for a substring
        print ('True')
    else:
        print ('False')  

if __name__ == "__main__":
    PatternMatching()
