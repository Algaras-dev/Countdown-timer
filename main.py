'''Countdown time until predefined date'''

import os
import time
from datetime import datetime

# Ascii art charachters used to display the countdown
# taken from: https://patorjk.com/software/taag/#p=display&f=Doh&t=
_ascii_charachters = {
    '0': '''     000000000        00:::::::::00    00:::::::::::::00 0:::::::000:::::::00::::::0   0::::::00:::::0     0:::::00:::::0     0:::::00:::::0 000 0:::::00:::::0 000 0:::::00:::::0     0:::::00:::::0     0:::::00::::::0   0::::::00:::::::000:::::::0 00:::::::::::::00    00:::::::::00        000000000     ''',

    '1': '''  1111111    1::::::1   1:::::::1   111:::::1      1::::1      1::::1      1::::1      1::::l      1::::l      1::::l      1::::l      1::::l   111::::::1111::::::::::11::::::::::1111111111111''',

    '2': ''' 222222222222222    2:::::::::::::::22  2::::::222222:::::2 2222222     2:::::2             2:::::2             2:::::2          2222::::2      22222::::::22     22::::::::222      2:::::22222        2:::::2             2:::::2             2:::::2       2222222::::::2222222:::::22::::::::::::::::::222222222222222222222''',

    '3': ''' 333333333333333   3:::::::::::::::33 3::::::33333::::::33333333     3:::::3            3:::::3            3:::::3    33333333:::::3     3:::::::::::3      33333333:::::3             3:::::3            3:::::3            3:::::33333333     3:::::33::::::33333::::::33:::::::::::::::33  333333333333333   ''',

    '4': '''       444444444        4::::::::4       4:::::::::4      4::::44::::4     4::::4 4::::4    4::::4  4::::4   4::::4   4::::4  4::::444444::::4444::::::::::::::::44444444444:::::444          4::::4            4::::4            4::::4          44::::::44        4::::::::4        4444444444''',

    '5': '''555555555555555555 5::::::::::::::::5 5::::::::::::::::5 5:::::555555555555 5:::::5            5:::::5            5:::::5555555555   5:::::::::::::::5  555555555555:::::5             5:::::5            5:::::55555555     5:::::55::::::55555::::::5 55:::::::::::::55    55:::::::::55        555555555     ''',

    '6': '''        66666666          6::::::6          6::::::6          6::::::6          6::::::6          6::::::6          6::::::6          6::::::::66666    6::::::::::::::66  6::::::66666:::::6 6:::::6     6:::::66:::::6     6:::::66::::::66666::::::6 66:::::::::::::66    66:::::::::66        666666666     ''',

    '7': '''777777777777777777777::::::::::::::::::77::::::::::::::::::7777777777777:::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           7::::::7           77777777            ''',

    '8': '''     888888888        88:::::::::88    88:::::::::::::88 8::::::88888::::::88:::::8     8:::::88:::::8     8:::::8 8:::::88888:::::8   8:::::::::::::8   8:::::88888:::::8 8:::::8     8:::::88:::::8     8:::::88:::::8     8:::::88::::::88888::::::8 88:::::::::::::88    88:::::::::88        888888888     ''',

    '9': '''     999999999        99:::::::::99    99:::::::::::::99 9::::::99999::::::99:::::9     9:::::99:::::9     9:::::9 9:::::99999::::::9  99::::::::::::::9    99999::::::::9          9::::::9          9::::::9          9::::::9          9::::::9          9::::::9          9::::::9          99999999        ''',

    ':': '''                        ::::::::::::::::::                  ::::::::::::::::::                  '''
    }

# Width of all ascii art charachters
_ascii_charachter_len = {'0': 19,
                     '1': 12,
                     '2': 20,
                     '3': 19,
                     '4': 18,
                     '5': 19,
                     '6': 19,
                     '7': 20,
                     '8': 19,
                     '9': 19,
                     ':': 6}

# Functions
def get_target_date() -> datetime:
    '''Take target dateime from user.'''

    needed_inputs = ('Year', 'Month', 'Day', 'Hour', 'Minute', 'Second')
    taken_inputs = []

    # Take inputs as long as needed
    while len(taken_inputs) < len(needed_inputs):
        user_input = input(f'{needed_inputs[len(taken_inputs)]}: ')

        if not user_input.isdigit():
            print('Invalid input!')
            continue

        taken_inputs.append(int(user_input))

    # Attempt creating datetime object with current inputs
    try:
        target_time = datetime(*taken_inputs)

    # One or more inputs invalid. Function calls itself recursivly until all inputs are valid
    except ValueError as e:
        print(f'Invalid inputs: {e}\n')
        target_time = get_target_date()

    return target_time

def main():
    '''Main function'''

    target_time = get_target_date()
    current_time = datetime.now()

    # Run until hitting target time
    while current_time <= target_time:

        # Sleep until next second
        time.sleep((999_999 - current_time.microsecond)/1_000_000)

        # Refresh current time
        current_time = datetime.now()

        # Calculate delta
        delta = target_time - current_time

        # Create countdown str with regular charachters to convert into ascii art
        timer = f'{delta.days}:{delta.seconds // 3_600:02}:{(delta.seconds % 3_600) // 60:02}:{(delta.seconds % 3_600) % 60:02}'

        countdown = ''

        # Create the str with all ascii art combined
        # Eeach letter is 16 charachters tall width warying widths. To create the final string each
        # row has to be put together, to then merged into the final string
        for row in range(16):
            # Go every charachter that has to be added
            for charachter in timer:
                ascii_num = _ascii_charachters[charachter]
                numb_len = _ascii_charachter_len[charachter]

                # Get the ascii art for a number at the current row and add it together with two
                # whitespaces
                countdown += f'{ascii_num[row * numb_len:row * numb_len + numb_len]}  '

            # Add newlines after each completed row of charachters
            countdown += '\n'

        # Clear terminal and print countdown
        os.system('cls')
        print(countdown)

if __name__ == '__main__':
    main()
