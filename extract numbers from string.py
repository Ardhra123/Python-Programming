def extractMax(input):
 
     
     numbers = re.findall('\d+',input)
 
     numbers = map(int,numbers)
 
     print max(numbers)
 

if __name__ == "__main__":
    input = '236790trgboijdfuh'
    extractMax(input)
