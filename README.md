# Instalação e execução do projeto

1. **Criar e ativar um ambiente virtual**: Crie uma venv com `python -m venv .venv` e ative ela.
2. **Instalar dependências**: Instale as dependências com `pip install -r requirements.txt`. Caso haja algum erro relacionado ao FastAPI, o comando `pip install "fastapi[standard]"` adiciona as dependências adicionais para a cli.
3. **Rodar o servidor FastAPI**: Rode o comando `fastapi dev main.py` ou `uvicorn main:app --reload` para iniciar o servidor na porta 8000.
4. **Acessando a página web**: Acesse `http://localhost:8000/` para ter acesso ao form.
