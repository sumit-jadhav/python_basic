def game():
    return 874

score=game()
with open("C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\highscore.txt") as f:
    highscoreStr=f.read()

if highscoreStr=='':    
    with open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\highscore.txt','w') as f:
        f.write(str(score))

elif int(highscoreStr)<score:    
    with open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\highscore.txt','w') as f:
        f.write(str(score))
