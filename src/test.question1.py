import unittest

from question1 import Contract, Contracts

class TestContracts(unittest.TestCase):
    def test_get_top_N_open_contracts(self):
        #teste com dados de entrada do exemplo
        contracts = [
            Contract(1, 1), 
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        renegotiated = [3]  
        top_n = 3           

        #resultado esperado
        expected_open_contracts = [5, 4, 2]  

        #chamando a função à ser testada com os dados informados acima
        contracts_obj = Contracts()
        actual_open_contracts = contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        #confere se o retorno esperado é o mesmo retorno da função
        self.assertEqual(expected_open_contracts, actual_open_contracts)

#executa o teste
if __name__ == '__main__':
    unittest.main()