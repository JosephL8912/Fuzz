from html.parser import HTMLParser #adding the parser and fuzz library
from pythonfuzz.main import PythonFuzz

f = open("crash.txt", "w")


@PythonFuzz
def fuzz(buf):
    attempt = ""
    print(buf)
    try: #try this code 
        attempt = buf.decode("ascii") 
        parser = HTMLParser() #create the html parse
        parser.feed(attempt) #feed string to parser
        thing = attempt.encode('ascii')
        f.write(str(thing) + " \n") #write bytes to file
    except UnicodeDecodeError: #create the exception 
        pass

#run the fuzz method
if __name__ == '__main__':
    fuzz()