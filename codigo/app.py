import os
os.system("cls")  # Limpa a tela do terminal para começar com o visual limpo

# Cardápio de comidas: número -> (nome do prato, preço)
comidas = {
    1: ("X-Burger", 22.00),
    2: ("X-Salada", 24.00),
    3: ("X-Bacon", 27.50),
    4: ("Pizza Calabresa", 38.00),
    5: ("Pizza Margherita", 36.00),
    6: ("Pizza Portuguesa", 42.00),
    7: ("Batata Frita Grande", 18.00),
    8: ("Yakisoba", 34.00),
    9: ("Marmita de Frango", 25.00),
    10: ("Marmita de Carne", 28.00),
    11: ("Porção de Nuggets", 19.00),
    12: ("Hot Dog Completo", 17.50),
}

# Cardápio de bebidas: número -> (nome da bebida, preço)
bebidas = {
    1: ("Refrigerante Lata", 6.00),
    2: ("Refrigerante 2L", 13.00),
    3: ("Água Mineral sem Gás", 4.00),
    4: ("Suco Natural de Laranja", 9.00),
    5: ("Cerveja Lata", 8.50),
    6: ("Chopp Copo 400ml", 12.00),
}

# Cardápio de sobremesas (8 opções): número -> (nome da sobremesa, preço)
sobremesas = {
    1: ("Pudim de Leite Condensado", 12.00),
    2: ("Brownie com Sorvete", 18.00),
    3: ("Petit Gâteau", 21.00),
    4: ("Mousse de Chocolate", 11.00),
    5: ("Torta Holandesa", 15.00),
    6: ("Açaí na Tigela 400ml", 17.00),
    7: ("Brigadeiro de Colher", 10.00),
    8: ("Cheesecake de Morango", 16.50),
}

# IMPORTANTE: Combos com desconto calculado sobre a soma dos itens originais.
# Estrutura: número -> (nome, itens_inclusos, preco_original, preco_com_desconto, desconto_pct)
combos = {
    1: (
        "Combo Burger Bacon",
        "X-Bacon + Batata Frita Grande + Refrigerante Lata",
        51.50,
        round(51.50 * 0.85, 2),  # 15% de desconto (paga 85% do valor original)
        15,
    ),
    2: (
        "Combo Pizza & Pudim",
        "Pizza Calabresa + Refrigerante 2L + Pudim de Leite Condensado",
        63.00,
        round(63.00 * 0.82, 2),  # 18% de desconto
        18,
    ),
    3: (
        "Combo Galera",
        "2x X-Salada + Porção de Nuggets + 2x Refrigerante Lata",
        79.00,
        round(79.00 * 0.80, 2),  # 20% de desconto
        20,
    ),
    4: (
        "Combo Oriental Doce",
        "Yakisoba + Suco Natural de Laranja + Mousse de Chocolate",
        54.00,
        round(54.00 * 0.85, 2),  # 15% de desconto
        15,
    ),
}

taxa_entrega = 6.00     # Taxa fixa cobrada quando há pelo menos 1 item no pedido
carrinho = []           # IMPORTANTE: Lista que guarda cada item adicionado como [tipo, nome, qtd, preco, valor]
total_comidas = 0.0     # Soma de comidas e combos
total_bebidas = 0.0     # Soma das bebidas
total_sobremesas = 0.0  # Soma das sobremesas

# --- LOGIN SIMPLES ---
# IMPORTANTE: Loop de validação garante que o nome não fique vazio e tenha só letras.
while True:
    nome_usuario = input("Oi! Como posso te chamar? (só letras): ").strip()
    nome_sem_espaco = nome_usuario.replace(" ", "")  # Remove espaços só para checar .isalpha()

    if nome_sem_espaco == "":
        print("Ei, me diz seu nome primeiro pra gente começar 😊")
    elif not nome_sem_espaco.isalpha():
        print("Hmm, use só letras no nome, tá bom? Nada de números ou símbolos.")
    else:
        break

print(f"\nTudo certo, {nome_usuario}! Fica à vontade pra montar seu pedido.")

