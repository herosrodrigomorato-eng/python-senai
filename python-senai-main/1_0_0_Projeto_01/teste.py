
AEROPORTOS = {
    "1": ("Congonhas-SP", 102),
    "2": ("Guarulhos-SP", 112),
    "3": ("Campo de Marte-SP", 98),
    "4": ("Pinto Martins-CE", 2922),
    "5": ("Eduardo Gomes-AM", 6294),
}


def calcular(destino_id, embalagem, y, x, z, w, itens=1):
    if destino_id not in AEROPORTOS:
        raise ValueError("Destino inválido.")

    if embalagem not in ("1", "2"):
        raise ValueError("Embalagem inválida.")

    if y <= 0 or x <= 0 or z <= 0:
        raise ValueError("As dimensões devem ser maiores que zero.")

    if w <= 0:
        raise ValueError("O peso deve ser maior que zero.")

    if itens <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    nome, dist = AEROPORTOS[destino_id]

    f = 0.26 if embalagem == "1" else 0.37

    custo_unit = ((y * x * z * w) * (1 + f)) * (1 + (dist * 9.8))

    return nome, dist, custo_unit * itens


def executar():
    print("\n--- COTAÇÃO DE FRETE (Origem: Viracopos) ---")

    for k, (nome, dist) in AEROPORTOS.items():
        print(f"[{k}] {nome} ({dist} KM)")

    dest = input("Destino (0 para sair): ").strip()

    if dest == "0":
        return

    if dest not in AEROPORTOS:
        return print("Destino inválido.")

    emb = input("Embalagem [1] Caixa (m) | [2] Container (cm): ").strip()

    if emb not in ("1", "2"):
        return print("Embalagem inválida.")

    try:
        un = "m" if emb == "1" else "cm"

        y = float(input(f"Altura ({un}): ").replace(",", "."))
        x = float(input(f"Largura ({un}): ").replace(",", "."))
        z = float(input(f"Profundidade ({un}): ").replace(",", "."))
        w = float(input("Peso (kg): ").replace(",", "."))

        itens = int(input("Total de itens: "))

        nome, dist, total = calcular(dest, emb, y, x, z, w, itens)

        print(f"\nDestino: {nome} ({dist} KM) | Total: R$ {total:,.2f}\n")

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    executar()
