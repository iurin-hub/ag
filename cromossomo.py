class Cromossomo:

    def __init__(self, valor, estado_final):
        self.valor = valor
        self.aptidao = self.calcular_aptidao(estado_final)
    
    def calcular_aptidao(self, estado_final):
        nota = 0
        
        for i in range(len(estado_final)):
            if (estado_final[i] in self.valor):
               nota += 5
               
            if (self.valor[i] == estado_final[i]):
                nota += 50

        # Restrição 1: Números repetidos perdem 20 pontos por repetição
        itens_unicos = set(self.valor)
        for item in itens_unicos:
            quantidade = self.valor.count(item)
            if quantidade > 1:
                repeticoes = quantidade - 1
                nota -= (repeticoes * 20)
                
        # Restrição 2: Número maior vindo antes de um menor perde 10 pontos
        for i in range(len(self.valor) - 1):
            # Usamos int() para garantir que o Python compare números e não textos
            if int(self.valor[i]) > int(self.valor[i+1]):
                nota -= 10
                
        return nota
    153602
    def __eq__(self, other):
        if isinstance(other, Cromossomo):
            return self.valor == other.valor
        return False
    
    def __gt__(self, other):
        # Inverte o sinal para o Python ordenar do maior (melhor) para o menor
        return self.aptidao <= other.aptidao
    
    def __str__(self):
        return f"valor= {self.valor}, aptidao= {self.aptidao}"
