import pandas as pd

#Data downloaded from https://dashboard.repairmonitor.org/?language=en
repair_raw = pd.read_excel("repairs-en.xlsx")

#select rows
repair_data = repair_raw[[
    'Repair date',
    'Repair Cafe number',
    'Repair Cafe name',
    'Country',
    'Kind of product',
    'Category',
    'Brand',
    'Model, type number and/or serial number',
    '(Estimated) Year of production',
    'Has the product been repaired?',
    'If not repaired: why could you not repair it (list)?',
    'Reparability of product  (1 = difficult, 10 = easy)',
    'Did you use repair information?'
    ]]
