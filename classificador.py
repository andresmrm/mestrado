import os

from contador import Contador
from retrancas import CONTEUDOS, PUBLICANTES


os.chdir('../temporario')


erros = open('erros','w')
saida = open('saida.csv','w')
saida.write('"ID","Data","Retranca","Tipo do Conteúdo","Secretaria","Orgão","Texto"\n')
d = "temp3"
txts = os.listdir(d)
Contador.iniciar(len(txts))
for i, txt in enumerate(txts):
    #print(txt)
    # Extrai dados do nome do TXT
    data = '%s-%s-%sT00:00:00Z' % (txt[0:4], txt[4:6], txt[6:8])
    tipo_letra = txt[8:9]
    retranca = txt[9:15]
    if retranca != 'ALHAU.':
        try:
            arq = open(d+'/'+txt, "r")
            texto = arq.read()
            arq.close()
            texto = texto.replace('"','""')
            try:
                conteudo = CONTEUDOS[tipo_letra.lower()]
            except:
                conteudo = '-'
                print('ERRO CONTEUDO', tipo_letra, txt)
            #print(retranca, txt)
            try:
                secretaria, orgao = PUBLICANTES[retranca]
            except:
                secretaria, orgao = '-', '-'
                erros.write(retranca+'\n')
            saida.write('%s,%s,"%s","%s","%s","%s","%s"\n' % (i, data, tipo_letra+retranca, conteudo, secretaria, orgao, texto))
        except UnicodeDecodeError:
            print('Erro ARQ', txt)
    Contador.atualizar(i)
saida.close()
erros.close()
