import hangman_stages
word="apple"


flag=0
points=6
blanks=["_","_","_","_","_"]

pos=[]
while (points!=0 and "_" in blanks):
    print(word)
    letter=input("guess a letter")
    
    if letter in word:
      
        if word.count(letter)>1:
            k=0
            l=0
            
            if flag==0:
                counts=word.count(letter)
                flag=1
                
                for i in range (0,counts):
                    posi=word.index(letter,k+l)
                    pos.append(posi)
                    k=posi
                    l=1  
            for i in pos:
                blanks.pop(i)
                blanks.insert(i,letter)
                pos.remove(i)
                word= word.replace(letter,"_",i)

                break
                
        else:
            po=word.index(letter)
            blanks.pop(po)
            blanks.insert(po,letter)
            word=word.replace(letter,"_")
            
            
        
    else:
       
        points-=1
        print(points)
        
    print(blanks)
    print(hangman_stages.stages[points])






