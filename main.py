# main.py

from fastapi import FastAPI
import pandas as pd
from openpyxl import Workbook
import csv

labelRepoFile = 'Label_Repo.xlsx'
df3 = pd.read_excel(labelRepoFile, sheet_name='Processing')

myDict = df3.to_dict('records')



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/rei/")
async def rei(regnum: str, dateval: str):
    rei = [x['REI'] for x in myDict if x['EPA Reg. No.'] == regnum and x['Label Date'] == dateval]
    return {"REI": rei}

@app.get("/ppe/")
async def rei(regnum: str, dateval: str):
    ppe = [x['PPE'] for x in myDict if x['EPA Reg. No.'] == regnum and x['Label Date'] == dateval]
    return {"PPE": ppe}
