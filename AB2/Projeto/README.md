# Sistema de Planejamento de Matrícula

Este é um projeto desenvolvido como parte da disciplina de Computação Evolucionária para implementar um **sistema de aconselhamento pedagógico automatizado** para alunos do curso de Ciência da Computação (UFAL), com base no PPC2019.

## 🧑‍🎓 Alunos

- **Ruan Tenório de Melo**
- **Victor Hugo Silva Ângelo**
- **Vinícius da Costa Neitzke**

## 📊 Dados Utilizados

**Nome analisado**: Ruan Tenório de Melo ("de" é preposição)

### ⚙️ Parâmetros calculados a partir do nome:

- **Limite de disciplinas por semestre**: `8`
  - Cálculo: soma das letras do primeiro nome (`Ruan`), resultado dividido por 3 ⇒ resto `1` ⇒ limite = **8 disciplinas**
- **Ritmo de conclusão desejado**: `Maior tempo possível`
  - Cálculo: soma das letras do próximo nome (`Tenório`), resultado dividido por 3 ⇒ resto `1`
- **Ênfase escolhida**: `Sem ênfase`
  - Cálculo: soma das letras do próximo nome (`Melo`), resultado dividido por 3 ⇒ resto `2`
- **Critério de escolha de disciplinas**: `Todas do mesmo turno`
  - Cálculo: soma das letras do próximo nome (`Ruan`), resultado dividido por 3 ⇒ resto `1`

---


## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Viihtorugo/cc-computacao-evolucionaria-2024.2.git
    ```
2. Abra o terminal, vá para o diretório do repositório e digite o comando abaixo:
    ```bash
   make run_project
    ```
