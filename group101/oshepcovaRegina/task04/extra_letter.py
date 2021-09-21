def extra_letter(string_1: str, string_2: str):
    for i in string_2:
        if i not in string_1:
            return i
        elif not(string_1.count(i) == string_2.count(i)):
            return i

print(extra_letter('abbba', 'abbba'))