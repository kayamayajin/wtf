import pandas as pd
import numpy as np
from jqdatasdk import *
auth('15566918488','Shuiguo123')

####导入原始表格
df = pd.read_excel('/Users/kayamayajin/Desktop/draft.xlsx',converters = {u'code':str,u'Code':str,u'name':str,u'date':str})


#设置相关参数

##时间参数

today = '2020-08-25'

##需求参数
q_HT1 = 200
q_HT2 = 0

r_1 = q_HT1/(q_HT1 + q_HT2)
r_2 = q_HT2/(q_HT1 + q_HT2)


####得到需要的数据

for i in df.index:
    if int(df['code'].at[i]) > 599999:
        df['Code'].at[i] = df['code'].at[i] + '.XSHG'
    else:
        df['Code'].at[i] = df['code'].at[i] + '.XSHE'
    
    df['name'].at[i] = get_security_info(df['Code'].at[i]).display_name
    df['price'].at[i] = get_price(df['Code'].at[i], start_date = today, end_date = today, fields = ['open']).iloc[0,0]
    df['HT1'].at[i] = 1000*int(r_1*10*df['money'].at[i]/df['price'].at[i])
    df['HT2'].at[i] = 1000*int(r_2*10*df['money'].at[i]/df['price'].at[i])
    df['date'].at[i] = today


###导出一个新表格
df.to_excel('/Users/kayamayajin/Desktop/output.xlsx')


print('搞定')











