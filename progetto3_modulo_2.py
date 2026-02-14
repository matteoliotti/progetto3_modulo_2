import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parte 1 - Pulizia dati

df = pd.DataFrame({
    "Order Date":['2025-09-30','2025-10-31','2025-11-30','2025-12-31','2026-01-31',
                  '2026-02-28','2026-03-31','2026-04-30','2026-05-31','2026-06-30'],
    "Ship Date":['2025-10-31','2025-11-30','2025-12-31','2026-01-31','2026-02-28',
                 '2026-03-31','2026-04-30','2026-05-31','2026-06-30','2026-07-31'],
    "Category":['Technology','Technology','Furniture','Technology','Office Supplies',
                'Furniture','Technology','Furniture','Office Supplies','Furniture'],
    "Sub-Category":['Smartphone','Tablet','Letto','Smartwatch','Carta','Armadio','Digital camera','Scrivania','Tastiera','Sofa'],
    "Sales":[1000, 800, np.nan, 200, 150, 1200, 300, 400, None, 600],
    "Profit":[200, 150, 100, None, 30, 250, 60, 80, 10, 120],
    "Region":['Nord','Sud','Nord','Sud','Centro','Nord','Sud','Centro','Nord','Sud'],
    "State":['Roma','Napoli','Milano','Torino','Firenze','Venezia','Bari','Bologna','Genova','Palermo'],
    "Quantity":[10, 8, 5, 2, 15, np.nan, 3, 4, 5, 6],
})

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df=df.fillna(0)
df.drop_duplicates()

df["Year"]=df['Order Date'].dt.year
df=df.set_index("Year")

print(df)

# Parte 2 - Analisi Esplorativa (EDA)

df_anno = df.groupby('Year')[['Sales', 'Profit']].sum()

fig, ax = plt.subplots(figsize=(10,6))
plt.subplots_adjust(bottom=0.25)

width = 0.35
x = np.arange(len(df_anno.index))
bar1 = ax.bar(x - width/2, df_anno['Sales'], width, label='Vendite')
bar2 = ax.bar(x + width/2, df_anno['Profit'], width, label='Profitto')
ax.set_xticks(x)
ax.set_xticklabels(df_anno.index)
ax.set_xlabel('Anno')
ax.set_ylabel('Valore')
ax.set_title('Vendite e Profitto per Anno')
ax.legend()

df_sotto_categorie=df.groupby("Sub-Category")["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).set_index("Quantity")

print(f"le 5 sotto-categorie più vendute:\n{df_sotto_categorie.head()}")

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Sotto-Categoria', 0, len(df_sotto_categorie) - 1, valinit=0, valstep=1)

def update(val):
    idx = int(slider.val)
    sotto_categoria = df_sotto_categorie.iloc[idx]['Sub-Category']
    df_filtra = df[df['Sub-Category'] == sotto_categoria]
    df_anno = df_filtra.groupby('Year')[['Sales', 'Profit']].sum()
    ax.clear()
    width = 0.35
    x = np.arange(len(df_anno.index))
    ax.bar(x - width/2, df_anno['Sales'], width, label='Vendite')
    ax.bar(x + width/2, df_anno['Profit'], width, label='Profitto')
    ax.set_xticks(x)
    ax.set_xticklabels(df_anno.index)
    ax.set_xlabel('Anno')
    ax.set_ylabel('Valore')
    ax.set_title(f'Vendite e Profitto per Anno - {sotto_categoria}')
    ax.legend()
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()