if __name__ == "__main__":
    inp = raw_input().strip()
    b_arr = []
    for i in range(256):
        b_arr.append(0)
    for x in range(len(inp)):
        if b_arr[ord(inp[x])]:
            print "Non-unique - Repeated character ", inp[x], " at position  ",x
            break
        else:
            b_arr[ord(inp[x])] = 1

