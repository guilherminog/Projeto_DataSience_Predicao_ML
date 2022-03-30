import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd


class Template2022:
    nome_folha = "CONSUMOS"

    skiprows: int
    nome_arquivo: str
    df: pd.DataFrame

    colunas = {
        'Data': 'data',
        'Volume Etanol 3,5° (m³)': 'volume_etanol_3.5g_m3',
        'Volume Etanol 0° (m³)': 'volume_etanol_0g_m3',
        'Volume Frio (Diário)': 'volume_frio_diario',
        'Volume Frio (Acumulado)': 'volume_frio_acumulado',
        'Frio 1 (KWh)': 'frio_1_kwh',
        'Frio 2 (KWh)': 'frio_2_kwh',
        'Total Frio (Diário)': 'total_frio_diario',
        'Total Frio (Acumulado)': 'total_frio_acumulado',
        'CO2 1 (KWh)': 'co2_1_kwh',
        'CO2 2 (KWh)': 'co2_2_kwh',
        'ACM CO2 1': 'acm_co2_1',
        'ACM CO2 2': 'acm_co2_2',
        'Total CO2 (Acumulado)': 'total_co2_acumulado',
        'Volume Ar (Diário)': 'volume_ar_diario',
        'Volume Ar (Acumulado)': 'volume_ar_acumulado',
        'AR 1 (KWh)': 'ar_1_kwh',
        'AR2 2 (KWh)': 'ar_2_kwh',
        'Total CO2 (Diário)': 'total_co2_diario_ar',
        'Total CO2 (Acumulado)6': 'total_co2_acumulado_ar',
        'Total Torres (Diário)': 'total_torres_diario',
        'Total Torres (Acumulado)': 'total_torres_acumulado',
        'Total Caldeira (Diário)': 'total_caldeira_diario',
        'Total Caldeira (Acumulado)': 'total_caldeira_acumulado',
        'Consumo Utilidades Diário': 'consumo_utilidades_diario',
        'Consumo Utilidades Acumulado': 'consumo_utilidades_acumulado',
    }

    def __init__(self, nome_arquivo: str, tipo_planilha: str='xlsx', linha_inicio: int = 1):
        self.nome_arquivo = f"{nome_arquivo}.{tipo_planilha}"
        self.skiprows = linha_inicio - 1
        self.carrega_df()
        self.prepara_templates_antigos()
        self.filtra_colunas_e_linhas()
        self.renomeia_colunas()
        print(self.nome_arquivo, "shape", self.df.shape)

    def prepara_templates_antigos(self):
        pass

    def carrega_df(self):
        caminho_do_arquivo = f"data/{self.nome_arquivo}"
        self.df = pd.read_excel(caminho_do_arquivo, self.nome_folha, skiprows=self.skiprows)

    def filtra_colunas_e_linhas(self):
        #from ipdb import set_trace; set_trace()
        self.df = self.df[self.colunas.keys()].dropna(0)

    def renomeia_colunas(self):
        self.df = self.df.rename(columns=self.colunas)


class Template2020v2(Template2022):

    def prepara_templates_antigos(self):
        aux = self.colunas.copy()
        if 'Data.1' in self.df.columns:
            aux['Data.1'] = aux.pop('Data')
        else:
            aux['Data2'] = aux.pop('Data')

        if 'Total CO2 (Acumulado).1' in self.df.columns:
            aux['Total CO2 (Acumulado).1'] = aux.pop('Total CO2 (Acumulado)6')

        self.colunas = aux

class Template2020v1(Template2022):

    def prepara_templates_antigos(self):
        aux = self.colunas.copy()
        aux['Unnamed: 2'] = aux.pop('Data')
        aux['Unnamed: 51'] = aux.pop('Consumo Utilidades Diário')
        aux['Unnamed: 52'] = aux.pop('Consumo Utilidades Acumulado')
        aux['Total CO2 (Acumulado).1'] = aux.pop('Total CO2 (Acumulado)6')

        self.df['ACM CO2 1'] = self.df['CO2 1 (KWh)'].cumsum()
        self.df['ACM CO2 2'] = self.df['CO2 2 (KWh)'].cumsum()

        self.colunas = aux



class Template2019v1(Template2020v1):

    def prepara_templates_antigos(self):
        super().prepara_templates_antigos()

        aux = self.colunas.copy()
        aux['Volume Etanol 3,5°'] = aux.pop('Volume Etanol 3,5° (m³)')
        aux['Volume Etanol 0°'] = aux.pop('Volume Etanol 0° (m³)')
        self.colunas = aux

class Template2019v2(Template2019v1):

    def prepara_templates_antigos(self):
        super().prepara_templates_antigos()

        # from ipdb import set_trace; set_trace()

        aux = self.colunas.copy()
        aux['Total CO2 (Diário).2'] = aux.pop('Total Torres (Diário)')
        aux['Total CO2 (Acumulado).2'] = aux.pop('Total Torres (Acumulado)')
        self.colunas = aux
