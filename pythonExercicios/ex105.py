print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 105', '-' * 33)
print('-' * 19, 'Função - Analisando de Gerando Dicionários', '-' * 19)
print('=-' * 41)


def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação.
        :return: dicionário com várias informações sobre a situação da  turma.
    """
    maior = max(n)
    menor = min(n)
    med = sum(n)/len(n)
    if sit:
        if med >= 7.5:
            situacao = 'BOA'
        elif med >= 5:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'
        turma = {'total': len(n), 'maior': maior, 'menor': menor, 'média': med, 'situação': situacao}
    else:
        turma = {'total': len(n), 'maior': maior, 'menor': menor, 'média': med}
    return turma


print('-'*30)
print(notas(3.5, 6.5, 2, sit=True))
