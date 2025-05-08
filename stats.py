def number_of_words(text):
    word=text.split()
    return len(word)
def number_of_characters(text):
    dict={}
    for char in text:
        c_lower=char.lower()
        if c_lower in dict:
            dict[c_lower]+=1
        else:
            dict[c_lower]=1
    return dict
def list_of_chars(dic):
    list=[]
    for char in dic:
        if char.isalpha():
            list.append({"char": char, "num": dic[char]})
    list.sort(key=lambda x: x["num"], reverse=True)
    return list