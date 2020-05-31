def voto(ano):
    from datetime import date #É POSSIVEL IMPORTAR SÓ PRA DENTRO DA FUNÇÃO. ISSO ECONOMIZA MEMÓRIA
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print(voto(int(input('Digite seu ano de nascimento :'))))