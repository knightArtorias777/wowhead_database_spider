import pandas as pd
from io import StringIO

from spider import bis_url_spider
"""
数据处理 从list到最后的输出
"""

def process_list(equid_table:list):
    data_list = equid_table[2]
    data_io = StringIO(data_list)
    df = pd.read_csv(data_io, sep='\t')
    print(df)
    df.to_html('output_table.html')


if __name__ == '__main__':
    test_url='https://www.wowhead.com/cn/guide/classes/Death-Knight/Unholy/bis-gear#bis-items-raid'
    tb = bis_url_spider(test_url)
    process_list(tb)