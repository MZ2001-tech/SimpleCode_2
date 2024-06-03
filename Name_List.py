

def main():
 number  = int(input("Enter Number of Name: "))
 NumList = []
 NumList.append(number) 

 NameList = []
 for _ in range(number):
   name =  input("Enter The Name: ")
   NameList.append(name)

 List(NumList, NameList)

 print(f"There a a total of {NumList[0]} .")
 print(f"These are the List Generated : {NameList}") 

def List(NumList, NameList):
 for i in range(len(NameList)):
  print("Name: ", NameList[i])

if __name__ == "__main__":
    main()
