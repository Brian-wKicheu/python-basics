while True:
    my_string = str(input("Enter a String\n"))

    if my_string == "Exit":
        break
    string_list = []

    #create a reversed list  out of the string
    for i in range(0, len(my_string)):
        string_list.append(my_string[ (len(my_string)-i) -1 ])

    #compare
    reversed_string = "".join(string_list)

    if reversed_string == my_string:
        print("Palindrome")
    else:
        print("Not palindrome")
