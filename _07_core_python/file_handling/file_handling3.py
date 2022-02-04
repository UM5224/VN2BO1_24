with open("one.html","w") as f:
    f.write("<html>\n<head>\n<title>NameOfUrl \
           </title>\n</head>\n <body><h1>HomePage</h1>\
            \n</body></html>")


with open("one.html","r") as f:
    print(f.read())