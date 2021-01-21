
'''
This package are created because i need an easy way to make tables in sqlite3 with a python program
If you want, you can change this package for change the data base or configurations
'''
import sqlite3


class sqliteManage():
    # Class than create and manage the db connections

    def __init__(self, dbName: str):
        # connection with the database

        self.dbName = dbName
        self.connection = sqlite3.connect(dbName)
        self.cursor = self.connection.cursor()

        print(f'The connection with {dbName} has ben created')

        self.connection.close()


    def startConnection(self):
        # This method open the connection with the database

        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor()

        print(f'The connection with {self.dbName} has ben opened')

    def closeConnection(self):
        # This method can close the connection with the database

        self.connection.close()

        print(f'The connection with {self.dbName} has ben closed')


    def createTable(self, tableName: str, dbTableFields: tuple):
        # Method for create a table

        dbInstruction = f"CREATE TABLE {tableName} ("
        numberValues = len(dbTableFields) - 1

        for field in dbTableFields:
            dbInstruction += field

            numberValues -= 1
            if numberValues >= 0:
                dbInstruction += ','

        dbInstruction += ');'

        # Execute an sql instruction
        self.cursor.execute(dbInstruction)
        # Save the changes
        self.connection.commit()

        print(
            f'The table {tableName} has ben created in {self.dbName}\n{dbInstruction}')


    def insertElement(self, tableName='', elements=('',), values=('',)):
        # This method insert elements in an existen database

        dbInstruction = f"INSERT INTO {tableName} ("

        numberValues = len(elements) - 1

        for element in elements:
            dbInstruction += element
            numberValues -= 1

            if numberValues >= 0:
                dbInstruction += ', '

        dbInstruction += ') VALUES ('
        numberValues = len(values) - 1

        for value in values:
            dbInstruction += value

            numberValues -= 1
            if numberValues >= 0:
                dbInstruction += ', '

        dbInstruction += ');'

        # Execute an sql instruction
        self.cursor.execute(dbInstruction)
        # Save the changes
        self.connection.commit()
        print(f'An element has ben inserted in {tableName} \n{dbInstruction}')

    
    def selectElements(self, tableName='', tableElements= ('',), filterwhere=('',), fetchOne= False, operator=''):
        # This method can select data from a table in a database

        dbInstruction = 'SELECT '

        numberValues = len(tableElements) - 1

        for element in tableElements:
            dbInstruction += element + ' '
            numberValues -= 1

            if numberValues >=0:
                dbInstruction += ', '
        
        dbInstruction += f"FROM {tableName} "

        if not filterwhere == ('',):
            dbInstruction += 'WHERE '
            numberValues = len(filterwhere) - 1

            for where in filterwhere:
                dbInstruction += where + ' '
                numberValues -= 1
                if numberValues >=0:
                    dbInstruction += operator + ' '

        dbInstruction += ';'

        self.cursor.execute(dbInstruction)

        #The next code select the method 'fetchone()' or 'fetchall()'
        if fetchOne:
            data = self.cursor.fetchone()

        if not fetchOne:
            data = self.cursor.fetchall()
        
        return data



    def updateTable(self, tableName='', newValues=('',), filterWhere=('',)):
        # Method for update a table

        dbInstruction = f"UPDATE {tableName} SET "

        numberValues = len(newValues) - 1

        for value in newValues:
            dbInstruction += value

            numberValues -= 1
            if numberValues >= 0:
                dbInstruction += ', '

        dbInstruction += ' '

        if not filterWhere == ('',):
            dbInstruction += 'WHERE '
            numberValues = len(filterWhere) - 1

            for where in filterWhere:
                dbInstruction += where + ' '

                numberValues -= 1
                if numberValues >= 0:
                    dbInstruction += 'AND '

        dbInstruction += ';'

        # Execute an sql instruction
        self.cursor.execute(dbInstruction)
        # Save the changes
        self.connection.commit()
        print(f"The table {tableName} has ben actualized\n{dbInstruction}")


    def deleteElement(self, tableName='', filterWhere=('',)):
        # Function for delete an element in the database

        dbInstruction = f"DELETE FROM {tableName} "

        if not filterWhere == ('',):
            dbInstruction += 'WHERE '
            numberValues = len(filterWhere) - 1

            for where in filterWhere:
                
                filterNotification = "whit where arguments"
                dbInstruction += where + ' '
                
                numberValues -= 1
                if numberValues >= 0:
                    dbInstruction += 'AND '

        else:
            filterNotification = "without where arguments"

        dbInstruction += ';'

        # Execute an sql instruction
        self.cursor.execute(dbInstruction)
        # Save the changes
        self.connection.commit()
        print(
            f"The elements in the table {tableName} has ben deleted {filterNotification}\n{dbInstruction}")


    def dropTable(self, tableName):
        # Method for delete a table

        dbInstruction = f'DROP TABLE {tableName};'

        # Execute an sql instruction
        self.cursor.execute(dbInstruction)
        # Save the changes
        self.connection.commit()

        print(
            f'The table {tableName} in {self.dbName} has ben deleted\n{dbInstruction}')


def main():
    pass


if __name__ == '__main__':
    main()
