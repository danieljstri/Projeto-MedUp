from utils import convert_to_float
import pandas as pd

possible_months = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", "total"]

class Data:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.df.columns = self.df.columns.str.lower()  # Convert columns to lowercase for consistency

    def getLucro(self, month="total"):
        """
        Get the profit of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the profit of all the year)
        """
        error_month(month)
        
        lucro_str = self.df.at[12, month] # the |profit| is in the last row
        lucro = convert_to_float(lucro_str)
        return lucro
    
    def getReceitas(self, month="total"):
        """
        Get the revenue of the dataset (parameters: month)
        
        :month: get the revenue of the month selected. the standard is "total" (the revenue of all the year)
        """
        error_month(month)
        
        receita_str = self.df.at[0, month]
        receita = convert_to_float(receita_str)
        return receita

    def getReceitaExames(self, month="total"):
        """
        Get the exams revenue of the dataset (parameters: month)

        :month: get the revenue of the month selected. the standard is "total" (the exams revenue of all the year)
        """
        error_month(month)
        
        receita_exames_str = self.df.at[2, month]
        receita_exames = convert_to_float(receita_exames_str)
        return receita_exames
    
    def getReceitaAnestesia(self, month="total"):
        """
        Get the anesthesia revenue of the dataset (parameters: month)

        :month: get the revenue of the month selected. the standard is "total" (the anesthesia revenue of all the year)
        """
        error_month(month)
        
        receita_anestesia_str = self.df.at[3, month]
        receita_anestesia = convert_to_float(receita_anestesia_str)
        return receita_anestesia

    def getReceitaDinheiro(self, month="total"):
        """ 
        Get the cash revenue of the dataset (parameters: month)

        :month: get the revenue of the month selected. the standard is "total" (the cash revenue of all the year)
        """
        error_month(month)
        
        receita_dinheiro_str = self.df.at[4, month]
        receita_dinheiro = convert_to_float(receita_dinheiro_str)
        return receita_dinheiro
    

    def getDespesas(self, month="total"):
        """
        Get the expenses of the dataset (parameters: month)
        
        :month: get the expenses of the month selected. the standard is "total" (the expenses of all the year)
        """
        error_month(month)
        
        despesa_str = self.df.at[5, month]  # row 5 is DESPESAS TOTAIS
        despesa = convert_to_float(despesa_str)
        return despesa

    
    def getDespesaAluguel(self, month="total"):
        """
        Get the rent expenses of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the rent expenses of all the year)
        """
        error_month(month)
        
        despesa_aluguel_str = self.df.at[8, month]
        despesa_aluguel = convert_to_float(despesa_aluguel_str)
        return despesa_aluguel

    def getDespesaAnestesia(self, month="total"):
        """
        Get the anesthesia expenses of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the anesthesia expenses of all the year)
        """
        error_month(month)
        
        despesa_anestesia_str = self.df.at[7, month]
        despesa_anestesia = convert_to_float(despesa_anestesia_str)
        return despesa_anestesia

    def getAllData(self):
        """
        Get all data from the dataset
        """
        data = self.df.to_dict(orient='records')
        return data


def error_month(month):
    if month not in possible_months:
        raise ValueError(f"Month '{month}' is not valid. Choose from {possible_months}.")