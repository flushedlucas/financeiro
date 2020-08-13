import conector

global mydb
mydb = conector.connect_mysql("lucas-Inspiron-5558", "root", "")

def get_CODBDI(Code):
    cursor = mydb.cursor()
    cursor.execute("SELECT idCODBDI FROM cotacoes_Bovespa.CODBDI WHERE Code = " + Code)
    return cursor.fetchone()[0]

def getOrCreate_CODNEG(COD, Empresa):
    # Empresa = str.strip(Empresa)
    cursor = mydb.cursor()
    cursor.execute("SELECT idCODNEG FROM cotacoes_Bovespa.CODNEG WHERE Code = '" + COD+"'")
    codneg = cursor.fetchone()
    if codneg != None:
        return codneg[0]
    else:
        cursor.execute("SELECT idEmpresas FROM cotacoes_Bovespa.Empresas WHERE Name = '" + str.strip(Empresa) + "'")
        emp = cursor.fetchone()
        if emp == None:
            cursor.execute("INSERT INTO cotacoes_Bovespa.Empresas (Name, Code) VALUES (%s,%s)", params=(Empresa,""))
            mydb.commit()
            cursor.execute("SELECT idEmpresas FROM cotacoes_Bovespa.Empresas WHERE Name = '" + str.strip(Empresa) + "'")
            emp = cursor.fetchone()[0]
        cursor.execute("INSERT INTO cotacoes_Bovespa.CODNEG (Empresa_ID, Code) VALUES (%s,%s)", params=(emp,COD))
        mydb.commit()

        cursor.execute("SELECT idCODNEG FROM cotacoes_Bovespa.CODNEG WHERE Code = '" + COD+"'")
        codneg = cursor.fetchone()

        return codneg[0]

def get_TPmerc(Code):
    cursor = mydb.cursor()
    cursor.execute("SELECT id_TPMerc FROM cotacoes_Bovespa.TPMerc WHERE Code = " + Code)
    return cursor.fetchone()[0]

def get_ESPECI(ESPECI):
    cursor = mydb.cursor()
    cursor.execute("SELECT idESPECI FROM cotacoes_Bovespa.`ESPECI` WHERE Code = '" + ESPECI+"'")
    return cursor.fetchone()[0]

def get_INDOPC(Code):
    cursor = mydb.cursor()
    cursor.execute("SELECT id_INDOPC FROM cotacoes_Bovespa.INDOPC WHERE Code_Number = " + str(Code))
    return cursor.fetchone()[0]

def insert_cotacoes(Data_Pregao, CODBDI, CODNEG, Empresa, TPMerc, ESPECI, Prazot, MODREF, PREABRE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TETONEG, QUATOT, VOLTOT, PREEXE, INDOPC, DATEVEN, FATCOT, PTOEXE, CODISI, DISMES):
    cursor = mydb.cursor(buffered=True)
    query = ("INSERT INTO cotacoes_Bovespa.Cotacoes (Data_Pregao, CODBDI_ID, CODNEG_ID, TPMerc_Id, ESPECI_Id, Prazot, MODREF, PREABRE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TETONEG, QUATOT, VOLTOT, PREEXE, INDOPC_ID, DATEVEN, FATCOT, PTOEXE, CODISI, DISMES) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(query, (Data_Pregao, get_CODBDI(CODBDI), getOrCreate_CODNEG(CODNEG, Empresa), get_TPmerc(TPMerc), get_ESPECI(ESPECI), Prazot, MODREF, PREABRE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TETONEG,QUATOT, VOLTOT, PREEXE, get_INDOPC(INDOPC), CODISI, DISMES))
    mydb.commit()
    return

# teste = getOrCreate_CODNEG("VALE3", "Vale SA")
# print(teste)