#!/usr/bin/env python3

import datetime
import unittest

import exercicio01 as scooby

class CatracaTeste(unittest.TestCase):
    
    
    def test_ticket_vencido(self):
        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        saldo = scooby.PRECO_DA_PASSAGEM + 30.0
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)
        catraca = scooby.Catraca(concessionaria='sptrans')
        
        with self.assertRaises(scooby.ErrorTicketExpirado):
            catraca.liberar(ticket)
            
    def test_saldo_insuficiente(self):
        validade = datetime.datetime.now() + datetime.timedelta(days=2)
        saldo = scooby.PRECO_DA_PASSAGEM - 1.0
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)
        catraca = scooby.Catraca(concessionaria='sptrans')
        
        with self.assertRaises(scooby.ErrorSaldoInsuficiente):
            catraca.liberar(ticket)
    
    def test_concessionaria_diferente(self):
        validade = datetime.datetime.now() + datetime.timedelta(days=2)
        saldo = scooby.PRECO_DA_PASSAGEM + 10.0
        concessionaria = 'emtu'

        ticket = scooby.Ticket(validade, saldo, concessionaria)
        catraca = scooby.Catraca(concessionaria='sptrans')
        
        with self.assertRaises(scooby.ErrorConcessionariaDiferente):
            catraca.liberar(ticket)
            
    def test_catraca_liberada(self):
        validade = datetime.datetime.now() + datetime.timedelta(days=2)
        saldo = scooby.PRECO_DA_PASSAGEM + 10.0
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)
        catraca = scooby.Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)
        
        self.assertTrue(catraca.esta_liberada)
        self.assertTrue(ticket.saldo == (saldo - scooby.PRECO_DA_PASSAGEM))

        
        
if __name__ == '__main__':
    unittest.main()
    

print(scooby.Ticket)
