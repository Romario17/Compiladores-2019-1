Tabela_de_simbolos =
{
    'inicio'    : {'token':'inicio', 'tipo':''},
    'varinicio' : {'token':'varinicio', 'tipo':''},
    'varfim'    : {'token':'varfim', 'tipo':''},
    'escreva'   : {'token':'escreva', 'tipo':''},
    'leia'      : {'token':'leia', 'tipo':''},
    'se'        : {'token':'se', 'tipo':''},
    'entao'     : {'token':'entao', 'tipo':''},
    'fimse'     : {'token':'fimse', 'tipo':''},
    'fim'       : {'token':'fim', 'tipo':''},
    'inteiro'   : {'token':'inteiro', 'tipo','inteiro'},
    'lit'       : {'token':'lit', 'tipo':'literal'},
    'real'      : {'token':'real', 'tipo':'real'},
}

Estados_nao_finais_AFD =
{
    '':'',
    '':'',
    '':'',
}

Estados_finais_AFD = 
{
    'S1':'Num',
    'S6':'Literal',
    'S7':'id',
    'S8':'OPM',
    'S9':'AB_P',
    'S10':'FC_P'
    'S11':'PT_V',
    'S12':'OPR',
    'S13':'OPR',
    'S14':'OPR',
    'S15':'RCB',
    'S16':'OPR',
    'S18':'OPR',
    'S17':'OPR',
    'S20':'EOF'
}

Tabela_AFD = 
{
    'S0':
        {
            'Tab_espaco_salto':'S0',
            'D':'S1',
            '"':'S5',
            'L':'S7',
            '*':'S8',
            '-':'S8',
            '+':'S8',
            '/':'S8',
            '(':'S9',
            ')':'S10',
            ';':'S11',
            '<':'S12',
            '>':'S13',
            '=':'S17',
            '{':'S19',
            'EOF':'S20'
        },
    'S1':
        {
            'D':'S2',                        
            '.':'S2',
            'E':'S4',
        },
    'S2':
        {
            'D':'S1'
        },
    'S3':
        {
            'D':'S1'
        },
    'S4':
        {
            '+':'S3',
            '-':'S3'
        },
    'S5':
        {
            '.*':'S5',
            '"':'S6'
        },
    'S6':{},
    'S7':
        {
            'L':'S7',
            'D':'S7',
            '_':'S7'
        },
    'S8':{},
    'S9':{},
    'S10':{},
    'S11':{},
    'S12':
        {
            '=':'S14',
            '-':'S15',
            '>':'S18'
        },
    'S13':
        {
            '=':'S16'
        }
    'S14':{},
    'S15':{},
    'S18':{},
    'S19':
        {
            '.*':'S19'
        }
    'S20':
        {}    
}

def ehTab_espaco_salto(caracter)
    return caracter in ('\t',' ','\n')

def ehLiteral(caracter):
    return caracter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ehNumero(caracter):
    return caracter in '0123456789'

def ehOPM(caracter):
    return caracter in '+-/*'

def ehEstadofinal(estado):
    return estado in Estados_finais_AFD

def analisador_lexico(texto_codigo):
    linha=1
    coluna=1
    cont_caractere=0

    caractere=''
    rotulo=''
    palavra=''
    
    token=''
    tipo=''
    estado_atual='S0'
    continuar=True

    while(continuar):
        # Determinando o rótulo associado ao caractere
        if(cont_caractere < len(texto_codigo)):
            caractere = texto_codigo[cont_caractere]
            rotulo=caractere
            if(ehTab_espaco_salto(caractere)):
                rotulo = 'tab_espaco_salto'
            elif(ehLiteral(caractere)):
                rotulo = 'L'
            elif(ehNumero(caractere)):
                rotulo = 'D'
            elif(estado_atual is 'S1' and (caractere is 'e' or caractere is 'E')):
                rotulo = 'E'
            if(caractere is '\n'):
                linha = linha + 1
                coluna = 1
            palavra = palavra + caractere
        else:
            rotulo='EOF'

        if(rotulo in Tabela_AFD[estado_atual].keys()):
            estado_atual = Tabela_AFD[estado_atual][rotulo]
            if(ehEstadofinal(estado_atual)):
                token = Estados_finais_AFD[espaco][rotulo]
                if(token is 'id'):
                elif(palavra in Tabela_de_simbolos.keys()):
                    token = Tabela_de_simbolos[estado_atual]['token']
                    tipo = Tabela_de_simbolos[estado_atual]['tipo']
        else
            
            

def main():
    arquivo = open('texto.alg','r')
    texto_codigo = arquivo.read()
    analisador_lexico(texto_codigo)

if __name__ == "__main__":
    main()