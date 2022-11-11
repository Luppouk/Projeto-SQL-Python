# 2°F — Leonardo Torres Gonçalves e Silva — Luan Groppo Viana — Carlos Eduardo Miranda Cavalcanti

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
    database='greenpeace',
    user='root',
    password='')
    sql_insert = """INSERT INTO pesquisa (nome , tempo, derretimento, elevacaomar)
    VALUES
    (%s, %s, %s, %s);"""
    sql_select = "select year(tempo) from pesquisa;"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    records = cursor.fetchall()
    anos = []
    anosinval = []
    for x in records:
        anos.append(x[0])
    for x in anos:
        if anos.count(x) == 2:
            anosinval.append(x)
    resp = 's'
    while resp == 's':
        nome = input('Digite o nome do pesquisador:')
        time = [int(input("Digite o ano:")), int(input("Digite o mês:")), int(input("Digite o dia:")), int(input("Digite a hora:")), int(input("Digite o minuto:")), int(input("Digite o segundo:"))]
        while time[0] > 2021:   
            time[0] = int(input("Não pode ser maior que 2021. Digite o ano novamente:"))
        while time[0] in anosinval:
            time[0] = int(input("Já tem dois registros para esse ano. Digite o ano novamente:"))
        while time[1] > 12:
            time[1] = int(input("Um ano não tem mais de 12 meses. Digite o mês novamente:"))
        while time[2] > 31:
            time[2] = int(input("Um mês não tem mais de 31 dias. Digite o dia novamente:"))
        while time[3] > 24:
            time[3] = int(input("Um dia não tem mais de 24 horas. Digite a hora novamente:"))
        while time[4] > 60:
            time[4] = int(input("Uma hora não tem mais de 60 minutos. Digite o minuto novamente:"))
        while time[5] > 60:
            time[5] = int(input("Um minuto não tem mais de 60 segundos. Digite o segundo novamente:"))
        tempo = str(time[0]) + "-" + str(time[1]) + "-" + str(time[2]) + " " + str(time[3]) + ":" + str(time[4]) + ":" + str(time[5])
        derret = input("Digite o derretimento semestral em toneladas:")
        elev = input('Digite a elevação do mar em mm:')
        cursor.execute(sql_insert, (nome, tempo, derret, elev))
        connection.commit()
        print(cursor.rowcount, "inserido com sucesso")
        anos.append(time[0])
        for x in anos:
           if anos.count(x) == 2:
                anosinval.append(x)
        resp = input('Deseja inserir mais valores? s/n ')
        while resp != 's' and resp != 'n':
            resp = input('Inválido, digite novamente:')

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexão fechada")