import curses
import datetime
import random

menu = ['Visa', 'MasterCard', 'American Express', '', 'Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    stdscr.addstr(5, 40, "Welcome to our credit card generator!", curses.color_pair(2) | curses.A_BOLD)

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
                    
    stdscr.refresh()


def Rand_Date():
    year = datetime.date.today().year  
    exp_year = random.randint(int(year), int(year) + 5)
    exp_manth = random.randint(1, 12)

    return(str(exp_manth) + ' / ' + str(exp_year))

def Luhn_Alg(card_number):
    j = 0 
    sum = 0 
    for i in map(int, str(card_number)):
        if j % 2 == 0:
            multi = 1
        else:
            multi = 2
        digit = int(i) * multi
        j += 1

        if digit >= 10:
            digit = (digit//10 + digit%10)
        
        sum = sum + digit

    return((10-(sum %10))%10)



def Visa_func(stdscr):
    card_number="4"
    for i in range(14):
        digit = random.randint(0,9)
        card_number = card_number + str(digit)
    
    final_number = str(card_number) + str(Luhn_Alg(card_number))


    stdscr.addstr(2, 10, """\

⠀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⠿⠿⠿⣿⣿⣿⠿⢿⡿⠿⢿⣿⠿⠛⠻⢿⣿⣿⡿⠿⢿⣿⣿⡇
⢸⣿⣿⣖⢀⢸⣿⠃⠀⣾⠀⠀⣾⠃⠀⣴⣦⣼⣿⡟⠀⠀⠸⣿⣿⡇
⢸⣿⣿⣿⡄⠹⡏⠀⣼⣿⠀⢠⣿⣧⣀⠈⠙⢿⡿⠀⣸⡆⠀⣿⣿⡇
⢸⣿⣿⣿⣇⠀⠁⢰⣿⡏⠀⢸⡟⠛⠛⠃⠀⣼⠁⢀⣉⣁⠀⢹⣿⡇
⢸⣿⣿⣿⣿⣶⣶⣿⣿⣧⣤⣾⣷⣦⣤⣶⣿⣷⣶⣾⣿⣿⣶⣾⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀

===========================
                    """)
    date = Rand_Date()
    stdscr.addstr(17, 0, final_number)
    stdscr.addstr(18, 0, date)
    stdscr.addstr(19, 0, str(random.randint(100, 999)))
    
    

def Mastercard_func(stdscr):
    card_number = random.randint(2221, 2720)
    for i in range(11):
        digit = random.randint(0,9)
        card_number = str(card_number) + str(digit)
    
    final_number = str(card_number) + str(Luhn_Alg(card_number))

    stdscr.addstr(2, 10, """\

    ⠀⠀⠀⠀⣀⣤⣶⣶⣶⣶⣶⣶⣤⣀⣀⣤⣶⣶⣶⣶⣶⣶⣤⣀⠀⠀⠀⠀
    ⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠉⠉⠛⠻⢿⣿⣷⣄⠀⠀
    ⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠙⢿⣿⣧⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣿⣿⡇
    ⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣠⣾⣿⡟⠀
    ⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⣀⣤⣴⣾⣿⡿⠋⠀⠀
    ⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠿⠿⠛⠉⠉⠛⠿⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀

    ===========================
                        """)
    date = Rand_Date()
    stdscr.addstr(17, 0, final_number)
    stdscr.addstr(18, 0, date)
    stdscr.addstr(19, 0, str(random.randint(100, 999)))
 

def AmericanEx_func(stdscr):
    card_number = random.choice([34, 37])
    for i in range(12):
        digit = random.randint(0,9)
        card_number = str(card_number) + str(digit)
    
    final_number = str(card_number) + str(Luhn_Alg(card_number))


    stdscr.addstr(2, 10, """\

    ⠀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀
    ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⡟⠉⠹⣿⡏⠉⠹⣿⡿⠉⠉⣿⡏⢉⣉⣉⡉⠹⡿⠋⣩⣿⡇
    ⢸⣿⡟⠀⠾⠀⢹⡇⢰⡀⠻⠃⣰⠀⣿⡇⢈⣉⣉⣿⠆⠀⢸⣿⣿⡇
    ⢸⣿⣀⣴⣶⣶⣀⣃⣸⣷⣀⣰⣿⣀⣿⣇⣈⣉⣉⣁⣰⣷⣄⣙⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
    ⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀
    ===========================
                        """)
    date = Rand_Date()
    stdscr.addstr(17, 0, final_number)
    stdscr.addstr(18, 0, date)
    stdscr.addstr(19, 0, str(random.randint(100, 999)))
    
    

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in[10, 13]:
            stdscr.clear()
            if current_row_idx != 3:
                stdscr.addstr(0, 0, "You chose {}, press any key to go back.".format(menu[current_row_idx]))
                if current_row_idx == 0:
                    Visa_func(stdscr)
                elif current_row_idx == 1:
                    Mastercard_func(stdscr)
                elif current_row_idx == 2:
                    AmericanEx_func(stdscr)
                elif current_row_idx == 4:
                    break
                stdscr.refresh()
                stdscr.getch()
            

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()

curses.wrapper(main)