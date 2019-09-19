from IPython.display import clear_output

def display_board(board):
    print("hello world, display board {0}".format(board))


display_board('bd')

def old_mac(name):
    # first_h = name[0:3]
    # second_h = name[3:]
    # print(first_h.capitalize()+second_h.capitalize())
    rev = name.split()[::-1]
    print('_'.join(rev))

old_mac('I am home')

def has_33(n):
    for i in range(len(n)-1):
        val = (n[i]==n[i+1]==3)
        print(val)
has_33([3,3,3,3,3,1])

def paper_doll(text):
    three = []
    for i in text:
        k=i*3
        three.append(k)
    print(''.join(three))
    re=''
    for char in text:
        re += char*3
    print(re)
paper_doll('love')

def blackjack(a,b,c):
    total=a+b+c
    if 1<=a>11 or 1<=b>11 or 1<=c>11:
        print('Please enter a value in between 1-11')
    elif total>21 and a==b==c==11:
        new_total=total-10
        print('new_total = ', new_total)
        if new_total>21:
            print('You are BUST!!!')
            exit()

    elif total==21:
        print("you got {}, blackjack".format(total))


blackjack(11,5,8)