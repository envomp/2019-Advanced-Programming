try:
    while True:
        inp = [x.split(",") for x in input().split()]
        piano = inp[0]
        corners = inp[1:]
        for pair in corners:
            hypothenuse = (int(pair[0])**2 + int(pair[1])**2)**0.5
            pianotenuse = (int(piano[0])**2 + int(piano[1])**2)**0.5 / 2**0.2
            if hypothenuse > pianotenuse:
                print("Y", end="")
            else:
                print("N", end="")
        print()

except EOFError:
    exit()
