# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        saldo_atual = self.plano.verificar_saldo()

        # TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':

        if saldo_atual >= custo:
            self.plano.deduzir_saldo(custo)
            saldo_restante = self.plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


# TODO: Verifique se o saldo do plano é suficiente para a chamada.

# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.

# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    # TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        self.saldo -= valor


# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:


# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
