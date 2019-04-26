Tabela_de_simbolos = {
    'inicio': {'token': 'inicio', 'tipo': ''},
    'varinicio': {'token': 'varinicio', 'tipo': ''},
    'varfim': {'token': 'varfim', 'tipo': ''},
    'escreva': {'token': 'escreva', 'tipo': ''},
    'leia': {'token': 'leia', 'tipo': ''},
    'se': {'token': 'se', 'tipo': ''},
    'entao': {'token': 'entao', 'tipo': ''},
    'fimse': {'token': 'fimse', 'tipo': ''},
    'fim': {'token': 'fim', 'tipo': ''},
    'inteiro': {'token': 'inteiro', 'tipo': 'inteiro'},
    'lit': {'token': 'lit', 'tipo': 'literal'},
    'real': {'token': 'real', 'tipo': 'real'},
}

Estados_finais_AFD = {
    'S1': 'Num',    # Numeral
    'S6': 'Literal',# Literal
    'S7': 'id',     # identificador
    'S8': 'OPM',    # *,-,+,/
    'S9': 'AB_P',   # {
    'S10': 'FC_P',  # }
    'S11': 'PT_V',  # ;
    'S12': 'OPR',   # <
    'S13': 'OPR',   # >
    'S14': 'OPR',   # <=
    'S15': 'RCB',   # <-
    'S16': 'OPR',   # >=
    'S18': 'OPR',   # <>
    'S17': 'OPR',   # =
    'S20': 'EOF',   # final de arquivo
    'S21': 'Num'    # Num
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
            'E': 'S4',
        },

    'S2':
        {
            'D': 'S21'
        },

    'S3':
        {
            'D': 'S1'
        },

    'S4':
        {
            '+': 'S3',
            '-': 'S3',
            'D': 'S1'
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

    'S13':{
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
        'E':'S4',
        'D':'S21'
    }
}


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

def ehEstadofinalExcessao(estado):
    return estado in ('S1','S7','S12','S13')


def rotular(caracter, estado):
    rotulos_S0 = {' ': 'Espaco', '\t': 'Tab', '\n': 'Salto'}
    if(ehTab_espaco_salto(caracter) and estado is 'S0'):
        return rotulos_S0[caracter]
    if(caracter is '}' and estado is 'S19'):
        return 'Comentario'
    if(ehLiteral(caracter)):
        return 'L'
    if(ehNumero(caracter)):
        return 'D'
    if(estado is 'S1' and (caracter is 'e' or caracter is 'E')):
        return 'E'
    return caracter


def erro_lexico(estado):
    erros = {}

class Palavra:
    def __init__(self):
        self.palavra=''
        self.token=''
        self.tipo=''
    def set_palavra(self, string):
        self.palavra = string
    def get_palavra(self):
        return self.palavra
    def set_token(self, string):
        self.token = string
    def get_token(self):
        return self.token
    def set_tipo(self, string):
        self.tipo = string
    def get_tipo(self):
        return self.tipo    

cont_caractere=0
linha = 1
coluna = 1

def analisador_lexico_1(texto_codigo, estado_atual, palavra):
    global cont_caractere
    global linha
    global coluna

    caractere = ''
    rotulo = ''
    continuar = True

    while(continuar):
        if(cont_caractere < len(texto_codigo)):
            caractere = texto_codigo[cont_caractere]
            cont_caractere = cont_caractere + 1

            rotulo = rotular(caractere, estado_atual)

            if(caractere is '\n'):
                linha = linha + 1
                coluna = 1
            else:
                coluna = coluna + 1
            if(estado_atual is 'S0'):
                palavra = ''
        else:
            rotulo = 'EOF'
            continuar = False

        if(rotulo in Tabela_AFD[estado_atual].keys()):
            estado_atual = Tabela_AFD[estado_atual][rotulo]
            if(rotulo in ('Comentario', 'Tab', 'Espaco', 'Salto')):
                print(rotulo + ' Ignorado\n')
            if(ehEstadofinal(estado_atual)):
                if(ehEstadofinalExcessao(estado_atual)):
                    return analisador_lexico_1(texto_codigo, estado_atual, palavra)
                else:
                    return 'token: {}\tlexema: {}\ttipo: {}\tlinha: {}\tcoluna: {}\n'.format(palavra,palavra,palavra.tipo,linha,coluna)
                    
        elif(ehEstadofinalExcessao(estado_atual)):
            return 'token: {}\tlexema: {}\ttipo: {}\tlinha: {}\tcoluna: {}\n'.format(palavra.palavra, palavra.get_token(),palavra.get_tipo(),linha,coluna)
        else:
            return '\nErro: linha {} e coluna {}.\n{}: {}'.format(linha, coluna, erro_lexico(estado_atual), palavra)

def analisador_lexico(texto_codigo):
    palavra = Palavra()
    analisador_lexico_1(texto_codigo, 'S0', palavra)

def ler_lexema(arquivo):
    linha = 1
    coluna = 1

    rotulo = ''
    palavra = ''

    token = ''
    tipo = ''

    cont_caractere = 0
    caractere = ''
    continuar = True
    estado_atual ='S0'
    estado_prox = ''

    while(continuar):
        if(cont_caractere < len(arquivo)):
            caractere = arquivo[cont_caractere]
            rotulo = rotular(caractere, estado_atual)

            if(rotulo in Tabela_AFD[estado_atual].keys):
                estado_prox = Tabela_AFD[estado_atual][rotulo]

                if(estado_prox is 'S0'):
                    palavra = ''
                    if(caractere is '\n'):
                        linha = linha + 1
                        coluna = 0
                    else:
                        cont_caractere = cont_caractere + 1
            else:
                print(erro_lexico(estado))
        else:
            rotulo = 'EOF'
            continuar = False
        print(caractere)


def main():
    arquivo = open('texto.alg', 'r')
    texto_codigo = arquivo.read()
    ler_lexema(texto_codigo)
    # analisador_lexico(texto_codigo)


if __name__ == "__main__":
    main()
