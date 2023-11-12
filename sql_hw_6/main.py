import sys

import connect as connector


MAX_QUERY_NUMBER = 12


def execute_query(query_text:str, parameters:tuple) -> list[tuple]:
    with connector.create_connection() as con:
        cur = con.cursor()
        cur.execute(query_text, parameters)
        return cur.fetchall()


def get_query_text(query_number:int) -> str:
    with open(f".\sql_queries\query_{query_number}.sql", "r") as fh:
        result = fh.read()
    
    return result


def account_parameters(query_text:str):
    param_set = set()

    new_list = query_text.split()
    
    for i in new_list:
        if i[0] == ":":
            param_set.add(i.replace(")", ""))
    
    return len(param_set)


def main():
    if len(sys.argv) > 1:
        # find query_number for reading file
        try:
            query_number = int(sys.argv[1])
        except ValueError:
            return "First parameter must be integer"
        
        # check for max query number
        if query_number > MAX_QUERY_NUMBER:
            return f"Number of query must be between 1 and {MAX_QUERY_NUMBER}"
        
        # get list of parameters for query wich user entered
        param_list = sys.argv[2:]

        query_text = get_query_text(query_number)
        
        if query_text:
            # get number of parameters, wich text of query has
            number_param = account_parameters(query_text)
            
            # check number of user parameters and number of parameters of query text
            if number_param < len(param_list):
                return f"You have entered too many parameters. You entered: {len(param_list)}; needed: {number_param}"
            elif number_param > len(param_list):
                return f"You have entered few parameters. You entered: {len(param_list)}; needed: {number_param}"
            
            result = execute_query(query_text, tuple(param_list))
        else:
            result = "Can't find query text"
    else:
        query_text = get_query_text(1)
    
    result = execute_query(query_text, tuple(param_list))

    return result




if __name__ == "__main__":
    print(main())
