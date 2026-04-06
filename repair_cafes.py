import pandas as pd

#Data downloaded from https://dashboard.repairmonitor.org/?language=en
repair_raw = pd.read_excel("repairs-en.xlsx")

#select columns
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

#rename columns
repair_data = repair_data.rename(columns={
    'Repair date':'date',
    'Repair Cafe number':'cafe_no',
    'Repair Cafe name':'cafe_name',
    'Country':'country',
    'Kind of product':'product_kind',
    'Category':'category',
    'Brand':'brand',
    'Model, type number and/or serial number':'model',
    '(Estimated) Year of production':'production_year',
    'Has the product been repaired?':'repaired',
    'If not repaired: why could you not repair it (list)?':'failure_reason',
    'Reparability of product  (1 = difficult, 10 = easy)':'repairability',
    'Did you use repair information?':'repair_info'
    })

#set date to datetime format

repair_data['date'] = pd.to_datetime(repair_data['date'])
