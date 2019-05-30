Tabela_de_simbolos = {
    'inicio': {'token': 'inicio', 'tipo': ' '},
    'varinicio': {'token': 'varinicio', 'tipo': ' '},
    'varfim': {'token': 'varfim', 'tipo': ' '},
    'escreva': {'token': 'escreva', 'tipo': ' '},
    'leia': {'token': 'leia', 'tipo': ' '},
    'se': {'token': 'se', 'tipo': ' '},
    'entao': {'token': 'entao', 'tipo': ' '},
    'fimse': {'token': 'fimse', 'tipo': ' '},
    'fim': {'token': 'fim', 'tipo': ' '},
    'inteiro': {'token': 'inteiro', 'tipo': 'inteiro'},
    'lit': {'token': 'lit', 'tipo': 'lit'},
    'literal' :{'token':'literal', 'tipo':'lit'},
    'real': {'token': 'real', 'tipo': 'real'}
}

Estados_finais_AFD = {
    'S1':'Num',
    'S6':'literal',
    'S7':'id',
    'S8':'OPM',
    'S9':'AB_P',
    'S10':'FC_P',
    'S11':'PT_V',
    'S12':'OPR',
    'S13':'OPR',
    'S14':'OPR',
    'S15':'RCB',
    'S16':'OPR',
    'S18':'OPR',
    'S17':'OPR',
    'S20':'EOF',
    'S21':'Num',
    'S22':'Num'
}

Erros_lexicos = {
    'S19': 'Comentario nao terminado!',
    'S5': 'Literal nao terminado!',
    'S2': 'Constante numerica invalida!',
    'S3': 'Constante numerica invalida!',
    'S4': 'Constante numerica invalida!'
}

# Tabela de transicoes
Tabela_AFD = {
    'S0':
        {
            'Tab': 'S0',
            'Espaco': 'S0',
            'Salto': 'S0',
            'D': 'S1',
            '"': 'S5',
            'L': 'S7',
            '*': 'S8',
            '-': 'S8',
            '+': 'S8',
            '/': 'S8',
            '(': 'S9',
            ')': 'S10',
            ';': 'S11',
            '<': 'S12',
            '>': 'S13',
            '=': 'S17',
            '{': 'S19',
            'EOF': 'S20'
        },

    'S1':
        {
            'D': 'S1',
            '.': 'S2',
            'E': 'S3',
            'e': 'S3'
        },

    'S2':
        {
            'D': 'S21'
        },

    'S3':
        {
            '+': 'S4',
            '-': 'S4',
            'D': 'S22'
        },

    'S4':
        {
            'D': 'S22'
        },

    'S5':
        {
            '.*': 'S5',
            '"': 'S6'
        },

    'S6': {},

    'S7':
    {
            'L': 'S7',
            'D': 'S7',
            '_': 'S7'
    },

    'S8': {},

    'S9': {},

    'S10': {},

    'S11': {},

    'S12':
    {
            '=': 'S14',
            '-': 'S15',
            '>': 'S18'
    },

    'S13': {
            '=': 'S16'
    },

    'S14': {},

    'S15': {},

    'S18': {},

    'S19':
    {
            '.*': 'S19',
            '}': 'S0'
    },

    'S20': {},

    'S21':
    {
        'D': 'S21'
    },

    'S22':
    {
        'D': 'S22'
    }
}

def ehAschii_32_126(caracter):
    return caracter in (" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}\t\n")

def ehTab_espaco_salto(caracter):
    return caracter in ('\t', ' ', '\n')

def ehLiteral(caracter):
    return caracter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ehNumero(caracter):
    return caracter in '0123456789'

def ehOPM(caracter):
    return caracter in '+-/*'

def ehEstadofinal(estado):
    return estado in Estados_finais_AFD

def ehEstadofinalExcecao(estado):
    return estado in ('S1', 'S7', 'S12', 'S13', 'S21', 'S22')

def rotular(caracter, estado):
    if(caracter is not '"' and estado is 'S5' and ehAschii_32_126(caracter)):
        return '.*'
    if(caracter is not '}' and estado is 'S19' and ehAschii_32_126(caracter)):
        return '.*'
    if(caracter is '}' and estado is 'S19'):
        return 'Comentario'
    if(ehLiteral(caracter)):
        return 'L'
    if(ehNumero(caracter)):
        return 'D'
    rotulos_S0 = {' ': 'Espaco', '\t': 'Tab', '\n': 'Salto'}
    if(ehTab_espaco_salto(caracter) and estado is 'S0'):
        return rotulos_S0[caracter]
    return caracter

