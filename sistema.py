
def precoTotal(quantidade, preco):
    total = quantidade * preco
    desconto = 0

    if total >= 100:
        desconto = total * 0.10

    return total - desconto;

nome_produto=input("Digite o nome do produto: ");

quantidade = int(input("Digite a quantidade desejada do produto: "));

preco_produto=int(input("Digite o preço do produto: "));


print(precoTotal(quantidade, preco_produto));





