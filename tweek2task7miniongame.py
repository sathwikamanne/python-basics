#Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules

#Both players are given the same string,s .
#Both players have to make substrings using the letters of the string s.
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.

#Scoring
#A player gets +1 point for each occurrence of the substring in the string s .

def minion_game(string):
    n=len(string)
    comb=((n)*(n+1))/2
    count_k=0
    count_s=0
    count_k=sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s=comb-count_k
    
    if count_s==count_k:
        print("Draw")
    elif count_s>count_k:
        print("Stuart",int(count_s))
    else:
        print("kevin",int(count_k))
    # your code goes here

if _name_ == '_main_':

#Input (stdin)
#BANANA
  
#Your Output (stdout)
#Stuart 12
#Expected Output
#Stuart 12
