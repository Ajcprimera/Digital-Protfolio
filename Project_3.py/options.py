import convertion as cv

def matrix_options(user_selection):
    while True:
        try:
            if user_selection == 1:
                while True:
                    try:
                        rows = int(input('Input the number of rows'))
                        columns = int(input('Input the number of columns'))
                        selection = cv.convertion_u(rows, columns)
                        break
                    except ValueError:
                        print('This value is not a number')
            elif user_selection == 2:
                while True:
                    try:
                        rows = int(input('Input the number of rows'))
                        columns = int(input('Input the number of columns'))
                        selection = cv.convertion_r(rows, columns)
                        return selection
                    except ValueError:
                        print('This value is not a number')
            elif user_selection != 1 and user_selection != 2:
                raise Exception ('This option is not valid')
        except Exception as error:
            print(error)

s = matrix_options(2)
print(s)