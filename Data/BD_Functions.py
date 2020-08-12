import conector

global mydb
mydb = conector.connect_mysql("lucas-Inspiron-5558", "root", "")

def get_CODBDI():
    pass

def getOrCreate_CODNEG():
    pass

def get_TPmerc():
    pass

def get_ESPECI():
    pass

def get_INDOPC():
    pass

def insert_cotacoes(Data_Pregao, CODBDI, CODNEG, TPMerc, ESPECI, Prazot, MODREF, PREABRE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TETONEG, QUATOT, VOLTOT, PREEXE, INDOPC, CODISI, DISMES):
    cursor = mydb.cursor(buffered=True)
    query = ("INSERT INTO cotacoes_Bovespa.Cotacoes (Data_Pregao, CODBDI_ID, CODNEG_ID, TPMerc_Id, ESPECI_Id, Prazot, MODREF, PREABRE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TETONEG, QUATOT, VOLTOT, PREEXE, INDOPC_ID, CODISI, DISMES) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(query, (Data_Pregao, get_CODBDI(), getOrCreate_CODNEG(), get_TPmerc(), get_ESPECI(), Prazot, MODREF, PREABRE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TETONEG,QUATOT, VOLTOT, PREEXE, get_INDOPC(), CODISI, DISMES))
    mydb.commit()
    return