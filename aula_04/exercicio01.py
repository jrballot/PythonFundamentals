#!/usr/bin/env python3

# Quando o usuário passar um ticket valido na catraca,
# a catraca deve liberar e o preço da passagem deve ser 
# descontado do saldo do ticket. Um ticket válido
# é um ticket que está dentro do prazo de validade,
# tem saldo suficiente para pagar a passagem e pertence
# a mesma concessionária da catraca.


import datetime

########################################################
## Contantes
########################################################

PRECO_DA_PASSAGEM = 4.0

########################################################
## Erros
########################################################

class ErrorTicketExpirado(Exception):
    pass

class ErrorSaldoInsuficiente(Exception):
    pass

class ErrorConcessionariaDiferente(Exception):
    pass

########################################################
## Class
########################################################

class Ticket:
    
    def __init__(self, validade, saldo, concessionaria):
        self.validade = validade
        self.saldo = saldo
        self.concessionaria = concessionaria
        
class Catraca:
    
    def __init__(self, concessionaria):
        self.concessionaria = concessionaria
        self.estado = 'travada'

    def esta_liberada(self):
        if self.estado == 'liberada':
            return True
        return False


    def liberar(self, ticket):
        
        if ticket.validade < datetime.datetime.now():
            raise ErrorTicketExpirado
        
        if ticket.saldo < PRECO_DA_PASSAGEM:
            raise ErrorSaldoInsuficiente
        
        if ticket.concessionaria != self.concessionaria:
            raise ErrorConcessionariaDiferente
    
        ticket.saldo = ticket.saldo - PRECO_DA_PASSAGEM
        self.estado = 'liberada'
    
########################################################
## Testes
########################################################

if __name__ == '__main__':

    # TESTE TICKET EXPIRADO
    try:
        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        saldo = PRECO_DA_PASSAGEM + 30.0
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)
        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)
        print("BUG ENCONTRADO")
    except ErrorTicketExpirado:
        print('Teste de ticket expirado ok')



    # TEST CONCESSIONARIA DIFERENTE
    try:
        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        saldo = PRECO_DA_PASSAGEM + 30.0
        concessionaria = 'emtu'

        ticket = Ticket(validade, saldo, concessionaria)
        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)
        print("BUG ENCONTRADO")

    except ErrorConcessionariaDiferente:
        print('Teste de Concessionaria incorreta ok')


        
    # TESTE SALDO INSUFICIENTE
    try:
        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        saldo = PRECO_DA_PASSAGEM - 1.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)
        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)
        print("BUG ENCONTRADO")

        
    except ErrorSaldoInsuficiente:
        print('Teste de Saldo insuficiente ok')

    # TESTE CATRACA LIBERADA 

    validade = datetime.datetime.now() + datetime.timedelta(days=365)
    saldo = PRECO_DA_PASSAGEM + 1.00
    concessionaria = 'sptrans'

    ticket = Ticket(validade, saldo, concessionaria)
    catraca = Catraca(concessionaria='sptrans')
    catraca.liberar(ticket)   

    try:    
        assert catraca.esta_liberada()
        assert ticket.saldo == (saldo - PRECO_DA_PASSAGEM)
        
        print('Happy-path ok!!!')
    except:
        print('BUG ENCONTRADO')
