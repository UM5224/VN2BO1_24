with open("Default.jpg","rb") as f1:
    with open("pic.jpg","wb") as f2:
        image = f1.read()
        f2.write(image)


with open("tree.png","rb") as file1:
    image2=file1.read()
with open("pic2.png","wb") as file2:
    file2.write(image2)
