class Orders:
    def combine_orders(self, requests, n_max):

        #validar se existem requisições
        if requests is None or len(requests) <= 0:
            raise Exception("Não há requisições abertas.")
        
        #validar o número informado do top_n
        if n_max is None or n_max <= 0:
            raise Exception("Quantidade de valor máximo inválido.")

        trips = []
        index_requests_used = []

        #percorre as requisições
        for i in range(len(requests)):
            best_combination = None
            value_best_combination = 0

            #verifica se a requisição já está numa viagem
            if i in index_requests_used:
                continue

            #percorre as requisições, comparando com todas as outras
            for j in range(i + 1, len(requests)):
                #verifica se a requisição já está numa viagem
                if j in index_requests_used:
                    continue

                #cria a soma e verifica se a soma dos pedidos é menor ou igual ao valor máximo permitido
                sum_actual = requests[i] + requests[j]
                if sum_actual <= n_max:
                    #se for a primeira combinação válida, armazena seus indices
                    if best_combination is None:
                        best_combination = {'I': i, 'J': j}
                    #senão, alimenta o valor da melhor combinação
                    else:
                        value_best_combination = requests[best_combination['I']] + requests[best_combination['J']]
                    #se a soma atual for melhor que a melhor soma até agora, atualize a melhor combinação
                    if value_best_combination < sum_actual:
                        best_combination = {'I': i, 'J': j}
            
            #se não houver nenhuma combinação válida para o pedido atual, adicione-o como uma viagem única e
            #adicione o índice do pedido atual aos índices usados
            if best_combination is None:
                trips.append({'I': i, 'J': j})
                index_requests_used.append(i)
            else:
            #senão adicione os índices da melhor combinação aos índices usados e a melhor combinação às viagens
                index_requests_used.append(best_combination['I'])
                index_requests_used.append(best_combination['J'])
                trips.append(best_combination)
        

        #retornar o numero mínimo de viagens, inteiro
        return len(trips)
