def competicao():
    total = 1000000000
    for i in range(3):
        nome = input('Insira o nome do competidor: ')
        hora = int(input('Insira as horas: '))
        minuto = int(input('Insira os minutos: '))
        segundo = int(input('Insira os segundos: '))

        total_horas = (hora * 3600) + (minuto * 60) + segundo

        if total_horas < total:
            total = total_horas
            hora_final = hora
            vencedor = nome
            minuto_final = minuto
            segundo_final = segundo
    return hora_final, minuto_final, segundo_final, vencedor

final_hour, final_minute, final_second, winner = competicao()

print(f'{winner} levou {final_hour} horas, {final_minute} minutos, {final_second} segundos e ganhou a competição!')
