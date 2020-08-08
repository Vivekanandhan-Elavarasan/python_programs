# Task 2:
# Write a function called is sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume(as a
#                                                                              precondition) that the elements of the list can be compared with the relational
# operators <, > , etc.
# For example, is_sorted([1, 2, 2]) should return True and is_sorted(['b', 'a']) should
# return False

def is_sorted(arr):
    for x in range(1, len(arr)):
        if arr[x] < arr[x-1]:
            return False
    return True


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))

# Task-3:
# Write a program that finds all the reverse pairs in the word list. Two words are a
# “reverse pair” if each is the reverse of the other.


def reverse_pairs(arr):
    for i in range(0, len(arr)):
        rev = arr[i][::-1]
        if rev in arr[i+1:]:
            print(arr[i], rev)


reverse_pairs(["vba", "ccc", "lkjh", "abv", "hjkl"])

# Task-4:
# Write a program that finds all of the metathesis pairs in the dictionary. Two
# words form a “metathesis pair” if you can transform one into the other by
# swapping two letters
# for example, “converse” and “conserve.”
# Hint: don’t test all pairs of words, and don’t test all possibleswaps.


def can_swap(w1, w2):
    swaps = 2
    for i in range(0, len(w1)):
        if w1[i] != w2[i]:
            swaps -= 1
    if swaps != 0:
        return False
    return True


def metathesis_print(arr):
    ana_dict = {}
    for w in arr:
        r_w = "".join(sorted(w))
        if r_w in ana_dict:
            for a_w in ana_dict[r_w]:
                if can_swap(w, a_w):
                    print(w, a_w)
            ana_dict[r_w].append(w)
        else:
            ana_dict[r_w] = [w]


metathesis_print(['converse', 'conserve', 'conserev',
                  'dad', 'dda', 'abc', 'zzz', 'cba'])