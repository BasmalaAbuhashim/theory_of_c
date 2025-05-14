def pda(str):
    if len(str) % 2 == 0:
        return False
    stack = []
    state = "q0"
    i = 0
    n = len(str)
    mid = n//2
    while i<n:
        ch = str[i]
        if state == "q0":
            if i == mid:
                state = "q1"
            else:
                stack.append(ch)
                i+=1
        elif state == "q1":
            state = "q2"
            i+=1
        elif state == "q2":
            if not stack:
                return False
            topp = stack.pop()
            if topp != ch:
                return False
            i+=1
    return len(stack) == 0 and state == "q2"

inp = ["aba", "abba", "abcba", "a", "bbb", "abcd"]
for x in inp:
    print(f"{x} -> {'Accepted' if pda(x) else 'Rejected'}")