# --- MENU PRINCIPAL ---
while True:
    print("\n[1] Comidas  [2] Bebidas  [3] Sobremesas  [4] Combos  [5] Carrinho  [6] Finalizar  [cls] Desfazer  [0] Sair")
    opcao = input("> ").strip().lower()

    # IMPORTANTE: 'cls' desfaz o último item colocado no carrinho e estorna o valor do total correspondente.
    if opcao == "cls":
        if len(carrinho) == 0:
            print("Ainda não tem nada no carrinho pra desfazer.")
        else:
            ultimo = carrinho.pop()  # Remove e retorna o último elemento adicionado
            tipo, nome, qtd, preco, valor = ultimo
            if tipo in ("comida", "combo"):
                total_comidas -= valor
            elif tipo == "bebida":
                total_bebidas -= valor
            elif tipo == "sobremesa":
                total_sobremesas -= valor
            print(f"Beleza, tirei {qtd}x {nome} do seu pedido.")
        continue

    # --- OPÇÃO 1: COMIDAS ---
    if opcao == "1":
        print(f"\n--- COMIDAS ({nome_usuario}) ---")
        for codigo in comidas:
            nome, preco = comidas[codigo]
            print(f"{codigo}. {nome} - R$ {preco:.2f}")

        escolha = input("Qual vai ser hoje? (número ou 'v' pra voltar): ").strip().lower()
        if escolha == "v":
            continue

        # IMPORTANTE: Valida se a escolha é um número existente no dicionário e se a quantidade é > 0.
        if escolha.isdigit() and int(escolha) in comidas:
            codigo = int(escolha)
            qtd_txt = input("Quantas unidades você quer? ").strip()

            if qtd_txt.isdigit() and int(qtd_txt) > 0:
                qtd = int(qtd_txt)
                nome, preco = comidas[codigo]
                valor = preco * qtd
                total_comidas += valor
                carrinho.append(["comida", nome, qtd, preco, valor])
                print(f"Fechado! Adicionei {qtd}x {nome} (R$ {valor:.2f}).")
            else:
                print("Coloca um número maior que zero na quantidade, por favor.")
        else:
            print("Não achei esse número nas comidas. Tenta escolher outro.")

    # --- OPÇÃO 2: BEBIDAS ---
    elif opcao == "2":
        print(f"\n--- BEBIDAS ({nome_usuario}) ---")
        for codigo in bebidas:
            nome, preco = bebidas[codigo]
            print(f"{codigo}. {nome} - R$ {preco:.2f}")

        escolha = input("Vai querer qual bebida? (número ou 'v' pra voltar): ").strip().lower()
        if escolha == "v":
            continue

        if escolha.isdigit() and int(escolha) in bebidas:
            codigo = int(escolha)
            qtd_txt = input("Quantas unidades? ").strip()

            if qtd_txt.isdigit() and int(qtd_txt) > 0:
                qtd = int(qtd_txt)
                nome, preco = bebidas[codigo]
                valor = preco * qtd
                total_bebidas += valor
                carrinho.append(["bebida", nome, qtd, preco, valor])
                print(f"Anotado! +{qtd}x {nome} (R$ {valor:.2f}).")
            else:
                print("Digite um número maior que zero pra quantidade.")
        else:
            print("Essa opção não tá na lista de bebidas.")

    # --- OPÇÃO 3: SOBREMESAS ---
    elif opcao == "3":
        print(f"\n--- SOBREMESAS ({nome_usuario}) ---")
        for codigo in sobremesas:
            nome, preco = sobremesas[codigo]
            print(f"{codigo}. {nome} - R$ {preco:.2f}")

        escolha = input("Qual sobremesa deu vontade? (número ou 'v' pra voltar): ").strip().lower()
        if escolha == "v":
            continue

        if escolha.isdigit() and int(escolha) in sobremesas:
            codigo = int(escolha)
            qtd_txt = input("Quantas você quer? ").strip()

            if qtd_txt.isdigit() and int(qtd_txt) > 0:
                qtd = int(qtd_txt)
                nome, preco = sobremesas[codigo]
                valor = preco * qtd
                total_sobremesas += valor
                carrinho.append(["sobremesa", nome, qtd, preco, valor])
                print(f"Boa escolha! +{qtd}x {nome} (R$ {valor:.2f}).")
            else:
                print("Por favor, digite um número maior que zero.")
        else:
            print("Não encontrei essa sobremesa no cardápio.")

    # --- OPÇÃO 4: COMBOS COM DESCONTO ---
    elif opcao == "4":
        print(f"\n--- COMBOS COM DESCONTO ({nome_usuario}) ---")
        for codigo in combos:
            nome, desc, preco_orig, preco_combo, desc_pct = combos[codigo]
            economia = preco_orig - preco_combo
            print(
                f"{codigo}. {nome} ({desc_pct}% OFF) — R$ {preco_combo:.2f} "
                f"[de R$ {preco_orig:.2f} | você economiza R$ {economia:.2f}]\n"
                f"    Vem com: {desc}"
            )

        escolha = input("Qual combo você manda ver? (número ou 'v' pra voltar): ").strip().lower()
        if escolha == "v":
            continue

        if escolha.isdigit() and int(escolha) in combos:
            codigo = int(escolha)
            qtd_txt = input("Quantos combos? ").strip()

            if qtd_txt.isdigit() and int(qtd_txt) > 0:
                qtd = int(qtd_txt)
                nome, _, _, preco_combo, _ = combos[codigo]
                valor = preco_combo * qtd
                total_comidas += valor
                carrinho.append(["combo", nome, qtd, preco_combo, valor])
                print(f"Show! Adicionei {qtd}x {nome} (R$ {valor:.2f}).")
            else:
                print("Digite um número maior que zero pra quantidade de combos.")
        else:
            print("Esse combo não existe por aqui.")

    # --- OPÇÃO 5: CARRINHO ---
    # IMPORTANTE: Só soma a taxa de entrega ao total geral se houver itens (subtotal > 0).
    elif opcao == "5":
        print(f"\n--- SEU CARRINHO, {nome_usuario} ---")
        if len(carrinho) == 0:
            print("Tá vazio por enquanto. Escolha algo no cardápio!")
        else:
            for item in carrinho:
                tipo, nome, qtd, preco, valor = item
                print(f"{qtd}x {nome} (R$ {preco:.2f} cada) = R$ {valor:.2f}")

        subtotal = total_comidas + total_bebidas + total_sobremesas
        total_geral = subtotal + taxa_entrega if subtotal > 0 else 0.0

        print(
            f"Comidas/Combos: R$ {total_comidas:.2f} | Bebidas: R$ {total_bebidas:.2f} | "
            f"Sobremesas: R$ {total_sobremesas:.2f} | Entrega: R$ {taxa_entrega:.2f}"
        )
        print(f"Total até agora: R$ {total_geral:.2f}")

    # --- OPÇÃO 6: FINALIZAR ---
    # IMPORTANTE: Exige carrinho preenchido e endereço não vazio antes de gerar o resumo final.
    elif opcao == "6":
        if len(carrinho) == 0:
            print("Antes de fechar, coloque pelo menos um item no carrinho 😉")
            continue

        while True:
            endereco = input("Me passa seu endereço completo pra entrega: ").strip()
            if endereco != "":
                break
            print("Preciso do endereço certinho pra conseguir te entregar.")

        subtotal = total_comidas + total_bebidas + total_sobremesas
        total_final = subtotal + taxa_entrega

        print("\n=== PEDIDO CONFIRMADO ===")
        print(f"Cliente:          {nome_usuario}")
        print(f"Endereço:         {endereco}")
        for item in carrinho:
            tipo, nome, qtd, preco, valor = item
            print(f"- {qtd}x {nome} (R$ {preco:.2f} cada) -> R$ {valor:.2f}")
        print(f"Total comidas/combos: R$ {total_comidas:.2f}")
        print(f"Total bebidas:        R$ {total_bebidas:.2f}")
        print(f"Total sobremesas:     R$ {total_sobremesas:.2f}")
        print(f"Taxa entrega:         R$ {taxa_entrega:.2f}")
        print(f"TOTAL TUDO:           R$ {total_final:.2f}")
        print(f"Prontinho, {nome_usuario}! Já tá tudo encaminhado. Bom apetite!")
        break

    # --- OPÇÃO 0: SAIR ---
    elif opcao == "0":
        print(f"Tudo bem, {nome_usuario}! Quando bater a fome de novo, é só chamar.")
        break

    else:
        print("Não entendi essa opção. Escolha 1, 2, 3, 4, 5, 6, cls ou 0.")