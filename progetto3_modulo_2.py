# Parte 1 - Pulizia dati

import numpy as np
import pandas as pd

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
