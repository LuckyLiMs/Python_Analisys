import pandas as pd
import matplotlib.pyplot as plt

# Dados dos produtos
dados = {
    'nome': ['X-Burguer', 'X-Salada', 'X-Bacon', 'Coca-Cola 350ml', 'Coca-Cola 600ml',
             'Batata Média', 'Batata Grande', 'X-Egg', 'X-Tudo', 'Guaraná Lata'],
    'status': ['ativo', 'ativo', 'inativo', 'ativo', 'inativo',
               'ativo', 'ativo', 'ativo', 'ativo', 'ativo'],
    'categoria': ['Lanche', 'Lanche', 'Lanche', 'Bebida', 'Bebida',
                  'Acompanhamento', 'Acompanhamento', 'Lanche', 'Lanche', 'Bebida'],
    'medida': ['un', 'un', 'un', 'lata', 'garrafa',
               'porção', 'porção', 'un', 'un', 'lata'],
    'preco_custo': [6.50, 7.00, 8.00, 3.00, 4.00, 4.00, 5.00, 7.50, 9.00, 2.80],
    'preco_venda': [14.00, 15.50, 16.00, 6.50, 8.00, 10.00, 12.00, 15.00, 18.00, 6.00]
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Cálculos de lucro unitário e margem de lucro (%)
df['lucro_unitario'] = df['preco_venda'] - df['preco_custo']
df['margem_lucro_perc'] = (df['lucro_unitario'] / df['preco_venda']) * 100

# Produto mais e menos lucrativo
produto_mais_lucrativo = df.loc[df['lucro_unitario'].idxmax()]
produto_menos_lucrativo = df.loc[df['lucro_unitario'].idxmin()]

# Quantidade e percentual de produtos ativos e inativos
status_counts = df['status'].value_counts()
status_percent = (status_counts / len(df)) * 100

# Contagem de produtos por categoria
categoria_counts = df['categoria'].value_counts()

# Média de lucro por categoria
media_lucro_categoria = df.groupby('categoria')['lucro_unitario'].mean()

# Exibindo resultados
print("Produto mais lucrativo:")
print(produto_mais_lucrativo[['nome', 'lucro_unitario', 'margem_lucro_perc']])
print("\nProduto menos lucrativo:")
print(produto_menos_lucrativo[['nome', 'lucro_unitario', 'margem_lucro_perc']])
print("\nQuantidade de produtos por status:")
print(status_counts)
print("\nPercentual de produtos por status:")
print(status_percent.round(2))
print("\nNúmero de produtos por categoria:")
print(categoria_counts)
print("\nMédia do lucro unitário por categoria:")
print(media_lucro_categoria.round(2))

# Gráfico de barras: lucro unitário por produto
plt.figure(figsize=(10,6))
plt.bar(df['nome'], df['lucro_unitario'], color='skyblue')
plt.title('Lucro Unitário por Produto')
plt.ylabel('Lucro Unitário (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de pizza: proporção de produtos ativos vs inativos
plt.figure(figsize=(6,6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Proporção de Produtos Ativos e Inativos')
plt.show()
