import mysql.connector as mariadb

class Principal:
    def __init__(self):
        self.banco = mariadb.connect(host= 'localhost', user= 'root', passwd= '', db= 'loja')

    def exibir_produtos(self):
        cursor = self.banco.cursor()
        comando_SQL = "SELECT codigo, nome, marca, DATE_FORMAT(STR_TO_DATE(validade,'%Y-%m-%d'), '%d/%m/%Y') FROM produtos WHERE validade <= DATE_ADD(NOW(), INTERVAL 20 DAY);"
        cursor.execute(comando_SQL)
        print(cursor.fetchall())

    def inserir_produto(self, codigo, nome, marca, validade):
        cursor = self.banco.cursor()
        comando_SQL = "INSERT INTO produtos VALUES(%s,%s,%s,STR_TO_DATE(%s,'%d/%m/%Y'));"       
        dados_lidos = (str(codigo), str(nome), str(marca), str(validade))
        cursor.execute(comando_SQL, dados_lidos)
        self.banco.commit()

    def excluir_produto(self, codigo, validade):
        cursor = self.banco.cursor()
        comando_SQL = "DELETE FROM produtos WHERE codigo = %s AND validade = STR_TO_DATE(%s,'%d/%m/%Y');"
        dados_lidos = (str(codigo), str(validade))
        cursor.execute(comando_SQL, dados_lidos)
        self.banco.commit()