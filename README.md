# Conversor de moeda com FastAPI (Python)
API para converter moedas utilizando FastAPI (Python) e alpha vantage


# Como Rodar

Clonar repositório
```cmd
git clone https://github.com/JoaoEnrique/conversor-fastapi.git
``` 

Instalar dependências
```cmd
pip install requirements.txt
```

Criar uma chave de API na alpha vantage e configurar .env
```cmd
ALPHA_VANTAGE_API_KEY=your-api-key
```

Rodar projeto
```cmd
uvicorn main:app --reload
```

<br>

# Exemplo de requisição. 
Converter DE BRL para USD e EUR
```cmd
http://127.0.0.1:8000/v2/async/converter/BRL
```

Body
```json
{
    "price": 10,
    "to_currencies": ["USD", "EUR"]
}
```


Resposta
```json
{
    "message": "success",
    "data": [
        {
            "USD": 1.75
        },
        {
            "EUR": 1.62
        }
    ]
}
```