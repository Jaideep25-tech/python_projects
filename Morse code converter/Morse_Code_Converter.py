def translate(sentence):
    translation = " "
    for letter in sentence:
        if letter in "Aa":
            translation = translation + " .- "
        elif letter in "Bb":
            translation = translation + " -... "
        elif letter in "Cc":
            translation = translation + " -.-. "
        elif letter in "Dd":
            translation = translation + " -.. "
        elif letter in "Ee":
            translation = translation + " . "
        elif letter in "Ff":
            translation = translation + " ..-. "
        elif letter in "Gg":
            translation = translation + " --. "
        elif letter in "Hh":
            translation = translation + " .... "
        elif letter in "Ii":
            translation = translation + " .. "
        elif letter in "Jj":
            translation = translation + " .--- "
        elif letter in "Kk":
            translation = translation + " -.- "
        elif letter in "Ll":
            translation = translation + " .-.. "
        elif letter in "Mm":
            translation = translation + " -- "
        elif letter in "Nn":
            translation = translation + " -. "
        elif letter in "Oo":
            translation = translation + " --- "
        elif letter in "Pp":
            translation = translation + " .--. "
        elif letter in "Qq":
            translation = translation + " --.- "
        elif letter in "Rr":
            translation = translation + " .-. "
        elif letter in "Ss":
            translation = translation + " ... "
        elif letter in "Tt":
            translation = translation + " - "
        elif letter in "Uu":
            translation = translation + " ..- "
        elif letter in "Vv":
            translation = translation + " ...- "
        elif letter in "Ww":
            translation = translation + " .-- "
        elif letter in "Ww":
            translation = translation + " .-- "
        elif letter in "Xx":
            translation = translation + " -..- "
        elif letter in "Yy":
            translation = translation + " -.-- "
        elif letter in "Zz":
            translation = translation + " --.. "
        elif letter in "1":
            translation = translation + " .---- "
        elif letter in "2":
            translation = translation + " ..--- "
        elif letter in "3":
            translation = translation + " ...-- "
        elif letter in "4":
            translation = translation + " ....- "
        elif letter in "5":
            translation = translation + " ..... "
        elif letter in "6":
            translation = translation + " -.... "
        elif letter in "7":
            translation = translation + " --... "
        elif letter in "8":
            translation = translation + " ---.. "
        elif letter in "9":
            translation = translation + " ----. "
        elif letter in "0":
            translation = translation + " ----- "
        elif letter in "?":
            translation = translation + " ..--.. "
        elif letter in "!":
            translation = translation + " -.-.-- "
        elif letter in ".":
            translation = translation + " .-.-.- "
        elif letter in ",":
            translation = translation + " --..-- "
        elif letter in ";":
            translation = translation + " -.-.-. "
        elif letter in ":":
            translation = translation + " ---... "
        elif letter in "+":
            translation = translation + " .-.-. "
        elif letter in "-":
            translation = translation + " -....- "
        elif letter in "/":
            translation = translation + " -..-. "
        elif letter in "=":
            translation = translation + " -...- "
        
        
        else:
            translation = translation + letter
    return translation
        
print(translate(input('''Enter the phrase which
you want to convert into "morse code":-\n''')))
