#PROBLEM FROM:
#http://www.pythonchallenge.com/
#CASE I:	calc 2 ** 38
num = 2**38
#put that in url in place of 0, try placing 2**38 or 1 for fun.

#Case II:
#given a string convert it to a char plus 2, Caesar cipher.
st = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
st = st.lower()
lst = st.split()
nlst = []
MAX = ord('z')
MIN = ord('a')-1
EXTRAS=".()'"
message =""

def cnvrt(chrtr):
	tmp = ord(ch) + 2
	if tmp > MAX:
		tmp = MIN+(tmp-MAX)
	chrtr = chr(tmp)
	return chrtr

for word in lst:
    neword = ""
    for ch in word:
        if ch not in EXTRAS:
            ch = cnvrt(ch)
        neword = neword + ch
    message += neword+" "

with open("message.txt","w") as f:
	f.write(message)

# with open("message.txt") as f:
# 	print(f.read())

#Case II hint got from the message: use string.maketrans()

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)
str = st
#print(str.translate(trantab))

#cools this works too didnt know that!! now need to translate the url of the page this message was in:
url = "http://www.pythonchallenge.com/pc/def/map.html"
with open("messageURL.txt","w") as f:
	f.write(url.translate(trantab))

#Obviously that doesnot make sense, now just look at the html page name it changed from "map" to "ocr" lets try that with the original address.
#gave us the hintL2.txt

#next in L2.py