#  💰 Projeto "Invista-me"

Bem-vindo ao projeto "Invista-me"! Este é um aplicativo web desenvolvido em Python/Django que tem como objetivo auxiliar os usuários a gerenciar seus investimentos de forma simples e eficiente. Com o Invista-me, os usuários podem criar uma conta, fazer login, registrar seus investimentos e acompanhar seu desempenho ao longo do tempo.
---
## Funcionalidades Principais

- **Cadastro de Usuário:** Os usuários podem se registrar no sistema fornecendo um nome de usuário, endereço de e-mail e senha.

- **Login e Logout:** Os usuários podem fazer login e logout em suas contas para acessar e gerenciar seus investimentos.

- **Adicionar Investimento:** Após fazer login, os usuários podem adicionar novos investimentos especificando os seguintes detalhes:
    - Nome do investimento (por exemplo, "LIVRO")
    - Valor do investimento (por exemplo, R$100,00)
    - Data do investimento (por exemplo, 27/07/2021)
    - Status de pagamento (por exemplo, Pago: True/False)

- **Editar Investimento:** Os usuários têm a opção de editar os detalhes de seus investimentos existentes, como valor, data e status de pagamento.

- **Excluir Investimento:** Os usuários podem excluir investimentos que não desejam mais acompanhar.

---

## 🛠️ Instalação

Siga os passos abaixo para configurar o ambiente do projeto e executá-lo localmente:

1. Clone o repositório do Invista-me para o seu computador:

```
git clone https://github.com/xBigJhow/Invista_Me.git cd invista-me
```

2. Crie um ambiente virtual para o projeto (recomendamos usar o virtualenv):

```
python -m venv venv
```

3. Ative o ambiente virtual:
No Windows:
```
venv\Scripts\activate
```
No Linux/Mac:

```
source venv/bin/activate
```

4. Instale as dependências do projeto:
```
pip install -r requirements.txt
```
5. Aplique as migrações do banco de dados:

```
python manage.py migrate
```

6. Crie um superusuário para acessar a área de administração:

```
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

8. Acesse o projeto no seu navegador: http://localhost:8000/

---
# 🖇️ Contribuição
Se você deseja contribuir para o desenvolvimento do Invista-me, siga os passos abaixo:

- Faça um fork do repositório e clone-o para o seu computador.
- Crie uma branch para a sua feature ou correção: git checkout -b nome-da-feature.
- Faça as alterações desejadas no código.
- Execute os testes para garantir que tudo está funcionando corretamente: python manage.py test.
- Envie as suas alterações: git push origin nome-da-feature.
- Abra um pull request no repositório original.
---
# 📄 Licença

O Invista-me é um software de código aberto sob a licença MIT.
