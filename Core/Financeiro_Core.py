import os
import Data.BD_Functions

def split_lines(linha):
    lista = []

    lista.append(linha[2:10])   # Data do pregão = linha[2:10]
    lista.append(linha[10:12])  # CODBDI = linha[10:12]
    lista.append(str.strip(linha[12:24]))   # CODNEG = linha[12:24]
    lista.append(linha[24:27])  # TPMERC = linha[24:27]
    lista.append(str.strip(linha[27:39]))   # NOMRES = linha[27:39]
    lista.append(str.strip(linha[39:49]))   # ESPECI = linha[39:49]
    lista.append(str.strip(linha[49:52]))   # Prazot = linha[49:52]
    lista.append(str.strip(linha[52:56]))   # MODREF = linha[52:56]
    lista.append(linha[56:67] + "." + linha[67:69])  # PREABRE = linha[56:69]
    lista.append(linha[69:80]+ "." + linha[80:82])  # PREMAX = linha[69:82]
    lista.append(linha[82:93]+ "." + linha[93:95])  # PREMIN = linha[82:95]
    lista.append(linha[95:106] + "." + linha[106:108]) # PREMED = linha[95:108]
    lista.append(linha[108:119] + "." + linha[119:121])    # PREULT = linha[108:121]
    lista.append(linha[121:132] + "." + linha[132:134])    # PREOFC = linha[121:133]
    lista.append(linha[134:145] + "." + linha[145:147])    # PREOFV = linha[133:147] ATENÇÃO AQUI
    lista.append(linha[147:152])    # TOTNEG = linha[147:152]
    lista.append(linha[152:170])    # QUATOT = linha[152:170]
    lista.append(linha[170:186] + "." + linha[186:188])    # VOLTOT = linha[170:188]
    lista.append(linha[188:199] + "." + linha[199:201])    # PREEXE = linha[188:201]
    lista.append(linha[201:202])    # INDOPC = linha[201:202]
    lista.append(linha[202:210])    # DATVEN = linha[202:210]
    lista.append(linha[210:217])    # FATCOT = linha[210:217]
    lista.append(linha[217:230])    # PTOEXE = linha[217:230]
    lista.append(linha[230:242])    # CODISI = linha[230:242]
    lista.append(linha[242:245])    # DISMES = linha[242:245]

    return lista

def import_cotacoes(arquivo):
    read = open(arquivo, 'r')
    read.readline()
    linhas = read.readlines()
    linhas.pop()
    map(split_lines, linhas)
    map()


import_cotacoes(os.getcwd() + '/Teste.txt')
    
