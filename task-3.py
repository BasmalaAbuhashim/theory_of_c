def Tm(str):
    tape = list(str)
    n = len(tape)
    while True:
        try:
            i_0 = tape.index('0')
            tape[i_0] = 'X'
        except ValueError:
            break

        try:
            i_1 = tape.index('1')
            tape[i_1] = 'Y'
        except ValueError:
            return False
        
        try:
            i_2 = tape.index('0')
            tape[i_2] = 'Z'
        except ValueError:
            return False

        try:
            i_3 = tape.index('1')
            tape[i_3] = 'K'
        except ValueError:
            return False
    
    for ch in tape:
        if ch not in {'X','Y','Z','K'}:
            return False
    return True
inp = ["0101", "00110011", "000111000111", "001101", "00011100011"]
for x in inp:
    val = Tm(x)
    print(f"{x} -> {'Accepted' if val else 'Rejected'}")