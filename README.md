# 🔗 flask-simple-api

Uma API REST simples desenvolvida com **Flask** para realizar operações de CRUD (Create, Read, Update, Delete) em uma lista de itens em memória. Ideal para fins de aprendizado, prototipagem ou testes com consumo de APIs REST.

---

## 📌 Tópicos

- [📖 Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Como Executar](#️-como-executar)
- [📮 Endpoints da API](#-endpoints-da-api)
- [🧠 Explicação do Código](#-explicação-do-código)
- [📄 Licença](#-licença)
- [🤝 Contribuindo](#-contribuindo)

---

## 📖 Sobre o Projeto

Esta é uma API criada com Flask que utiliza uma base de dados em memória (lista Python) para armazenar e manipular itens. Ela implementa todos os métodos básicos de um CRUD e responde com dados em formato JSON.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask (framework web)
- JSON (formato de resposta padrão)
- Ferramentas de API como Postman ou Insomnia (opcional, para testar)

---

## ⚙️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/rafaelmoreirax/flask-simple-api.git
cd flask-simple-api
```

2. **Instale o Flask:**

```bash
pip install flask
```

3. **Execute a API:**

```bash
python main.py
```

4. **Acesse no navegador ou via ferramenta de testes:**

```
http://localhost:5000/
```

---

## 📮 Endpoints da API

| Método | Rota                | Descrição                          |
|--------|---------------------|-------------------------------------|
| GET    | `/`                 | Verifica se a API está online       |
| GET    | `/items`            | Retorna todos os itens              |
| GET    | `/items/<id>`       | Retorna um item específico por ID   |
| POST   | `/items`            | Adiciona um novo item               |
| PUT    | `/items/<id>`       | Atualiza um item existente          |
| DELETE | `/items/<id>`       | Remove um item por ID               |

### 🔸 Exemplo de JSON para POST/PUT

```json
{
  "name": "Novo Item",
  "description": "Descrição opcional"
}
```

---

## 🧠 Explicação do Código

- `items`: lista Python que atua como um banco de dados temporário em memória.
- `next_id`: contador para atribuir novos IDs únicos aos itens.
- Rotas implementadas com `@app.route()` para mapear os métodos HTTP.
- Utiliza `jsonify()` para retornar respostas no formato JSON.
- Valida entradas com `request.json` e mensagens de erro apropriadas.
- `debug=True`: útil durante o desenvolvimento para recarregar a API automaticamente em caso de alterações.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o repositório.
2. Crie sua branch: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'feat: nova funcionalidade'`
4. Push para sua branch: `git push origin minha-feature`
5. Abra um Pull Request.

---

## 👤 Autor

Feito com 🧠 por [Rafael Moreira](https://github.com/rafaelmoreirax)
