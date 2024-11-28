

#--------------------------------------------------------------------------------------------------

#task 12 Palindrome
def is_palindrome(s):
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
input_str = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is NOT a palindrome.")

#---------------------------------------------------------------------------------------------------------


#task 13 pascal Triangle 
def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle

# Example usage
n = int(input("Enter the number of rows: "))
triangle = generate_pascals_triangle(n)

# Displaying the triangle
for row in triangle:
    print(row)




