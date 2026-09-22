# 🩸 Assistente Virtual HEMOPE

Um sistema interativo desenvolvido em **Python** para otimizar o atendimento, agendamento de consultas, exames e doações de sangue para o HEMOPE (Hemocentro de Pernambuco).

---

### 🚀 Funcionalidades do Sistema

O assistente opera através de um menu modular intuitivo que divide as responsabilidades em setores essenciais:

* **🩸 Doação de Sangue:** Orienta e inicia o processo para potenciais doadores.
* **📅 Marcação de Consulta:** Gerencia a identificação do paciente (nome e prontuário) para marcação de consultas médicas.
* **🧪 Marcação de Exames:** Direciona o utilizador para o setor de exames laboratoriais.
* **📊 Histórico de Atendimentos:** Estrutura preparada para rastreamento de dados de atendimento (com integração futura via API/WhatsApp).

---

### 📂 Estrutura do Projeto

O projeto segue boas práticas de engenharia de software, utilizando a **modularização** para separar a lógica de negócios e a persistência de dados:

```text
sistema-doacao-sangue-hemope/
│
├── modulos/
│   ├── doacao/
│   │   └── assistente_doacao.py
│   ├── consulta/
│   │   └── assistente_consulta.py
│   └── exames/
│       └── assistente_exames.py
│
├── banco.py          # Gerenciamento de tabelas e conexões
└── main.py           # Arquivo principal (Controlador do Menu)
