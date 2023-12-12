class Participante:
    def __init__(self, nome, idade, endereco, reside_sp, horario_evento):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.reside_sp = reside_sp
        self.horario_evento = horario_evento

def cadastrar_participante():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    endereco = input("Digite seu endereço: ")
    reside_sp = input("Você reside em SP? (Sim/Não): ").lower() == "sim"
    horario_evento = input("Você confirma que o evento ocorre à noite? (Sim/Não): ").lower() == "sim"

    participante = Participante(nome, idade, endereco, reside_sp, horario_evento)
    return participante

def verificar_condicoes(participante):
    if not participante.idade >= 18:
        return "Você deve ser maior de idade para participar do evento."

    if not participante.reside_sp:
        return "A participação no evento é restrita a moradores do estado de São Paulo."

    if not participante.horario_evento:
        return "Você deve confirmar que o evento ocorre à noite para participar."

    return None

def verificar_vagas_disponiveis(total_inscritos, limite_vagas):
    if total_inscritos >= limite_vagas:
        return "Desculpe, as inscrições estão encerradas. Todas as vagas foram preenchidas."

    return None

def main():
    limite_vagas = 50
    total_inscritos = 0
    participantes = []

    while total_inscritos < limite_vagas:
        print("\n=== Inscrição para o Evento ===")
        participante = cadastrar_participante()

        # Verificar condições
        condicao = verificar_condicoes(participante)

        if condicao is not None:
            print(f"\nErro na inscrição: {condicao}")
            continue

        # Verificar vagas disponíveis
        mensagem_vagas = verificar_vagas_disponiveis(total_inscritos, limite_vagas)

        if mensagem_vagas is not None:
            print(f"\nErro na inscrição: {mensagem_vagas}")
            break

        # Inscrição validada
        total_inscritos += 1
        participantes.append(participante)
        print("\nInscrição validada com sucesso!")

    print("\n=== Lista de Participantes ===")
    for participante in participantes:
        print(f"Nome: {participante.nome}, Idade: {participante.idade}, Endereço: {participante.endereco}")

if __name__ == "__main__":
    main()
