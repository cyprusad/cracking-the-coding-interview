def remove_dups(s):
    res = ""
    d = dict()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
            res += s[i]
    return res

def filtr(s, ch):
    res = ""
    for x in range(len(s)):
        if s[x] != ch:
            res += s[x]
    return res

def remove_dups2(s):
    if s == "":
        return ""
    else:
        return s[0] + remove_dups2(filtr(s[1:], s[0]))

if __name__ == "__main__":
    inp = raw_input().strip()
    print remove_dups2(inp)

