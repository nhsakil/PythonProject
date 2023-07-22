service = "Hello Bob"
service1 = service.lower()
#print(service1)
type(service)
dir(service)
service2= service1.find("b")
print(len(service)*7)
print(service.capitalize())
print(service.replace("b","B"))

data = "Stephen from the coursera class stehn@gmail.com 12.24 GMT"
email = data.find("@")
spaceinText = data.find(" ", email)
getEmail = data[email+1:spaceinText]
print(getEmail)


text = "X-DSPAM-Confidence:    0.8475"
text1 = text.find(".")
text2= text[text1-1:text1+5]
print(float(text2))