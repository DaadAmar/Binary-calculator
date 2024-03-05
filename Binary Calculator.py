def is_valid_binary(number):
    return all(bit == '0' or bit == '1' for bit in number)


#  The function flips each bit in the binary string. All '0's become '1's,
# and all '1's become '0's, resulting in the one's complement of the binary number.

def ones_complement(binary):
    return ''.join('1' if bit == '0' else '0' for bit in binary)


#  This function takes a value that is one's complement and adds one to it making 
# it two's complement

def twos_complement(output1):
    binary_list = list(output1)
    index = len(binary_list) - 1
    carry = 1  
    while index >= 0 and carry > 0:
        sum_bit = int(binary_list[index]) + carry
        binary_list[index] = str(sum_bit % 2)
        carry = sum_bit // 2
        index -= 1
    if carry > 0:
        binary_list.insert(0, str(carry))
    result_binary = "".join(binary_list)
    return result_binary


def binary_addition(number_1, number_2):
    number_1 = str(number_1)
    number_2 = str(number_2)
    # Make both binary numbers of equal length by padding with zeros
    length = max(len(number_1), len(number_2))
    number_1 = number_1.zfill(length)
    number_2 = number_2.zfill(length)
    result = ""
    carry = 0

    for bit1, bit2 in zip(reversed(number_1), reversed(number_2)):
        # Perform binary addition for the current bits and the carry
        bit_sum = int(bit1) + int(bit2) + carry

        # Calculate the current result bit and update the carry
        result_bit = str(bit_sum % 2)
        carry = bit_sum // 2

        result = result_bit + result

    # If there is a carry after the iteration, prepend it to the result
    if carry:
        result = '1' + result

    return result


def binary_subtraction( number_1 , number_2 ):
    number_1 = str(number_1)
    number_2 = str(number_2)
    # Make both binary numbers of equal length by padding with zeros
    length = max(len(number_1), len(number_2))
    number_1 = number_1.zfill(length)
    number_2 = number_2.zfill(length)
    result = ""
    borrow = 0

    for bit1, bit2 in zip(reversed(number_1), reversed(number_2)):
        # Perform binary subtraction for the current bits and the borrow
        bit_diff = int(bit1) - int(bit2) - borrow

        # Adjust the borrow based on the current subtraction
        if bit_diff < 0:
            bit_diff += 2
            borrow = 1
        else:
            borrow = 0

        result_bit = str(bit_diff)

        # Prepend the result bit to the final result
        result = result_bit + result

    return result

def display_menu_1():
    print("\n** Binary Calculator **")
    print("A) Insert new numbers")
    print("B) Exit")

def display_menu_2():
    print("\n** Please select the operation **")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) Addition")
    print("D) Subtraction")

def main():
    while True:
        # Display the main menu
        display_menu_1()
        choice_1 = input("\nEnter your choice (A/B): ").upper()
        
        # Handle the user's choice in Menu 1
        if choice_1 == 'A':
            # Get the first binary number from the user
            number_1 = input("\nEnter the first binary number: ")
            
            # Validate the first binary number
            if not is_valid_binary(number_1):
                print("Invalid binary number. Please insert a valid binary number.")
                continue
            
            # Display the second menu for operations
            display_menu_2()
            choice_2 = input("\nEnter your choice (A/B/C/D): ").upper()
            
            # Perform the chosen operation based on the user's choice in Menu 2
            if choice_2 in ['A', 'B']:
                # If the operation is one's or two's complement
                if choice_2 == 'A':
                    result = ones_complement(number_1)
                else:
                    # For two's complement, compute one's complement first
                    number_1 = ones_complement(number_1)
                    result = twos_complement(number_1)

                print(f"Result: {result}")
            elif choice_2 in ['C', 'D']:
                # If the operation is addition or subtraction
                number_2 = input("\nEnter the second binary number: ")
                
                # Validate the second binary number
                if not is_valid_binary(number_2):
                    print("Invalid binary number. Please insert a valid binary number.")
                    continue

                if choice_2 == 'C':
                    result = binary_addition(number_1, number_2)
                    
                else:
                    result = binary_subtraction(number_1, number_2)

                print(f"Result: {result}")
            else:
                # Invalid choice in Menu 2
                print("Please select a valid choice.")
                
        elif choice_1 == 'B':
            # Exit the program if the user chooses to exit
            print("Exiting program.")
            break
        
        else:
            # Invalid choice in Menu 1
            print("Please select a valid choice.")
            

# Run the main function
main()
