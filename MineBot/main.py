import discord
from discord.ext import commands
from connections import database, autoTable
import tables

# Sqlite 3 connection

database = database.sqliteManage('mineBotDatabase.sqlite3')

# MINEBOT

# Command prefix
bot = commands.Bot(command_prefix='&')

# Commands
@bot.command()
async def ping(ctx):
    # Command ping
    print(f'{ctx.guild.name} : ping')
    ping_msg = discord.Embed(
        title="Status", 
        description=f"Pong",
        color=discord.Color.green())
    
    await ctx.send(embed=ping_msg)

@bot.command()
async def createTable(ctx, tableType: str):
    # Command for create a table in the database
    
    print(f'{ctx.guild.name} : createTable')
    database.startConnection()

    if tableType.upper() == 'COORDS':
        tableElementType = tables.tableCoordinates
    else:
            createTable_Msg = discord.Embed(
                title="Error", 
                description=f"No ha ocurrido nada wtf",
                color=discord.Color.purple())

    try:
        database.createTable(tableName=f"Coords{ctx.guild.name}", dbTableFields= tableElementType)

        createTable_Msg = discord.Embed(
            title="Tabla creada exitosamente", 
            description=f"Se ha creado una tabla llamada {tableType}{ctx.guild.name} en la correspondiente base de datos, ahora puedes guardar las cordenadas",
            color=discord.Color.green())
            

    except Exception as e:
        createTable_Msg = discord.Embed(
            title="Error", 
            description=f"Ha ocurrido un error al crear la tabla\n{e}",
            color=discord.Color.red())
        print(f"Error:\n{e}")

    database.closeConnection()
    await ctx.send(embed=createTable_Msg)


@bot.command()
async def insertcoords(ctx, title: str, xvalue: int, yvalue: int, zvalue: int):
    # Command for create a table in the database
    
    print(f'{ctx.guild.name} : insertcoords')
    database.startConnection()


    try:
        database.startConnection()

        database.insertElement(
            tableName=f"Coords{ctx.guild.name}",
            elements=("user", "titles", "x_coordinates", "y_coordinates", "z_coordinates"),
            values=(f"'{ctx.message.author}'", f"'{title}'", str(xvalue), str(yvalue), str(zvalue))
        )

        insertcoords_Msg = discord.Embed(
            title="Coordenadas añadidas", 
            description=f"Se han guardado las coordenadas '{title}' en Coords{ctx.guild.name}",
            color=discord.Color.green())
            

    except Exception as e:
        insertcoords_Msg = discord.Embed(
            title="Error", 
            description=f"Ha ocurrido un error al insertar las coordenadas\n{e}",
            color=discord.Color.red())

        print(f"Error:\n{e}")

    database.closeConnection()
    await ctx.send(embed=insertcoords_Msg)


@bot.command()
async def show(ctx, arguments):
    # This command is for search and return the values in an embed message

    print(f"{ctx.guild.name}: show")

    try:
        database.startConnection()

        elements = database.selectElements(f"Coords{ctx.guild.name}", tableElements=("*",), filterwhere=(f"titles like '%{arguments}%'",))

        if elements == []:
            output = "No hay elementos para mostrar"

        else:
            output = ""
            for element in elements:
                output += f"id ={element[0]} \n {element[1]} \n{element[2]}, {element[3]}, {element[4]} \nPor: {element[5]}\n\n"


        show_Msg = discord.Embed(
            title=f"Coordenadas {arguments}", 
            description=f"{output}",
            color=discord.Color.blue())

        database.closeConnection()

    except Exception as e:

        print(f"Error:\n{e}")

        show_Msg = discord.Embed(
            title=f"Error al buscar las coordenadas", 
            description=f"Error\n{e}",
            color=discord.Color.red())

    await ctx.send(embed=show_Msg)


@bot.command()
async def delete(ctx, element_id):
    # This command delete an element of the database

    print(f"{ctx.guild.name}: delete")
    
    try:
        database.startConnection()

        user = database.selectElements(f"Coords{ctx.guild.name}", tableElements=("user",), filterwhere=(f"id = {element_id}",))

        if str(user[0][0]) == str(ctx.message.author):
            

            database.deleteElement(tableName=f"Coords{ctx.guild.name}", filterWhere=(f"id = {element_id}",))

            delete_Msg = discord.Embed(
                title=f"Coordenadas eliminadas", 
                description=f"Ha borrado las coordenadas exitosamente",
                color=discord.Color.green())

        else:
            delete_Msg = discord.Embed(
                title=f":0", 
                description=f"No tienes permiso para borrar las coordenadas, pertenecen a: {user[0][0]}",
                color=discord.Color.purple())
        
        database.closeConnection()

    except Exception as e:
        
        print(f"Error:\n{e}")

        delete_Msg = discord.Embed(
            title=f"Ha ocurrido un error", 
            description=f"Error:\n{e}",
            color=discord.Color.red())

    await ctx.send(embed= delete_Msg)

    

# TOKEN
bot.run("ODAwMjczNzg0MjUwNDMzNTY2.YAPvCg.vLUVgF9FLt3BXAEczYf-MK57HOk")