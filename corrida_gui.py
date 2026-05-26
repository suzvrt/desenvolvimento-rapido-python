total_lento = 0
total_moderado = 0
total_rapido = 0
total_elite = 0

qtd_corredores = int(input("Digite a quantidade de corredores: "))
print("------------------------------------------------------")

for i in range(qtd_corredores):
    print(f"\n--- Dados do {i+1}º Corredor ---")
    nome = input("Nome: ")
    distancia = float(input("Distância percorrida (em metros): "))
    tempo = float(input("Tempo gasto (em minutos): "))
    
    velocidade_media = (distancia / 1000) / (tempo / 60)
    
    if velocidade_media < 8:
        classificacao = "Lento"
        total_lento += 1
    elif 8 <= velocidade_media < 12:
        classificacao = "Moderado"
        total_moderado += 1
    elif 12 <= velocidade_media < 16:
        classificacao = "Rápido"
        total_rapido += 1
    else:
        classificacao = "Elite"
        total_elite += 1
        
    print("\nRESULTADO INDIVIDUAL:")
    print(f"Nome: {nome}")
    print(f"Distância: {distancia} metros")
    print(f"Tempo: {tempo} minutos")
    print(f"Velocidade Média: {velocidade_media:.2f} km/h")
    print(f"Classificação: {classificacao}")
    print("------------------------------------------------------")

print("\n" + "-----------" + " RESUMO FINAL DA PESQUISA " + "-----------")
print(f"Corredores Lentos:   {total_lento}")
print(f"Corredores Moderados: {total_moderado}")
print(f"Corredores Rápidos:  {total_rapido}")
print(f"Corredores Elite:    {total_elite}")
print("------------------------------------------------------")