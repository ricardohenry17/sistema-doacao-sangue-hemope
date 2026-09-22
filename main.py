from banco import (
    criar_tabelas,
    registrar_atendimento,
    buscar_atendimentos
)

from modulos.doacao.assistente_doacao import iniciar_doacao
from modulos.consulta.assistente_consulta import menu_consultas
from modulos.exames.assistente_exames import iniciar_exames


# ============================================================
# CRIAÇÃO DAS TABELAS
# ============================================================

criar_tabelas()


# ============================================================
# CABEÇALHO
# ============================================================

print("\n======================================")
print("       ASSISTENTE VIRTUAL HEMOPE")
print("======================================")

print("\nBem-vindo ao Assistente Virtual HEMOPE!")


# ============================================================
# MENU PRINCIPAL
# ============================================================

while True:

    print("\n======================================")
    print("       ASSISTENTE VIRTUAL HEMOPE")
    print("======================================")

    print("\nComo podemos ajudar?")

    print("\n1 - 🩸 Doação de sangue")
    print("2 - 📅 Marcação de consulta")
    print("3 - 🧪 Marcação de exames")
    print("4 - 📊 Histórico de atendimentos")
    print("5 - Sair")

    opcao = input(
        "\nDigite o número da opção: "
    ).strip()


    # ========================================================
    # DOAÇÃO
    # ========================================================

    if opcao == "1":

        print("\n🩸 Setor de Doação")

        iniciar_doacao()


    # ========================================================
    # CONSULTAS
    # ========================================================

    elif opcao == "2":

        print("\n📅 Setor de Consultas")

        # A identificação do paciente será feita
        # dentro do módulo de consultas.
        #
        # Primeiro será solicitado:
        # - Nome completo
        # - Número do prontuário
        #
        # Depois disso, o paciente poderá utilizar
        # as funções do setor de consultas.

        menu_consultas()


    # ========================================================
    # EXAMES
    # ========================================================

    elif opcao == "3":

        print("\n🧪 Setor de Exames")

        iniciar_exames()


    # ========================================================
    # HISTÓRICO
    # ========================================================

    elif opcao == "4":

        print("\n======================================")
        print("       HISTÓRICO DE ATENDIMENTOS")
        print("======================================")

        print(
            "\n⚠️ A identificação do paciente para "
            "consulta ao histórico será definida "
            "pela identificação do WhatsApp."
        )

        print(
            "\nNo momento, o histórico será utilizado "
            "após a integração com o WhatsApp."
        )


    # ========================================================
    # SAIR
    # ========================================================

    elif opcao == "5":

        print(
            "\nEncerrando o Assistente Virtual HEMOPE..."
        )

        break


    # ========================================================
    # OPÇÃO INVÁLIDA
    # ========================================================

    else:

        print(
            "\n❌ Opção inválida. "
            "Escolha uma opção de 1 a 5."
        )
