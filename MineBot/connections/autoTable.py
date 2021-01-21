'''
This package are created because i need an easy way to make tables in sqlite3 with a python program
If you want, you can change this package for change the data base or configurations
'''

def typeInt(fieldName='default', notNull=False, primaryKey=False, autoIncrement=False):

    # This function helps to create a table

    dbInstruction = f'{fieldName} INTEGER '

    # Field values
    if notNull:
        dbInstruction += 'NOT NULL '
    if primaryKey:
        dbInstruction += 'PRIMARY KEY '
    if autoIncrement:
        dbInstruction += 'AUTOINCREMENT'

    return dbInstruction

def typeStr(fieldName='default', notNull=False, primaryKey=False):

    # This function helps to create a table

    dbInstruction = f'{fieldName} '

    # Field values
    if notNull == True:
        dbInstruction += 'NOT NULL '
    if primaryKey == True:
        dbInstruction += 'PRIMARY KEY '

    return dbInstruction


def main():

    print(typeInt(fieldName='id', notNull=True,primaryKey=True, autoIncrement=True))
    print(typeStr(fieldName='name', notNull=True))


if __name__ == '__main__':
    main()
