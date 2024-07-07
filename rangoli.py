def print_rangoli(size):
    alphabet_list = [chr(x) for x in range(97, size+97)]
    alphabet_list.sort(reverse=True)
    alphabet_string = "".join(alphabet_list)
    
    result_string = []
    #upper rangoli
    for i in range(size):
        if i == 0:
            result_string.append(alphabet_string[0])
        else:
            string = alphabet_string[0:1+i]
            reverse_string = string[::-1]
            string += reverse_string[1:]
            result_string.append(string)
            
    #bottom rangoli
    bottom = result_string[0:-1].copy()
    bottom.sort(key=len, reverse=True)
    
    result_string.extend(bottom)
    
    justify_center = lambda x : x.center(width,'-')
    
    result_list = list(map(list, result_string))
    result_dashed = list(map("-".join, result_list))
    width = max(len(x) for x in result_dashed)
    result_formated = list(map(justify_center, result_dashed))
    end_result = "\n".join(result_formated)
    
    print(end_result)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
