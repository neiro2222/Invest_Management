import requests
import datetime
import pathlib
import apimoex
import pandas as pd

board = 'TQBR'

with open("C:/Users/rdsj8/PycharmProjects/Invest_Management/tokens.txt", "r") as TICKs:
    TICKs = [line.rstrip() for line in TICKs]
pathlib.Path("C:/Users/rdsj8/PycharmProjects/Invest_Management/Database/{}".format(board)).mkdir(parents=True, exist_ok=True)
process = 0
with requests.Session() as session:
    for TICK in TICKs:
         process = process + 1
         print((process / len(TICKs)) * 100, ' %')
         data = apimoex.get_board_history(session, TICK, board=board)
         if data == []:
             continue
         df = pd.DataFrame(data)
         df = df[['TRADEDATE','CLOSE']]
         df.to_excel("C:/Users/rdsj8/PycharmProjects/Invest_Management/Database/{}/{}.xlsx".format(board,TICK), index=False)