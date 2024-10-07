import flet as ft

# Tópicos do Cadastro
    #por foto
    #-------------------------------------------------------------------
matricula = ft.TextField(label="Matrícula")
nomecompleto = ft.TextField(label="Nome")
cpf = ft.TextField(label="CPF")
datanascimento = ft.TextField(label="Data de Nascimento")


sexo = ft.Dropdown(
label="Sexo",
options=[
    ft.dropdown.Option("Masculino"),
    ft.dropdown.Option("Feminino")
],
value="",  # Valor padrão
     )
    #--------------------------------------
pai_membro = ft.Dropdown(
label="Seu pai é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
value="",  # Valor padrão
        )
    #----------------------------------------   
nome_mae = ft.TextField(label="Nome da Mãe")
mae_membro = ft.Dropdown(
label="Sua mãe é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
],
value="",  # Valor padrão
        )
    #--------------------------------------
nome_conjuge = ft.TextField(label="Nome do Cônjuge")
datanascimento_conjuge = ft.TextField(label="Data de Nascimento do Cônjuge")

conjuge_membro = ft.Dropdown(
label="Seu cônjuge é membro da PIB Pavuna?",
options = [
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
value="",  # Valor padrão
        )
tipo_sanguineo = ft.TextField(label="Tipo Sanguíneo")
estado_civil = ft.TextField(label="Estado Civil")
datacasamento = ft.TextField(label="Data do Casamento")
profissao = ft.TextField(label="Profissão")
naturalidade = ft.TextField(label="Naturalidade")
nacionalidade = ft.TextField(label="Nacionalidade")
rua = ft.TextField(label="Rua")
complemento = ft.TextField(label="Complemento")
bairro = ft.TextField(label="Bairro")
municipio = ft.TextField(label="Município")
estado = ft.TextField(label="Estado")
cep = ft.TextField(label="CEP")
tel_residencial = ft.TextField(label="Telefone Residencial")
tel_celular = ft.TextField(label="Telefone Celular")
email = ft.TextField(label="E-mail")
nome_pai = ft.TextField(label="Nome do Pai")
cargo_atual = ft.TextField(label = "Cargo Atual")
databatismo = ft.TextField(label = "Data do Batismo")
igrejabatismo = ft.TextField(label = "Igreja onde foi bartizado")
entradaPIB = ft.TextField(label="Quando se Tornou membro PIB?")
formaentrada = ft.TextField(label = "Como se tornou membro da PIB?")
nome_filho1 = (ft.TextField(label="Nome Filho(a) 1"))
datanascimento_filho1 = (ft.TextField(label="Data de Nascimento do Filho(a) 1"))
    
filho1_membro = ft.Dropdown(
label="Seu filho(a) 1 é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

nome_filho2 = (ft.TextField(label="Nome Filho(a) 2"))
datanascimento_filho2 = (ft.TextField(label="Data de Nascimento do Filho(a) 2"))
    
filho2_membro = ft.Dropdown(
label="Seu filho(a) 2 é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

nome_filho3 = (ft.TextField(label="Nome Filho(a) 3"))
datanascimento_filho3 = (ft.TextField(label="Data de Nascimento do Filho(a) 3"))
    
filho3_membro = ft.Dropdown(
label="Seu filho(a) 3 é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

nome_filho4 = (ft.TextField(label="Nome Filho(a) 4"))
datanascimento_filho4 = (ft.TextField(label="Data de Nascimento do Filho(a) 4"))
    
filho4_membro = ft.Dropdown(
label="Seu filho(a) 4 é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

nome_filho5 = (ft.TextField(label="Nome Filho(a) 5"))
datanascimento_filho5 = (ft.TextField(label="Data de Nascimento do Filho(a) 5"))
    
filho5_membro = ft.Dropdown(
label="Seu filho(a) 5 é membro da PIB Pavuna?",
options=[
    ft.dropdown.Option("Sim"),
    ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

variaveis = [
    nomecompleto,
    matricula,
    cpf,
    datanascimento,
    tipo_sanguineo,
    estado_civil,
    datacasamento,
    profissao,
    naturalidade,
    nacionalidade,
    rua,
    complemento,
    bairro,
    municipio,
    estado,
    cep,
    tel_residencial,
    tel_celular,
    email,
    nome_pai,
    nome_mae,
    nome_conjuge,
    datanascimento_conjuge,
    cargo_atual,
    databatismo,
    igrejabatismo,
    entradaPIB,
    formaentrada,
    sexo,
    pai_membro,
    mae_membro,
    conjuge_membro,
    nome_filho1,
    datanascimento_filho1,
    filho1_membro,
    nome_filho2,
    datanascimento_filho2,
    filho2_membro,
    nome_filho3,
    datanascimento_filho3,
    filho3_membro,
    nome_filho4,
    datanascimento_filho4,
    filho4_membro,
    nome_filho5,
    datanascimento_filho5,
    filho5_membro,
]


