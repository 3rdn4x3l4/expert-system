def remove_charset(string, charset):
    '''
    return a copy of string without chars from charset
    '''
    copy = ''
    for i in range(len(string)):
        if not string[i] in charset:
            copy = copy + string[i]
    return(copy)

def get_query(lines):
    '''
    take the lines of the files and return the query if it is unique
    meaning only one line of query
    '''
    query = []
    for i in range(len(lines) - 1,0,-1):
        if lines[i][:1] == '?':
            query.append(lines[i][1:])

    lenq = len(query)
    if lenq != 1:
        if lenq == 0:
            print('No query found')
        else:
            print('Only one query can be processed')
        exit()

    query = query[0]
    if query.isalpha() and query.isupper():
        print('query found', query)
        return (query)
    print('Incorrect query')

def get_knowledge(lines):
    '''
    take the lines of the files and return the knowledge if it is unique
    meaning only one line of knowledge
    '''
    knowledge = []
    for i in range(len(lines) - 1,0,-1):
        if lines[i][:1] == '=':
            knowledge.append(lines[i][1:])

    lenk = len(knowledge)
    if lenk != 1:
        if lenk == 0:
            print('No knowledge found')
        else:
            print('Only one knowledge can be true')
        exit()

    knowledge = knowledge[0]
    if knowledge.isalpha() and knowledge.isupper():
        print('knowledge found', knowledge)
        return (knowledge)
    print('Incorrect knowledge')

def get_propositions(lines):
    '''
    take the lines of the files and return the propositions
    '''
    return(lines)
