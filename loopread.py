with open (r"C:\Users\hp\OneDrive\Documents\fileData.txt" , "r") as file:
    content = file.readlines()
    count = 0
    for i in content:
        count += 1
        print(count)