def getToken(estado):
    if(estado in Estados_finais_AFD.keys()):
        return Estados_finais_AFD[estado]
    return ' '

def getTipo(token, lexema, estado):
    if(token is 'literal'):
        return Tabela_de_simbolos['lit']['tipo']
    if(token is 'Num'):
        if(estado in ('S1','S22')):
            return Tabela_de_simbolos['inteiro']['tipo']
        if(estado is 'S21'):
            return Tabela_de_simbolos['real']['tipo']
    if(token in ('OPM','OPR','RCB')):
        return lexema
    return ' '

class String:
    def __init__(self):
        self.lexema = ''
        self.token = '--'
        self.tipo = '--'

def getTokenAndTipo(lexema, estado):
    string = String()
    string.lexema = lexema
    if(lexema in Tabela_de_simbolos.keys()):
        string.token = Tabela_de_simbolos[lexema]['token']
        string.tipo = Tabela_de_simbolos[lexema]['tipo']
    else:
        string.token = getToken(estado)
        string.tipo = getTipo(string.token, lexema, estado)
    return string

def atualizarTabelaSimbolos(string):
    if(not string.lexema in Tabela_de_simbolos.keys()):
        Tabela_de_simbolos[string.lexema] = {'token':string.token, 'tipo':string.tipo}

def erro_lexico(erro):
    if(erro['estado'] in Erros_lexicos.keys()):
        return 'Erro: {}\tLinha: {}\tColuna: {}\n{}'.format(Erros_lexicos[erro['estado']],
            erro['linha'],erro['coluna'],erro['lexema'])
    return 'Erros nao foram identificados!'

class Arquivo:
    def __init__(self, texto):
        self.texto = texto
        self.cont_caractere = 0
        self.linha = 1
        self.coluna = 1
        self.notEOF = True

def analisador_lexico(arquivo):
    string = String()
    caractere = ''
    rotulo = ''
    estado_atual = 'S0'

    while(True):
        if(arquivo.cont_caractere < len(arquivo.texto)):
            caractere = arquivo.texto[arquivo.cont_caractere]
            arquivo.cont_caractere = arquivo.cont_caractere + 1
            rotulo = rotular(caractere, estado_atual)

            if(caractere is '\n'):
                arquivo.linha = arquivo.linha + 1
                arquivo.coluna = 1
            else:
                arquivo.coluna = arquivo.coluna + 1
        else:
            arquivo.notEOF = False
            rotulo = 'EOF'
            caractere = ''

        if(rotulo in Tabela_AFD[estado_atual].keys()):
            estado_atual = Tabela_AFD[estado_atual][rotulo]
            if(rotulo in ('Comentario', 'Tab', 'Espaco', 'Salto') and estado_atual is 'S0'):
                print(rotulo + ' Ignorado\n')
            else:
                string.lexema = string.lexema + caractere
            if(ehEstadofinal(estado_atual)):
                if(ehEstadofinalExcecao(estado_atual) is not True):
                    string = getTokenAndTipo(string.lexema, estado_atual)
                    atualizarTabelaSimbolos(string)
                    return string
        elif(ehEstadofinalExcecao(estado_atual)):
            arquivo.cont_caractere = arquivo.cont_caractere - 1
            string = getTokenAndTipo(string.lexema, estado_atual)
            atualizarTabelaSimbolos(string)
            return string
        else:
            erro = {'linha':arquivo.linha,'coluna':arquivo.coluna, 'estado':estado_atual, 'lexema':string.lexema+caractere}
            print(erro_lexico(erro)+'\n')
            estado_atual = 'S0'
            string.lexema = ''

def main():
    arquivo = open('doc/texto.alg', 'r')
    texto_codigo = arquivo.read()
    arquivo_texto = Arquivo(texto_codigo)

    while(arquivo_texto.notEOF):
        retorno = analisador_lexico(arquivo_texto)
        print('lexema: {}\ttoken: {}\ttipo: {}\n'.format(retorno.lexema, retorno.token, retorno.tipo))

if __name__ == "__main__":
    main()