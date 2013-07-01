def replace_space(s):
    res = ""
    for i in range(len(s)):
        if s[i] == " ":
            res += "%20"
        else:
            res += s[i]
    return res

if __name__ == "__main__":
    inp = raw_input().strip()
    print replace_space(inp)
