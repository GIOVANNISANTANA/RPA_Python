<h1 align="center"> :hammer:  RPA_Python </h1>

- Automação de processos no windows usando python.
- É necessário criar uma maquina virtual usando os passos:
- passo 1: 
> "python -m venv venv" (o ultimo venv pode ser outro nome a escolha do usuário)
- passo 2: caso seja o primeiro acesso é preciso ativar via PowerShell no windows com a seguinte linha: 
> "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process" (caso já esteja ativado, pule para o passo 3)
- passo 3: 
> ".\venv\Scripts\Activate.ps1"
- Pronto! maquina virtual criada.
```
```
- caso queira criar um executável prossiga com os seguintes passos:
- passo 1: 
> pip install pyinstaller (para instalar o criador de executável)
- passo 2: 
> pyinstaller --onefile main.py (main.py é o nome do arquivo que deseja tornar executável)

- Pronto! Agora temos um executável do codigo feito.
