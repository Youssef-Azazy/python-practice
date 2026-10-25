# HackerRank - Python > Strings

# String Split and Join
# Input:  "this is a string"
# Output: "this-is-a-string"
# split() makes a list of words, then "-".join(list) puts "-" between them.
def split_and_join(line):
    return "-".join(line.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
