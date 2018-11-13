import csv
import sys
from decimal import *

maxInt = sys.maxsize
decrement = True
while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

clast_dict = {}
trans_dict = {}
with open('address_clust.csv', 'r', encoding='utf-8') as f1, open('address_stats.csv', 'r', encoding='utf-8') as f2:
    i = 0
    for row in csv.reader(f1, delimiter=","):
        if i != 0:
            clast_dict[row[0]] = row[1]
        i += 1
    i = 0
    for row in csv.reader(f2, delimiter=","):
        if i != 0:
            if row[2] in trans_dict:
                trans_dict[row[2]][row[1]] = {'received': Decimal(row[3]), 'sent': Decimal(row[4])}
            else:
                trans_dict[row[2]] = {}
                trans_dict[row[2]][row[1]] = {'received': Decimal(row[3]), 'sent': Decimal(row[4])}
        i += 1
clast_2_1_info = [Decimal(0), Decimal(0), Decimal(0)]
clast_2_0_info = [Decimal(0), Decimal(0), Decimal(0)]
clast_1_0_info = [Decimal(0), Decimal(0), Decimal(0)]
for it in trans_dict:
    print(trans_dict[it])
    trans_in = Decimal(0)
    trans_out = Decimal(0)
    clas_0 = False
    clas_1 = False
    clas_2 = False
    clast_0_temp_inf = [Decimal(0), Decimal(0)]
    clast_1_temp_inf = [Decimal(0), Decimal(0)]
    clast_2_temp_inf = [Decimal(0), Decimal(0)]
    for it_i in trans_dict[it]:
        if it_i in clast_dict:
            if clast_dict[it_i] == '1':
                clas_1 = True
                clast_1_temp_inf[0] += trans_dict[it][it_i]['received']
                clast_1_temp_inf[1] += trans_dict[it][it_i]['sent']
            elif clast_dict[it_i] == '2':
                clas_2 = True
                clast_2_temp_inf[0] += trans_dict[it][it_i]['received']
                clast_2_temp_inf[1] += trans_dict[it][it_i]['sent']
        else:
            clas_0 = True
            clast_0_temp_inf[0] += trans_dict[it][it_i]['received']
            clast_0_temp_inf[1] += trans_dict[it][it_i]['sent']
        trans_in += trans_dict[it][it_i]['received']
        trans_out += trans_dict[it][it_i]['sent']
    print(clas_0, clas_1, clas_2)
    print(trans_out - trans_in)
    if (clas_2 and clas_1 and (not clas_0)) or ((clas_2 or clas_1) and (not clas_0)):
        clast_2_1_info[0] += clast_2_temp_inf[1]
        clast_2_1_info[1] += clast_1_temp_inf[1]
        clast_2_1_info[2] += abs(trans_in - trans_out)
    elif (clas_2 and clas_0 and (not clas_1)) or ((clas_2 or clas_0) and (not clas_1)):
        clast_2_0_info[0] += clast_2_temp_inf[1]
        clast_2_0_info[1] += clast_0_temp_inf[1]
        clast_2_0_info[2] += abs(trans_in - trans_out)
    elif (clas_1 and clas_0 and (not clas_2)) or ((clas_1 or clas_0) and (not clas_2)):
        clast_1_0_info[0] += clast_1_temp_inf[1]
        clast_1_0_info[1] += clast_0_temp_inf[1]
        clast_1_0_info[2] += abs(trans_in - trans_out)
print([x / Decimal(100000000) for x in clast_2_1_info])
print([x / Decimal(100000000) for x in clast_2_0_info])
print([x / Decimal(100000000) for x in clast_1_0_info])

