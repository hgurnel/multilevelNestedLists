import re
import ast
import math


# ----- CHECK INPUT NUMBER OF LINES (int) N > 0 -----

N_str = input() 
N = int(N_str)

def checkNbLines(nbLines):
    if isinstance(nbLines, int) and nbLines > 0:
        return True
    else:
        return False

# ----- CHECK FORMAT OF INPUT LINE ----- 
        
line_list = []
for i in range(N):
    line = input()
    line_list.append(line)        

           
def checkStringFormat(str):
    str_split = str.split();
    # pattern = re.compile("\-\-[a-z][+-]?[0-9]+\=(([+-]?[0-9]+\.?\d*)|(\[([^a-z]*)\])|(\[\]))", flags=re.IGNORECASE)
    pattern = re.compile("\-\-[a-z]([+-]?[0-9]+\.?\d*)\=(([+-]?[0-9]+\.?\d*)|(\[([^a-z]*)\])|(\[\]))", flags=re.IGNORECASE)
    
    for id in range(len(str_split)):
        match = pattern.match(str_split[id])
        is_match = bool(match)
        if is_match == False:
            break;
    
    return is_match
    
def checkInputLine(input):
    for item in range(len(input)):
        if not checkStringFormat(input[item]):
            return False
    return True

# ----- COMPUTE AVERAGE OF EACH OF THE N LINES and place result in list -----

all_lines_average_list = []

if checkNbLines(N):

    # __FOR__BEGIN
    
    for i in range(len(line_list)):
        
        # __IF__BEGIN        
        
        if not checkInputLine(line_list):            
            all_lines_average_list.append(["ERROR"])            
        else:
        
            # ----- EXTRACT THE VALUES FROM THE INPUT LINE & PLACE THEM IN A LIST -----
            
            # Remove blank spaces from input line number i
            line_no_spaces_str = line_list[i].replace(" ", "")
            
            # Add -- at the end of the line to have the same string pattern around the 
            # values of the line
            line_no_spaces_str += "--"
            
            # Get the values, which are all between = and -- and place them in a list
            def getValuesBetweenPattern(str, lst):
                for i in re.findall('\=(.*?)\-\-', str, re.S):
                    lst.append(i)
            
            line_no_spaces_list = []        
            getValuesBetweenPattern(line_no_spaces_str, line_no_spaces_list)
            
            # ----- TURN THE LIST (still in string format) INTO NESTED LISTS -----
            
            def getNestedLists(not_nested_lst, nested_lst):
                for j in not_nested_lst:
                    nested_lst.append(ast.literal_eval(j))
            
            values_nested_lists = []
            getNestedLists(line_no_spaces_list, values_nested_lists)
            
            # ----- COMPUTE AVERAGE OF EACH ELEMENT OF values_nested_lists -----
            
            def roundNumber(num):
                if isinstance(num, int):
                    return num
                else:
                    # If num is float, check its decimal part.
                    if(math.modf(num)[0] == 0):
                        return int(num)
                    else:
                        return round(num, 2)
            
            def averageOfOneNestedList(lst):
                sum = 0
                count = 0
                
                for i in lst:
                    if isinstance(i, list):
                        # Empty list: add nothing to sum but increase counter
                        if len(i) == 0:
                            count += 1
                        else:
                            sum += averageOfOneNestedList(i)
                            count += 1
                    else:
                        sum += i
                        count += 1
                
                average = sum / count
                # Round the average
                return roundNumber(average)
                
            
            def averageList(lst):
                for i in values_nested_lists:
                    if isinstance(i, list):
                        if len(i) == 0:
                            average_list.append(0)
                        else:
                            average_list.append(averageOfOneNestedList(i))
                    else:
                        # Round the number        
                        average_list.append(roundNumber(i))
            
            average_list = []
            averageList(average_list)
            
            all_lines_average_list.append(average_list)        
            
        # __IF__END
    
    # __FOR__END
            
            
    # ----- OUTPUT -----
 
    for i in range(len(line_list)):
        for j in all_lines_average_list[i]:
            print(j, end=" ")
        print("\r")   

else:
    print("ERROR")