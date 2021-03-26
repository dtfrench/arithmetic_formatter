def arithmetic_arranger(problems, true_or_false=False):

  # Return error if more than 5 problems.
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # Iterate through each problem passed into the function.
  digit_problem = []
  for problem in problems:

      problem = problem.split()
      
      # Return error if the operator is not plus or minus.
      if ((problem[1] != '+') and (problem[1] != '-')):
        return "Error: Operator must be '+' or '-'."

      # Return error if either operand has more than four digits.
      elif ((len(problem[0]) > 4) or (len(problem[2]) > 4)):
        return "Error: Numbers cannot be more than four digits."

      else:
          # Try converting operands to ints. If that fails return error.
          for position in problem:
            if (position != '+' and position != '-'):
              try:
                position = int(position)

              except:
                return "Error: Numbers must only contain digits."
          
          # Add the problem to the digit_problem list.
          digit_problem.append(problem)


  top_string = ''
  middle_string = ''
  bottom_string = ''
  solution = ''

  # Iterate through each problem in digit_problem list.
  for problem in digit_problem:

    # Check if first operand is longer than second operand. 
    if (len(problem[0]) > len(problem[2])):

      #If first operand is longer its length will be used.
      use_length = len(problem[0])

      # Right-align first operand and append it top_string variable.
      # along with four spaces to separate problems. 
      top_number = problem[0].rjust(use_length + 2)
      top_string = top_string + top_number + "    "

      # Establish the length betweeen the operator and the second operand
      # using the length of the first operand. 
      lower_length = len(problem[2])
      space_length = (use_length + 1) - lower_length
      
      spacer = ''
      i = 0
      while (i < space_length):
        spacer = spacer + " "
        i = i + 1
      
      # Append the operator, space, and second operand to the middle_string variable.
      middle_string = middle_string + problem[1] + spacer +  problem[2] + "    "
      
      # Use the length of the first operand to calculate the number of '-'s used to
      # underline the equation. Append '-'s and four spaces to the bottom_string variable. 
      underliner = '-'.rjust(use_length + 2, '-')
      bottom_string = bottom_string + underliner + "    "

    # Check if the second operand is longer than the first operand
    elif(len(problem[2]) >= len(problem[0])):

      #If the second operand is longer its length will be used.
      use_length = len(problem[2])

      # Right-align the first operand and append it to the top_string variable
      # along with four spaces to separate the equations.
      top_number = problem[0].rjust(use_length + 2)
      top_string = top_string + top_number + "    "

      # Establish the length betweeen the operator and the second operand
      # using the length of first operand.
      lower_length = len(problem[0])
      space_length = 1

      spacer = ''
      i = 0
      while (i < space_length):
        spacer = spacer + " "
        i = i + 1
      
      # Append the operator, space, and second operand to the middle_string variable
      # along with four spaces.
      middle_string = middle_string + problem[1] + spacer +  problem[2] + "    "
      
      # Use the length of the second operand to calculate the number of '-'s used to
      # underline the equation. Append '-'s and four spaces to the bottom_string variable.
      underliner = '-'.rjust(use_length + 2, '-')
      bottom_string = bottom_string + underliner + "    "

    # If the operator is a plus, add the operands together and add the result 
    # to the solution string as a right-aligned string along with four spaces.
    if (problem[1] == "+"):
      equals = int(problem[0]) + int(problem[2])
      solution_space = len(underliner)
      equals_justified = str(equals).rjust(solution_space)
      solution = solution + equals_justified + "    "
    
    # If the operator is a minus, subtract second operand from first and add  the result
    # to the solution string as a right-aligned string along with four spaces. 
    elif (problem[1] == "-"):
      equals = int(problem[0]) - int(problem[2])
      solution_space = len(underliner)
      equals_justified = str(equals).rjust(solution_space)
      solution = solution + equals_justified + "    "
  
  # If True is passed into the function, return the formatted string
  # without the solution.
  if (true_or_false == False):
    arranged_string = top_string.rstrip() + "\n" + middle_string.rstrip() + "\n" + bottom_string.rstrip()
  
  # If False is passed into the function, return the formatted string
  # with the solution.
  elif (true_or_false == True):
    arranged_string = top_string.rstrip() + "\n" + middle_string.rstrip() + "\n" + bottom_string.rstrip() + "\n" + solution.rstrip()

  #Return the complete, formatted string.
  return arranged_string
