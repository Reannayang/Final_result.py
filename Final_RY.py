
import requests
import re
username = input('what is your name?')
#f = open("game_record.txt","w+",encoding='utf-8')
#f.write('小B 3 2 14\n张三 3 3 21\n王五 1 6 6\n')
f = open("game_record.txt","r",encoding='utf-8')
history_info = f.readlines()
users = []
for i in range(len(history_info)):
    users.append(history_info[i][0:2])
    if username in users:
        history_no = re.findall('\d+' ,history_info[i])
        history_no = [int(i) for i in history_no]
        print(history_no)
    else:
        history_no = [0,0,0]
f.close()
print(username, 'you have been played %d times, at least caught in %d times and at average caught in %f times'%(history_no[0],history_no[1],history_no[2]))

def one_round():
    answer = int((requests.get("https://python666.cn/cls/number/guess/")).text)
    bingo = False
    times = 0
    while bingo == False:
        trial = int(input('plz guess and input a number between 1 and 100'))
        times += 1
        if trial >= 1 and trial <= 100:
            if trial > answer:
                print('too big')
            elif trial < answer:
                print('too small')
            else:
                bingo = True
        else:
            print('plz input a valid number between 1-100')
    return times



def renew_record(input,times_n):
    if input[0] == 0:
        renew_time= ((input[0]+1),times_n,((input[2]*input[0]+times_n)/(input[0]+1)))
    else:
        renew_time= ((input[0]+1),min(times_n,input[1]),((input[2]*input[0]+times_n)/(input[0]+1)))
    return renew_time

again = 'y'
while again == 'y'or history_no[0]== 0:
    try:
        times_r = one_round()
        history_no = renew_record(history_no,times_r)
    except ValueError:
        print('invalid input.plz try again')
    print(username, 'you have been played %d times, at least caught in %d times and at average caught in %f times'%(history_no[0],history_no[1],history_no[2]))
    again = input('do you want to play again?')
print('this is the exit. Welcome to play again.')
for i in range(len(history_info)):
    if username in history_info[i]:
        new_site = username +' ' + ' '.join(str(i) for i in history_no)+'\n'
        history_info[i] = new_site

if username not in users:
    new_site = username +' ' + ' '.join(str(i) for i in history_no)+'\n'
    history_info.append(new_site)

with open('game_record.txt','w',encoding='utf-8') as f:
    f.writelines(j for j in history_info)
    f.close()


