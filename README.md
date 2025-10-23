# 🏦 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um **desafio de programação** em Python.  
O objetivo é criar um sistema bancário simples que permita ao usuário realizar **depósitos**, **saques** e **consultar o extrato** de sua conta.

---

## 🚀 Funcionalidades

O sistema oferece as seguintes operações:

- 💰 **Depósito** — Permite adicionar um valor positivo ao saldo.
- 💸 **Saque** — Permite retirar valores da conta, respeitando:
  - O limite de **R$ 500,00 por saque**;
  - O limite máximo de **3 saques por dia**;
  - O valor disponível em **saldo**.
- 📄 **Extrato** — Mostra todas as movimentações realizadas (depósitos e saques) e o saldo atual.
- ❌ **Sair** — Encerra o programa de forma segura.

---

## 🧠 Regras de Negócio

- O **saldo inicial** é `R$ 0,00`;
- Não é permitido realizar depósitos ou saques com valores negativos ou iguais a zero;
- Caso o usuário tente sacar mais do que o saldo disponível, o sistema exibirá uma mensagem de erro;
- Caso o limite de saque diário (3 saques) seja atingido, novas tentativas serão bloqueadas.

---

## 🧩 Estrutura do Código

O programa utiliza um **loop `while True`** para manter o menu ativo até que o usuário escolha a opção **[0] Sair**.  
Cada operação é tratada com condições `if / elif / else`, garantindo a validação de todas as regras.

### Variáveis principais:
| Variável | Descrição |
|-----------|------------|
| `saldo` | Valor total disponível na conta |
| `limite` | Limite máximo permitido por saque (`500`) |
| `extrato` | Armazena o histórico de movimentações |
| `numero_saques` | Contador de saques realizados |
| `LIMITE_SAQUES` | Quantidade máxima de saques permitidos por dia (`3`) |

---
