def LongestCommonSubsequece():
    
    take_input = True
    while(take_input):
        S1 = input("Enter your first string: ")
        S2 = input("Enter your second string: ")
        if not S1.isalpha() or not S2.isalpha():
            print("Please use only alpha characters")
            take_input = True
        else:
            take_input = False

    s1_array = list(S1)
    s2_array = list(S2)

    temp = []
    index = 0 
    for i in range(len(s1_array)):
        for j in range(len(s2_array))[index:]:
            if s1_array[i].lower() == s2_array[j].lower():
                temp.append(s2_array[j])
                index = j+1
            else:
                continue
            break
    S3 = temp
    print ("The Longest Common Subsequence is")
    for i in S3:
        print(i, end="")

if __name__ == "__main__":
    LongestCommonSubsequece()
