name = 'The quick brown fox jumps over the lazy dog'
vowels = 'aeiou'

for comparator in vowels:
    count = 0
    for i in name:
        if i == comparator:
            count = count + 1

    print('comparator:' + str(count))
