data = {'jim': 'is a fraud', 'jane': 'is alive', 'bob': 'is cool'}


def function_in(search_name, search_type, data):
    if search_name in data:
        #print(search_name, search_type)
        #print('Found')
        return True

    elif search_name not in data:
        print(search_name, search_type)
        #print('Not found')
        return False


if __name__ == "__main__":

    print(function_in('bob', 'is cool', data))
    print(function_in('jack', 'is a fraud', data))
    print(function_in('jim', 'is a fraud', data))
