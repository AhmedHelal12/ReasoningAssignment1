
# A represents for all
# E represents there exists


import re

def eliminate_implification(exp):
    temp1=re.sub(r'->',r'|',exp)
    temp2=re.sub(r'<=>',r'&',temp1)
    return temp2

# Example usage
# input_expression = "(P->Q) & (~(Q->R)) <=> (P->R)"
# result = eliminate_implification(input_expression)
# print("Result after elimination:", result)







def move_negation(exp):
    # Move negations inward for conjunction (AND) expressions
    temp1 = re.sub(r'~\((\w+)&(\w+)\)', r'(~\1|~\2)', exp)
    # Move negations inward for disjunction (OR) expressions
    temp2 = re.sub(r'~\((\w+)\|(\w+)\)', r'(~\1&~\2)', temp1)
    # Replace A with E 
    temp3 = re.sub(r'~Ax:(\w+)', r'Ex:~\1', temp2)

    # Replace E with A 
    temp4 = re.sub(r'~Ex:(\w+)', r'Ax:~\1', temp3)

    return temp4

# Example usage
# input_expression = "(~P&Q) | ~(R&S) ~Ax:P"
# result = move_negation(input_expression)
# print("Result after moving negations inward and replacing quantifiers:", result)

def remove_double_not(exp):
    temp1=re.sub(r'~~(\w+)',r'\1',exp)
    print(temp1)
    return temp1

# input_expression="~~B ~~C"
# result=remove_double_not(input_expression)
# print('Result after removing the double not:',result)

def standardize_variable(exp):


    temp1 = re.sub(r'(\w+)(.+)(\1)', r'\1\2n', exp)
    return temp1

# Example usage
# input_expression = "P(x) & Q(x)"
# result = standardize_variable(input_expression)
# print("Result after standardizing variables:", result)



def to_prenex_normal_form(exp):
    # Find all quantified expressions (A and E followed by a variable and a formula)
    quantified_expressions = re.findall(r'\b(A|E)(\w+)', exp)
    
    # Reorder quantified expressions to appear at the beginning of the string
    reordered_exp = ''.join(f'{quant[0]}{quant[1]}' for quant in quantified_expressions)
    temp = re.sub(r'\b(A|E)(\w+)', '', exp)
    print(temp)
    # remove :
    remaining_exp=re.sub(r':','',temp)
    # Combine reordered quantified expressions and the remaining expression
    prenex_normal_form = reordered_exp + remaining_exp
    return prenex_normal_form

# # Example usage
# input_expression = "Ez: Px & Ay: Qy"
# result = to_prenex_normal_form(input_expression)
# print("Prenex normal form:", result)

def skolemization(exp):
    # Define a lambda function to generate a character not present in the string
    generate_new_char = lambda s: next(
        letter for letter in "abcdefghijklmnopqrstuvwxyz" if letter not in s
    )

    # Apply Skolemization by replacing existential quantifiers with new characters
    temp1 = re.sub(r'Ex(\w+)(\(\w+\))', lambda match: match.group(1) + generate_new_char(exp) , exp)
    return temp1

# Example usage
input_expression = "ExP(x) EyZ(y)"
result = skolemization(input_expression)
print("Skolemized expression:", result)