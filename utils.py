import pandas as pd


enem = (
    pd.read_csv('dados/MICRODADOS_ENEM_2022.csv', encoding='latin1', delimiter=';')
)

def mapear_idade(faixa_etaria):
    if faixa_etaria <= 10:
        return 'Menor de 26 anos'
    else:
        return '26 anos ou mais'

estado_civil = {
    0: 'Não informado',
    1: 'Solteiro(a)',
    2: 'Casado(a)/Mora com companheiro(a)',
    3: 'Divorciado(a)/Desquitado(a)/Separado(a)',
    4: 'Viúvo(a)'
}

cor_raca = {
    0: 'Não declarado',
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena '
}

nacionalidade = {
    0: 'Não declarado',
    1: 'Brasileiro(a)',
    2: 'Brasileiro(a) Naturalizado(a)',
    3: 'Estrangeiro(a)',
    4: 'Brasileiro(a) Nato(a), nascido(a) no exterior',
}

situacao_ensino_medio = {
    1: 'Já concluí o Ensino Médio',
    2: 'Estou cursando e concluirei o Ensino Médio em 2020',
    3: 'Estou cursando e concluirei o Ensino Médio após 2020',
    4: 'Não concluí e não estou cursando o Ensino Médio',
}


def mapear_ano_conclusao(ano):
    if ano == 0:
        return 'Não informado'
    elif ano <=6:
        return 'Concluiu depois de 2013'
    else:
        return 'Concluiu em 2013 ou antes'
    
tipos_escola = {
    1: 'Não Respondeu',
    2: 'Pública',
    3: 'Privada',
    4: 'Exterior'
}

tipos_ensino = {
    1: 'Ensino Regular',
    2: 'Educação Especial - Modalidade Substitutiva',
    3: 'Educação de Jovens e Adultos'
}

treineiro = {
    1: 'Sim',
    0: 'Não'
}

status_redacao = {
    1: 'Sem problemas',
    2: 'Anulada',
    3: 'Cópia Texto Motivador',
    4: 'Em Branco',
    6: 'Fuga ao tema',
    7: 'Não atendimento ao tipo textual',
    8: 'Texto insuficiente',
    9: 'Parte desconectada'
}

faixas_renda = {
    'A': 0,
    'B': 1045,
    'C': 1567.50,
    'D': 2090,
    'E': 2612.50,
    'F': 3135,
    'G': 4180,
    'H': 5225,
    'I': 6270,
    'J': 7315,
    'K': 8360,
    'L': 9405,
    'M': 10450,
    'N': 12540,
    'O': 15675,
    'P': 20900,
    'Q': float('inf')  # infinito, para representar "Acima de R$ 20.900,00"
}

# Função para atribuir a faixa de renda
def atribuir_grupo_renda(valor):
    if valor == 0:
        return 'Nenhuma Renda'
    elif valor <= 1567.50:
        return 'Até R$ 1.567,50'
    elif valor <= 6270:
        return 'De R$ 1.567,51 até R$ 6.270,00'
    elif valor <= 20900:
        return 'De R$ 6.270,01 até R$ 20.900,00'
    else:
        return 'Acima de R$ 20.900,00'
    
def atribuir_grupo_moradores(valor):
    if valor == 1:
        return 'Moro Sozinho(a)'
    elif valor <= 5:
        return '2 a 5 pessoas'
    elif valor <= 10:
        return '6 a 10 pessoas'
    else:
        return 'Mais de 10 pessoas'

# Aplicando o mapeamento às colunas
enem['TP_FAIXA_ETARIA'] = enem['TP_FAIXA_ETARIA'].apply(mapear_idade)
enem['TP_ESTADO_CIVIL'] = enem['TP_ESTADO_CIVIL'].map(estado_civil)
enem['TP_COR_RACA'] = enem['TP_COR_RACA'].map(cor_raca)
enem['TP_NACIONALIDADE'] = enem['TP_NACIONALIDADE'].map(nacionalidade)
enem['TP_ST_CONCLUSAO'] = enem['TP_ST_CONCLUSAO'].map(situacao_ensino_medio)
enem['TP_ANO_CONCLUIU'] = enem['TP_ANO_CONCLUIU'].apply(mapear_ano_conclusao)
enem['TP_ESCOLA'] = enem['TP_ESCOLA'].map(tipos_escola)
enem['TP_ENSINO'] = enem['TP_ENSINO'].map(tipos_ensino)
enem['IN_TREINEIRO'] = enem['IN_TREINEIRO'].map(treineiro)
enem['TP_STATUS_REDACAO'] = enem['TP_STATUS_REDACAO'].map(status_redacao)
enem['Q006'] = enem['Q006'].map(faixas_renda).apply(atribuir_grupo_renda)
enem['Q005'] = enem['Q005'].apply(atribuir_grupo_moradores)


enem.to_csv('dados/dados_enem_tratados.csv', index=False)