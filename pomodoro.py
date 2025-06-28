import time
import os
import sys

# --- Configurações ---
# Duração dos períodos em minutos. Para testar, você pode usar valores menores (ex: 0.1 para 6 segundos).
MINUTOS_FOCO = 25
MINUTOS_PAUSA_CURTA = 5
MINUTOS_PAUSA_LONGA = 15
SESSÕES_ATE_PAUSA_LONGA = 4

def limpar_tela():
    """Limpa a tela do terminal de forma compatível com Windows, Linux e macOS."""
    # 'nt' é para Windows, o resto é para Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def contagem_regressiva(minutos):
    """Executa uma contagem regressiva para a quantidade de minutos fornecida."""
    total_segundos = int(minutos * 60)
    
    while total_segundos > 0:
        # divmod é uma função elegante que retorna o quociente e o resto da divisão
        mins, segs = divmod(total_segundos, 60)
        
        # Formata o tempo para sempre ter dois dígitos (ex: 05:09)
        timer = f'{mins:02d}:{segs:02d}'
        
        # Imprime o tempo na mesma linha, substituindo o conteúdo anterior
        # \r (retorno de carro) move o cursor para o início da linha
        sys.stdout.write('\r' + timer)
        sys.stdout.flush()
        
        time.sleep(1)
        total_segundos -= 1
    
    # Imprime uma linha em branco no final para não sobrescrever a última atualização (00:00)
    print()

def main():
    """Função principal que executa os ciclos do Pomodoro."""
    sessoes_completas = 0
    
    try:
        while True:
            # --- Ciclo de Foco ---
            limpar_tela()
            print("🍅 POMODORO TIMER 🍅")
            print(f"Sessões completas: {sessoes_completas}")
            print(f"\nIniciando sessão de foco #{sessoes_completas + 1}. Mantenha a concentração!")
            contagem_regressiva(MINUTOS_FOCO)
            
            sessoes_completas += 1
            print("\nSessão de foco terminada! Hora da pausa.")
            # \a é o caractere de "sino" do terminal, que emite um som de alerta
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(2) # Pausa para o usuário ler a mensagem

            # --- Ciclo de Pausa ---
            limpar_tela()
            print("🍅 POMODORO TIMER 🍅")
            print(f"Sessões completas: {sessoes_completas}")

            if sessoes_completas % SESSÕES_ATE_PAUSA_LONGA == 0:
                print(f"\nÓtimo trabalho! Você completou {SESSÕES_ATE_PAUSA_LONGA} sessões. Aproveite uma pausa longa!")
                contagem_regressiva(MINUTOS_PAUSA_LONGA)
            else:
                print("\nFaça uma pausa curta. Estique as pernas!")
                contagem_regressiva(MINUTOS_PAUSA_CURTA)
            
            print("\nPausa terminada. Prepare-se para a próxima sessão de foco!")
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(3)

    except KeyboardInterrupt:
        # Captura o Ctrl+C para sair do programa de forma elegante
        print("\n\nCronômetro interrompido. Bom trabalho hoje!")
        sys.exit(0)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()