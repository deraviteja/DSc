def find_winner(ar):

    winner = []

    if (ar[0] == ar[1]) and (ar[1] == ar[2]):
        winner.append(ar[1])
    if (ar[3] == ar[4]) and (ar[4] == ar[5]):
        winner.append(ar[3])
    if (ar[6] == ar[7]) and (ar[7] == ar[8]):
        winner.append(ar[6])
    if (ar[0] == ar[4]) and (ar[4] == ar[8]):
        winner.append(ar[0])
    if (ar[2] == ar[4]) and (ar[4] == ar[6]):
        winner.append(ar[2])
    if (ar[0] == ar[3]) and (ar[3] == ar[6]):
        winner.append(ar[0])
    if (ar[1] == ar[4]) and (ar[4] == ar[7]):
        winner.append(ar[1])
    if (ar[2] == ar[5]) and (ar[5] == ar[8]):
        winner.append(ar[2])

    return winner


def check_validity(ar, winner, invalid, valid):

    if '.' in ar:  # check if game is over early ==> there is a winner

        if ar.count('o') == ar.count('x'):  # indicates 'o' must be the only winner

            if 'o' in winner:  # check if 'x' is also a winner

                if 'x' not in winner:  # now its a valid case
                    print valid
                else:  # else its invalid
                    print invalid

            else:  # 'o' dint win so invalid
                print invalid

        elif (ar.count('o') == (ar.count('x') - 1)):  # check if 'x' is the only winner

            if 'x' in winner:

                if 'o' not in winner:  # valid case
                    print valid
                else:
                    print invalid

            else:  # 'x' did not be the winner
                print invalid

        else:
            print invalid

    else:

        if (ar.count('o') == 4) and (ar.count('x') == 5):  #

            if 'o' in winner:
                print invalid
            else:
                print valid

        else:
            print invalid


invalid = "invalid"
valid = "valid"

while 1:
    inp = (raw_input())
    if inp == 'end':
        break
    ar = list(inp)

    for i in range(len(ar)):
        if ar[i] is 'X':
            ar[i] = 'x'
        if ar[i] is 'O':
            ar[i] = 'o'


    winner = find_winner(ar)
    check_validity(ar,winner,invalid,valid)




