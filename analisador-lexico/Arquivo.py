                               token = Estados_finais_AFD[estado_atual][rotulo]
                if(token is 'id'):
                    if(palavra in Tabela_de_simbolos.keys()):
                        token = Tabela_de_simbolos[palavra]['token']
                        tipo = Tabela_de_simbolos[palavra]['tipo']
                    elif(palavra not in Tabela_de_simbolos.keys()):
                        Tabela_de_simbolos[palavra] = {
                            'token': palavra, 'tipo': tipo}
               
                elif(token in ('OPM', 'OPR', 'RCB')):
                    tipo = palavra
                elif(token is 'Literal'):
                    tipo = 'Literal'
                print('token:'+token+'\tlexema:'+palavra+'\ttipo:' +
                      tipo+'\tlinha:'+linha+'\tcoluna:'+coluna+'\n')