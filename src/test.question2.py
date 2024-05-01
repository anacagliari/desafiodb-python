import unittest

from question2 import Orders

class TestOrders(unittest.TestCase):
    #prepara ambiente de teste, executa a cada teste feito
    def setUp(self):
        self.ordem = Orders()

    def test_combine_orders(self):

        #teste com uma lista pequena, com dados de entrada do exemplo
        requests_1 = [70, 10, 30]
        n_max_1 = 100
        #chamando a função à ser testada com os dados informados acima, informando o resultado esperado
        self.assertEqual(self.ordem.combine_orders(requests_1, n_max_1), 2)

        #teste com uma lista onde todas as viagens são únicas
        requests_2 = [100, 90, 95]
        n_max_2 = 100
        #chamando a função à ser testada com os dados informados acima, informando o resultado esperado
        self.assertEqual(self.ordem.combine_orders(requests_2, n_max_2), 3)

#executa o teste
if __name__ == '__main__':
    unittest.main()
