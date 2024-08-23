def verificar_acesso(cargo, dia_da_semana):
    # Lista de dias úteis
    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

    # Converter o cargo e o dia para minúsculas para evitar problemas com a entrada
    cargo = cargo.lower()
    dia_da_semana = dia_da_semana.lower()

    # Verificar se o cargo é um dos tipos especificados
    if cargo == "gerente":
        return "Acesso permitido."

    elif cargo == "analista":
        if dia_da_semana in dias_uteis:
            return "Acesso permitido."
        else:
            return "Acesso negado."

    elif cargo == "estagiário":
        if dia_da_semana in dias_uteis:
            return "Acesso permitido."
        else:
            return "Acesso negado."

    else:
        return "Cargo não reconhecido."

# Exemplo de uso
cargo = "analista"  # Exemplo de cargo
dia_da_semana = "sábado"  # Exemplo de dia da semana
resultado = verificar_acesso(cargo, dia_da_semana)
print(f"Cargo: {cargo}")
print(f"Dia da semana: {dia_da_semana}")
print(resultado)