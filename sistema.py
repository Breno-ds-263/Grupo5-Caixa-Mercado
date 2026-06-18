def precoTotal(quantidade, preco):
    total = quantidade * preco
    desconto = 0

    if total > 100:
        desconto = total * 0.10

    return total - desconto;

