import string

letters = string.ascii_letters.upper()
reversed_letters = letters[::-1]
with open("blocks.txt","w")as f:

    for c in letters:
        f.write(f"{c} {reversed_letters[ord(c)-65]}\n")
    
    for c1 in letters:
        for c2 in letters:
            c = c1+c2
            p = reversed_letters[ord(c1)-65]+ reversed_letters[ord(c2)-65]
            f.write(f"{c} {p}\n")
    for c1 in letters:
        for c2 in letters:
            for c3 in letters:
                c = c1+c2+c3
                p  = reversed_letters[ord(c1)-65]+ reversed_letters[ord(c2)-65]+reversed_letters[ord(c3)-65]
                f.write(f"{c} {p}\n")
