# Question 5: Exploring Logical Operations and Precedence

# Task 1: Validating Calculations

normal_arithmetic_expression = 10 + 5 * 10
print(normal_arithmetic_expression)
# "Normal" equals 60, because 10 times 5 is 50 plus 10 which is 60 (order of operations). 
normal_arithmetic_expression_with_parentheses = (10 + 5) * 10
print (normal_arithmetic_expression_with_parentheses)
# "With parentheses" equals 150, because 10 plus 5 is 15 and then times 10 which is 150.
# They do not match.

# Task 2: Mix and Match

mixed_expression = ((3 + 7) * 50) > ((3 + 7) * 25) and ((3 + 7) * 50) > ((3 + 7) * 10)
# I think the outcome will be true because 500 is "greater" than 250 "and" 500 is "greater" than 100.
print(mixed_expression)