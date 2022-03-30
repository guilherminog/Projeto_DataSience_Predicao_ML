from templates import *
from ipdb import set_trace
import pandas as pd

planilhas_meses = [

    # Template2019('18_jan', linha_inicio=6),
    # Template2019('18_fev', linha_inicio=6),
    # Template2019('18_mar', linha_inicio=6),
    # Template2019('18_abr', linha_inicio=6),
    # Template2019('18_mai', linha_inicio=6),
    # Template2019('18_jun', linha_inicio=6),
    # Template2019v2('18_jul', linha_inicio=6),
    # Template2019v2('18_ago', linha_inicio=6),
    # Template2019v2('18_set', linha_inicio=6),
    # Template2019v2('18_out', linha_inicio=6),
    Template2019v2('18_nov', linha_inicio=6),

    Template2019v1('18_dez', linha_inicio=6),

    Template2019v1('19_jan', linha_inicio=6),
    Template2019v1('19_fev', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_mar', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_abr', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_mai', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_jun', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_jul', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_ago', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_set', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_out', tipo_planilha='xlsm', linha_inicio=6),
    Template2019v1('19_nov', tipo_planilha='xlsm', linha_inicio=6),

    Template2020v1('19_dez', tipo_planilha='xlsm', linha_inicio=6),

    Template2020v1('20_jan', linha_inicio=6),
    Template2020v1('20_fev', linha_inicio=6),
    Template2020v1('20_mar', linha_inicio=6),
    Template2020v1('20_abr', linha_inicio=6),
    Template2020v1('20_mai', linha_inicio=6),

    Template2020v2('20_jun', linha_inicio=3),
    Template2020v2('20_jul', linha_inicio=5),
    Template2020v2('20_ago', linha_inicio=3),
    Template2020v2('20_set'),
    Template2020v2('20_out'),
    Template2020v2('20_nov'),
    Template2020v2('20_dez'),

    Template2022('21_jan'),
    Template2022('21_fev'),
    Template2022('21_mar'),
    Template2022('21_abr'),
    Template2022('21_mai'),
    Template2022('21_jun'),
    Template2022('21_jul'),
    Template2022('21_ago'),
    Template2022('21_set'),
    Template2022('21_out'),
    Template2022('21_nov'),
    Template2022('21_dez'),

    Template2022('22_jan'),
    Template2022('22_fev'),
    Template2022('22_mar'),
]

df_completo = pd.concat([x.df for x in planilhas_meses])
df_completo.reset_index(drop=True, inplace=True)

print("linhas 2022 -> ", df_completo[df_completo['data'].dt.year == 2022].shape[0])
print("linhas 2021 -> ", df_completo[df_completo['data'].dt.year == 2021].shape[0])
print("linhas 2020 -> ", df_completo[df_completo['data'].dt.year == 2020].shape[0])
print("linhas 2019 -> ", df_completo[df_completo['data'].dt.year == 2019].shape[0])
print("linhas 2018 -> ", df_completo[df_completo['data'].dt.year == 2018].shape[0])
print("linhas nan -> ", df_completo.isna().sum().sum())
print("shape ", df_completo.shape)


df_completo.to_excel("output_dados/output.xlsx", index=False)
df_completo.to_csv("output_dados/output.csv", index=False)