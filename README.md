# GS-IOT-GoalRoad

## Link do projeto no Youtube: https://youtu.be/cqAdSfbL69M

## 👨‍💻 Integrantes do Grupo
| Nome           | RM        |
|----------------|-----------|
| Daniel Akiyama | RM 558263 |
| Danilo Correia | RM 557540 |
| João Pedro R   | RM 558199 |

## 🤖 IA - IA generativa para guiar a nova mão de obra profissional do mercado

Este projeto demonstra uma **IA generativa** utilizando o serviço Ollama, API e um Front-end para receber as informações.

---

## 📖 Visão Geral
O código recebe a carreira que o deseja seguir, e desenvolve um road map para o usuário seguir de cursos, livros, oficinas e habilidades.

---

## 🔧 Tecnologias Utilizadas
- **Python**: para a API e puxar a resposta da IA
- **Ollama**: Serviço de IA utilizado para geração das respostas
- **HTML + JavaScript**: Para a criação da front-page para o usuário fazer a comunicação

---

## 🦙 Ollama
O Ollama foi utilizado devido a sua semelhancia com o chat-gpt, que é a IA generativa mais comumente conhecida, porém enquanto a utilização do chat-gpt em uma API é pago, o Ollama é gratuito

## Objetivo do fluxo:

- Usuário manda uma mensagem no chat, por exemplo: Quero ser cientista de dados, o que devo fazer?

- O front-end, informa o python sobre os dados recebidos

- O python, transforma a mensagem em um json e requisita da IA um retorno sobre aquela mensagem

- A IA retorna uma mensagem em json, o python desfaz o json e manda para o front-end

- O front-end exibi a mensagem para o usuário


### 📚 Bibliotecas

#### 🐍 Python
- Flask - API
  
- CORS - libera o acesso do front
  
- JSON - geração de json para a transmissão de informações do Ollama, python e front-end
  
- requests - para a transmissão de informação

<img width="1749" height="898" alt="image" src="https://github.com/user-attachments/assets/39704b64-337e-4a2c-94a3-543cf24d4361" />
