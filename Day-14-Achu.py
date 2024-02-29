
def split_and_join(line):
    split_word=line.split(" ")
    join_word="-".join(split_word)
    return join_word



line = input()
result = split_and_join(line)
print(result)