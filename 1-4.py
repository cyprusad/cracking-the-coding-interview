if __name__ == "__main__":
    inp = raw_input().strip().split()
    if len(inp[0]) != len(inp[1]):
        print "Not anagram"
    if ''.join(sorted(inp[0])) == ''.join(sorted(inp[1])):
        print "Anagram"

    # Other option is to use dictionaries, similar to previous problems
