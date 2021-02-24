from string import ascii_lowercase

def solution(new_id):

    answer = new_id.lower()
    check_list = list(ascii_lowercase) + list(map(str,range(10))) + ['-', '_', '.']

    answer = "".join([x for x in answer if x in check_list])

    for i in range(len(answer)-1,1,-1):
        if(answer[i] == '.' and answer[i-1] == '.'):
            answer = answer[:i-1] + answer[i:]
    answer = answer.strip('.')

    if (not answer):
        answer = 'aaa'
    elif (len(answer) > 15):
        answer = answer[0:15].rstrip('.')

    if(len(answer)<3):
        for i in range(len(answer),3):
            answer += answer[-1]

    return answer


new_id = ".asd....sa#^#d1...."
print(solution(new_id))
