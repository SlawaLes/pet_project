import pandas as pd
dt = pd.read_excel("C:/Users/user/Desktop/pack/mm.xlsx")

dt['money_num'] = dt['Money']

if __name__=='__main__':
    print(dt.head(4))