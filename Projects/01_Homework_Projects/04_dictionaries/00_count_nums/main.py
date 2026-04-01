"""This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the 
information.

An example run of the program looks like this (user input is in blue):"""



user_numbers =  []
def asking_number():
   while True:
        
        number = input ("Enter a number ")
        if number == "":
            break
        user_numbers.append(number)
   return(user_numbers)




num_dict = {}    
def count_numbers(numbersssss):
  for num in numbersssss:
      if num not in num_dict:
         num_dict[num] = 1 
      else :
         num_dict[num] +=1  
  return num_dict

   
def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """  
    print(num_dict)
    # for num in num_dict:
    #     print(str(num) + " appears " + str(num_dict[num]) + " times.")
    
    for key,value in num_dict.items():
        print (f"{key} has appeared {value} times")


def main():
   prompt = asking_number()
   value = count_numbers(prompt)
   print_counts(value)


if __name__ == "__main__":
    main()
