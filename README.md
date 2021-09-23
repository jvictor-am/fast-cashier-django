<h2 align="center">
  Fast Cashier - JV
</h2>

## :computer: Sobre

Backend para projeto de um caixa rápido de uma empresa hipotética. <br/>
[Clique aqui](https://fast-cashier-dj.herokuapp.com/api/) para ver a API. Deploy realizado com o heroku.

## Funcionalidades

  1. Consultar e cadastrar os produtos ou serviços e seus percentuais de comissão. <br/>
    - endpoint de [product](https://fast-cashier-dj.herokuapp.com/api/product/)
  2. Consultar e cadastrar os clientes (apenas nome). <br/>
    - endpoint de [customer](https://fast-cashier-dj.herokuapp.com/api/customer/)
  3. Consultar e cadastrar os vendedores (apenas nome). <br/>
    - endpoint de [seller](https://fast-cashier-dj.herokuapp.com/api/seller/)
  4. Lançar uma venda (data/hora, vendedor, cliente, itens e quantidades. <br/>
    - endpoint de [order](https://fast-cashier-dj.herokuapp.com/api/order/)
  5. Consultar comissões de dado vendedor em dado período. <br/>
    - endpoint de [seller/pk/commission/?start_date=2021-09-19&end_date=2021-09-21](https://fast-cashier-dj.herokuapp.com/api/seller/2/commission/?start_date=2021-09-1&end_date=2021-09-21)

## Feito com

- Python
- Django
- Django-Rest-Framework
- PostgreSQL
- Docker
- Pytest
- etc...

## Exemplos de json para realizar cadastros:
  - endpoint de [product](https://fast-cashier-dj.herokuapp.com/api/product/):
    ```
    {
        "name": "Teste01",
        "price": 150,
        "fixed_commission_percentage": 8
    }
    ```
  - endpoint de [customer](https://fast-cashier-dj.herokuapp.com/api/customer/):
    ```
    {
        "name": "Tester"
    }
    ```
  - endpoint de [seller](https://fast-cashier-dj.herokuapp.com/api/seller/):
    ```
    {
        "name": "Tester02"
    }
    ```
 - endpoint de [order](https://fast-cashier-dj.herokuapp.com/api/order/):
    ```
    {
        "customer": 3,
        "seller": 4,
        "items": [
            {
                "product": 3,
                "quantity": 4
            }
        ]
    }
    ```

## Instruçoẽs para instalação em ambiente local:

  - Clonar projeto:
    ```
    $ git clone git@github.com:jvictor-am/fast-cashier-django.git
    ```
  - Ir para pasta do projeto:
    ```
    $ cd fast-cashier-django
    ```
  - Fazer setup de [ambiente virtual](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - Instalar dependências:
    ```
    $ pip install -r requirements.txt
    ```
  - Tenha um ambiente docker em sua máquina para realizar o comando abaixo e criar o banco de dados postgres:
    ```
    $ docker-compose up -d
    ```
  - Aplicar migrações do projeto:
    ```
    $ python manage.py migrate
    ```
  - Criar superusuário:
    ```
    $ python manage.py createsuperuser
    ```
  - Executar em localhost:
    ```
    $ python manage.py runserver
    ```
  - A partir daqui você deve ser capaz de visualizar API root no browser após setar DEBUG = True no arquivo de settings.py:
    ```
    $ http://localhost:8000/api/
    ```
  - Se verificar algum warning no terminal sobre pasta static, execute:
    ```
    $ python manage.py collectstatic
    ```

---

# Author

[**João Victor**](https://www.linkedin.com/in/jo%C3%A3o-victor-de-andrade-mesquita-848a09122/)

<h2 align="center">
  Thank You!
</h2>
