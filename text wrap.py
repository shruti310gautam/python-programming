#You are given a string S and width w .
#Your task is to wrap the string into a paragraph of width, w .

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    

