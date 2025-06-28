import json
import os
import time

# Nome do arquivo que usaremos para armazenar os contatos
NOME_ARQUIVO = "contatos.json"

def carregar_contatos():
    """Carrega os contatos do arquivo JSON. Se o arquivo não existir, retorna uma lista vazia."""
    if os.path.exists(NOME_ARQUIVO):
        # Evita erro se o arquivo estiver completamente vazio
        if os.path.getsize(NOME_ARQUIVO) == 0:
            return []
        try:
            with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return [] # Retorna lista vazia se o JSON for inválido
    return []

def salvar_contatos(contatos):
    """Salva a lista de contatos no arquivo JSON com uma formatação legível."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(contatos, arquivo, indent=4, ensure_ascii=False)

def adicionar_contato(contatos):
    """Pede os dados de um novo contato e o adiciona à lista."""
    print("\n--- Adicionar Novo Contato ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("\n[ERRO] O nome é obrigatório!")
        return contatos

    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    # Cria um dicionário para o novo contato
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    
    contatos.append(novo_contato)
    salvar_contatos(contatos)
    print(f"\n[SUCESSO] Contato '{nome}' adicionado!")
    return contatos

def listar_contatos(contatos):
    """Exibe todos os contatos da lista de forma organizada."""
    print("\n--- Lista de Contatos ---")
    if not contatos:
        print("Nenhum contato na agenda.")
        return

    # Acha o nome mais longo para alinhar a formatação
    max_len = max(len(c["nome"]) for c in contatos) if contatos else 0

    for i, contato in enumerate(contatos, 1):
        print(f"{i}. Nome:     {contato['nome']:<{max_len}}")
        print(f"   Telefone: {contato.get('telefone', '-')}")
        print(f"   E-mail:   {contato.get('email', '-')}")
        print("-" * 25)

def buscar_contato(contatos):
    """Busca por contatos cujo nome contenha o termo pesquisado."""
    print("\n--- Buscar Contato ---")
    termo_busca = input("Digite o nome ou parte do nome para buscar: ").lower().strip()
    if not termo_busca:
        print("\n[ERRO] Termo de busca não pode ser vazio.")
        return

    encontrados = [c for c in contatos if termo_busca in c['nome'].lower()]

    if not encontrados:
        print(f"\nNenhum contato encontrado com o termo '{termo_busca}'.")
    else:
        print(f"\n--- Contatos Encontrados ({len(encontrados)}) ---")
        listar_contatos(encontrados)

def remover_contato(contatos):
    """Remove um contato da lista."""
    print("\n--- Remover Contato ---")
    termo_busca = input("Digite o nome exato do contato a ser removido: ").strip()

    contato_para_remover = None
    for contato in contatos:
        if contato['nome'].lower() == termo_busca.lower():
            contato_para_remover = contato
            break
    
    if contato_para_remover:
        contatos.remove(contato_para_remover)
        salvar_contatos(contatos)
        print(f"\n[SUCESSO] Contato '{contato_para_remover['nome']}' removido!")
    else:
        print(f"\n[ERRO] Contato com o nome '{termo_busca}' não encontrado.")
    
    return contatos

def exibir_menu():
    """Mostra o menu principal de opções para o usuário."""
    print("\n===== Agenda de Contatos =====")
    print("1. Adicionar Contato")
    print("2. Listar Todos os Contatos")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("5. Sair")
    print("==============================")

def main():
    """Função principal que executa o loop do programa."""
    contatos = carregar_contatos()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            contatos = adicionar_contato(contatos)
        elif escolha == '2':
            listar_contatos(contatos)
        elif escolha == '3':
            buscar_contato(contatos)
        elif escolha == '4':
            contatos = remover_contato(contatos)
        elif escolha == '5':
            print("\nSaindo da agenda... Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Por favor, tente novamente.")
        
        # Pausa para o usuário poder ler a saída antes de o menu reaparecer
        time.sleep(1.5)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()