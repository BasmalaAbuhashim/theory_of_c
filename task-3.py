def Tm(str):
    tape = list(str)
    n = len(tape)
    if n % 4 != 0 or n == 0:
        return False
    blocck = n//4
    b_1 = str[0:blocck]
    b_2 = str[blocck:2 * blocck]
    b_3 = str[2 * blocck:3 * blocck]
    b_4 = str[3 * blocck:]
    if all(ch == '0' for ch in b_1) and all(ch == '1' for ch in b_2) and all(ch == '0' for ch in b_3) and all(ch == '1' for ch in b_4):
           return True
    return False


inp = ["0101", "00110011", "000111000111", "001101", "00011100011"]
for x in inp:
    val = Tm(x)
    print(f"{x} -> {'Accepted' if val else 'Rejected'}")
