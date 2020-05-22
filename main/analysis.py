import pandas as pd
import webscrap

def find_recurrency(option, dataframe):

    df_nums = dataframe.iloc[:,2:8] # Selecionamos apenas as colunas que indicam os números sorteados

    ocurr = pd.Series([]) # Series que armazenará o total de ocorrências de cada número

    for (column, data) in df_nums.iteritems(): # Iteramos pelo data frame coluna a coluna
        temp = ( data.value_counts() ).sort_index() # Contamos as ocorrências de cada número na coluna
        ocurr = ocurr.add(temp,fill_value=0) # Somamos as ocorrências da coluna com as ocorrências das colunas anteriores

    tot = int(ocurr.sum()) # Soma de todas as ocorrências de cada número

    df_ocorr = pd.DataFrame([]) # Dataframe que guardará as informações de ocorrência de cada número

    df_ocorr['Número de Ocorrências'] = ocurr # Criamos a coluna das ocorrências

    percentage = lambda x: (x/tot) * 100 # Lambda usado para calcular a porcentagem
    df_ocorr['% Total'] = ocurr.apply(percentage) # Criamos a coluna das porcentagens

    if option == 'Specific Number':
        pass
    
    else:
        if option == 'mais frequentes':
            df_ocorr.sort_values('% Total', inplace = True, ascending = False) # Ordenamos o dataframe em ordem decrescente

        elif option == 'menos frequentes':
            df_ocorr.sort_values('% Total', inplace = True, ascending = True) # Ordenamos o dataframe em ordem crescente


        print(f"Os números {option} são:")
        for num, ocorr in (df_ocorr.iloc[:6,0]).items():
            print(f"{num} - foi sorteado {int(ocorr)} vezes\n")

    return

        

