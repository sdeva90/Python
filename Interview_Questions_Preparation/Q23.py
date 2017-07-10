# replace a character in a string
def textfill(text, symbol):
    a = text.replace(' ', symbol)
    print(a)

text = "san sou"
symbol = "$"
textfill(text, symbol)
# replace a character in a string model 2

def textfill(text, symbol):
    # a = text.replace(' ', symbol)
    s = list(text)
    d = []
    t =''
    # print(s)
    for i in s:
        if i == ' ':
            d.append(symbol)
        else:
            d.append(i)
    l = t.join(d)
    print(l)

text = "san sou end"
symbol = "$"
textfill(text, symbol)
