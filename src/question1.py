class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)

class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):

        #validar se existem contratos
        if open_contracts is None or len(open_contracts) <= 0:
            raise Exception("Não há contratos abertos.")
        
        #validar o número informado para saber quantos devedores aparecerão no top_n
        if top_n is None or top_n <= 0:
            raise Exception("Quantidade de maiores devedores inválido.")

        nDebtors = []

        #ordena do maior para o menor pelo debt
        ordered_debtor_contracts = sorted(open_contracts, key=lambda contract: contract.debt, reverse=True)

        #busca os maiores devedores até top_n, desprezando os já renegociados
        for contract in ordered_debtor_contracts:
            if renegotiated_contracts is not None and contract.id in renegotiated_contracts:
                continue
            
            nDebtors.append(contract.id)

            if len(nDebtors) == top_n:
                break

        #retorna a lista de maiores devedores, de acordo com quantos posições quer visualizar (top_n)
        return nDebtors
    