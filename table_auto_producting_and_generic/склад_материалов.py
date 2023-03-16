import pandas as pd
from data import materials
from random import randint

def table_gen(LENGTH_OF_TABLE = 50):
    """This function is generating table in format dict().
    """
    table = dict()
    
    for i in materials:
        table[f'{i}'] = [randint(1, 20) for i in range(LENGTH_OF_TABLE)]

    return table

def main() -> int:

    excel_table = table_gen()

    df = pd.DataFrame(excel_table)

    df.to_excel("./Склад_1.xlsx")

    return 0

if __name__ == '__main__':
    main()
