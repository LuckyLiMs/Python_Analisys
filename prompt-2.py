import pandas as pd
import matplotlib.pyplot as plt

# Dados dos insumos
dados_insumos = {
	'nome': [
    	'Pão Brioche', 'Carne Bovina 150g', 'Bacon', 'Cebola', 'Batata Congelada',
    	'Alface', 'Tomate', 'Queijo Cheddar', 'Presunto', 'Ovo'
	],
	'categoria': [
    	'Padaria', 'Carne', 'Embutidos', 'Hortifruti', 'Congelados',
    	'Hortifruti', 'Hortifruti', 'Laticínios', 'Embutidos', 'Granja'
	],
	'medida': [
    	'un', 'kg', 'kg', 'kg', 'kg',
    	'kg', 'kg', 'kg', 'kg', 'un'
	],
	'estoque': [
    	40, 25, 10, 60, 20,
    	30, 18, 12, 9, 60
	],
	'estoque_minimo': [
    	50, 30, 15, 40, 25,
    	20, 25, 15, 10, 50
	],
	'preco_custo': [
    	0.60, 28.00, 22.00, 4.00, 12.00,
    	3.00, 5.00, 18.00, 19.00, 0.50
	],
	'custo_kg_l': [
    	10.00, 28.00, 22.00, 4.00, 12.00,
    	3.00, 5.00, 18.00, 19.00, 12.00
	]
}

# Criando o DataFrame
df = pd.DataFrame(dados_insumos)

# Custo total em estoque por insumo (estoque * custo por kg/l)
df['custo_total_estoque'] = df['estoque'] * df['custo_kg_l']

# Insumos em situação crítica (estoque < estoque_minimo)
df['critico'] = df['estoque'] < df['estoque_minimo']
insumos_criticos = df[df['critico'] == True]

# Percentual de insumos críticos
percentual_criticos = (len(insumos_criticos) / len(df)) * 100

# Custo total dos insumos críticos
custo_total_criticos = insumos_criticos['custo_total_estoque'].sum()

# Agrupamento por categoria dos insumos críticos
categorias_criticas = insumos_criticos['categoria'].value_counts()

# Top 5 insumos mais caros em valor total de estoque
top_5_caros = df.nlargest(5, 'custo_total_estoque')

# ---------- Resultados no console ----------
print("Insumos em estoque crítico:")
print(insumos_criticos[['nome', 'estoque', 'estoque_minimo']])

print("\nPercentual de insumos em situação crítica: {:.2f}%".format(percentual_criticos))

print("\nCategorias mais afetadas por estoque crítico:")
print(categorias_criticas)

print("\nCusto total dos insumos abaixo do mínimo: R${:.2f}".format(custo_total_criticos))

print("\nTop 5 insumos mais caros (valor total em estoque):")
print(top_5_caros[['nome', 'custo_total_estoque']])

# ---------- Gráficos ----------

# Gráfico de barras – Custo total em estoque por insumo
plt.figure(figsize=(10,6))
plt.bar(df['nome'], df['custo_total_estoque'], color='orange')
plt.xticks(rotation=45, ha='right')
plt.title('Custo Total em Estoque por Insumo')
plt.ylabel('Custo Total (R$)')
plt.tight_layout()
plt.show()

# Gráfico de barras – Apenas insumos críticos
plt.figure(figsize=(10,6))
plt.bar(insumos_criticos['nome'], insumos_criticos['custo_total_estoque'], color='red')
plt.xticks(rotation=45, ha='right')
plt.title('Custo Total de Insumos em Estoque Crítico')
plt.ylabel('Custo Total (R$)')
plt.tight_layout()
plt.show() 