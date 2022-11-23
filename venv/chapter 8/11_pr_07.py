# this="        ,,,,,,,,,        dada,,,,,,,,,,,,           "
# print(this)
# print(this.strip())


def remove_and_split(string,word):
    newStr= string.replace(word," ")
    return newStr.strip()

this="  sumit dada   sumitdada         "
n=remove_and_split(this,"sumit")
print(n)