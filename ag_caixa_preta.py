#-*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:42:15 2013

@Autores: 
Cleidson dos Santos Souza
Felipe Túlio de Castro
Guilherme Macedo Mendes
Rennan Aquino Neri
"""
# importação e renomeação dos pacotes de funções
import numpy as np
import matplotlib as mpl
import os
from scipy.stats.mstats import mquantiles

#Limpeza da tela do shell Python
os.system('cls')

#Construção do menu do script - Cabeçalho
print u'Universidade Estadual de Montes Claros (Unimontes)'
print u'Especialização em Engenharia de Sistemas'
print u'Disciplina: Algoritmos Genéticos'
print u'Professor: Renato Dourado Maia'
print u'Problema da Caixa Preta - Trabalho Prático \n'
print u'Equipe de desenvolvimento: \nCleidson dos Santos Souza; Felipe Túlio de Castro; Guilherme Macedo Mendes; Rennan Aquino Neri. \n'

#Menu de configuração paramétrica
print u'MENU DE CONFIGURAÇÃO DO SISTEMA \n'
print u'Escolha o tipo de seleção que deseja utilizar: (1) Roleta (2) Torneio'
Op_Selecao = input('Resposta -> ')
print u'Escolha o tipo de cruzamento que deseja utilizar: (3) Ponto de corte (4) Uniforme'
Op_Cruzamento = input('Resposta -> ')
print u'Escolha o tipo de mutação que deseja utilizar: (5) Bit (6) Bit a Bit '
Op_Mutacao = input('Resposta -> ')
print u'Deseja utilizar o elitismo no algoritmo: (7) Sim (8) Não'
Op_Elitismo = input('Resposta -> ')
print u'Defina a taxa de cruzamento: '
Prob_Cruzamento = input('Resposta -> ')
print u'Defina a taxa de mutação: '
Taxa_Mutacao = input('Resposta -> ')
print u'Defina a quantidade de indivíduos da população: '
Tam_Populacao = input('Resposta -> ')
print u'Defina a quantidade de gerações: '
Maximo_Geracoes = input('Resposta -> ')

#Inicialização do código genético
print '\n'
print u'INICIALIZAÇÃO DO ALGORITMO GENÉTICO\n'

#Declaração das variáveis iniciais
Num_Execucoes = 100
Tam_Individuo = 36
Maior_Fitness = 0
Menor_Fitness = 0
Num_sucessos = 0
Solucao_Otima = 0
Execucao = 1
Linha = 0
Coluna = 0
Somatoria_Fitness = 0
Populacao_Selecionada = np.zeros((Tam_Populacao, Tam_Individuo))
Populacao_Cruzamento = np.zeros((Tam_Populacao, Tam_Individuo))
Populacao_Mutacao = np.zeros((Tam_Populacao, Tam_Individuo))
Mascara_Bits = np.zeros((1,Tam_Individuo))
Media_Fitness_Geracao = np.zeros((Maximo_Geracoes,1))
Melhor_Fitness_Geracao = np.zeros((Maximo_Geracoes,1))
Melhor_individuo_Geracao = np.zeros((Maximo_Geracoes,Tam_Individuo))
Maior_Fitness_Execucao = np.zeros((Num_Execucoes,1))
Menor_Fitness_Execucao = np.zeros((Num_Execucoes,1))
Media_Fitness_Execucao = np.zeros((Num_Execucoes,1))

#Laço de repetição das execuções solicitadas para o trabalho
while (Execucao <= Num_Execucoes):
    
    Populacao_Inicial = np.ones((Tam_Populacao, Tam_Individuo))
    
    #Geração da população inicial    
    for Linha in range(Tam_Populacao):
        for Coluna in range(Tam_Individuo):
            Populacao_Inicial[Linha,Coluna] = round(np.random.rand(1,1))
    
    # Laço de repetição das gerações para a evoluççao do Algoritmo Genético
    Geracao = 1
    Media_Fitness_Geracao = np.zeros((Maximo_Geracoes+1,1))
    Melhor_Fitness_Geracao = np.zeros((Maximo_Geracoes+1,1))
    Melhor_Individuo = np.zeros((Maximo_Geracoes+1,Tam_Individuo))
    while (Geracao <= Maximo_Geracoes):
        #Função que gera o fitness dos indivíduos
        Fitness = np.zeros((Tam_Populacao,1))
        for Linha in range(Tam_Populacao):
            b01 = Populacao_Inicial[Linha,1] * Populacao_Inicial[Linha,4];
            b02 = Populacao_Inicial[Linha,22] * Populacao_Inicial[Linha,13];
            b03 = Populacao_Inicial[Linha,23] * Populacao_Inicial[Linha,3];
            b04 = Populacao_Inicial[Linha,20] * Populacao_Inicial[Linha,9];
            b05 = Populacao_Inicial[Linha,35] * Populacao_Inicial[Linha,14];
            b06 = Populacao_Inicial[Linha,10] * Populacao_Inicial[Linha,25];
            b07 = Populacao_Inicial[Linha,15] * Populacao_Inicial[Linha,16];
            b08 = Populacao_Inicial[Linha,2] * Populacao_Inicial[Linha,32];
            b09 = Populacao_Inicial[Linha,27] * Populacao_Inicial[Linha,18];
            b10 = Populacao_Inicial[Linha,11] * Populacao_Inicial[Linha,33];
            b11 = Populacao_Inicial[Linha,30] * Populacao_Inicial[Linha,31];
            b12 = Populacao_Inicial[Linha,21] * Populacao_Inicial[Linha,24];
            b13 = Populacao_Inicial[Linha,34] * Populacao_Inicial[Linha,26];
            b14 = Populacao_Inicial[Linha,28] * Populacao_Inicial[Linha,6];
            b15 = Populacao_Inicial[Linha,7] * Populacao_Inicial[Linha,12];
            b16 = Populacao_Inicial[Linha,5] * Populacao_Inicial[Linha,8];
            b17 = Populacao_Inicial[Linha,17] * Populacao_Inicial[Linha,19];
            b18 = Populacao_Inicial[Linha,0] * Populacao_Inicial[Linha,29];
            b19 = Populacao_Inicial[Linha,22] * Populacao_Inicial[Linha,3];
            b20 = Populacao_Inicial[Linha,20] * Populacao_Inicial[Linha,14];
            b21 = Populacao_Inicial[Linha,25] * Populacao_Inicial[Linha,15];
            b22 = Populacao_Inicial[Linha,30] * Populacao_Inicial[Linha,11];
            b23 = Populacao_Inicial[Linha,24] * Populacao_Inicial[Linha,18];
            b24 = Populacao_Inicial[Linha,6] * Populacao_Inicial[Linha,7];
            b25 = Populacao_Inicial[Linha,8] * Populacao_Inicial[Linha,17];
            b26 = Populacao_Inicial[Linha,0] * Populacao_Inicial[Linha,32];
            
            Fitness[Linha, 0] = 9 + b01 - b02 + b03 - b04 + b05 - b06 + b07 + b08 + b09 + b10 \
            - b11 - b12 + b13 - b14 + b15 - b16 + b17 - b18 + b19 + b20 + b21 + b22 \
            + b23 + b24 + b25 + b26

        #----------------------------------------------------------------------------------------------
        #Função de elitismo

        if Op_Elitismo == 7:
            Media_Fitness_Geracao[Geracao,0] = np.mean(Fitness)
            #valor = np.max(Fitness)
            idc = np.argmax(Fitness)
            Melhor_Individuo[Geracao,:] = Populacao_Inicial[idc,:]
            Melhor_Fitness_Geracao[Geracao,0] = Fitness[idc,0]
            
            if Geracao > 1:
                if Melhor_Fitness_Geracao[Geracao,0] < Melhor_Fitness_Geracao[Geracao-1]:
                    Melhor_Individuo[Geracao,:] = Melhor_Individuo[Geracao-1,:]
                    Melhor_Fitness_Geracao[Geracao,0] = Melhor_Fitness_Geracao[Geracao-1,0]
            
            Populacao_Inicial[1,:] = Melhor_Individuo[Geracao,:]
            Fitness[1,0] = Melhor_Fitness_Geracao[Geracao,0]
            
          
        #----------------------------------------------------------------------------------------------
        #Funções de Seleçao
        if Op_Selecao == 1:
            Linha_Selecao = 2
            Somatoria_Fitness = np.sum(Fitness)
            for Linha_Selecao in range(Tam_Populacao):
                Num_Randomico = round(np.random.random())
                Acumulo = 0
                j = 1
                for j in range(Tam_Populacao):
                    Acumulo = Acumulo + Fitness[j,0]
                    if Acumulo >= Num_Randomico:
                        Populacao_Selecionada[Linha_Selecao,:] = Populacao_Inicial[j,:]
                        break
        elif Op_Selecao == 2:
            for Linha in range(Tam_Populacao):
                num1 = round(np.random.random())
                num2 = round(np.random.random())
                if Fitness[num1,0] > Fitness[num2,0]:
                    Populacao_Selecionada[Linha,:] = Populacao_Inicial[num1,:]
                elif Fitness[num1,0] < Fitness[num2,0]:
                    Populacao_Selecionada[Linha,:] = Populacao_Inicial[num2,:]
                elif Fitness[num1,0] == Fitness[num2,0]:
                    Populacao_Selecionada[Linha,:] = Populacao_Inicial[num2,:]
           
        #----------------------------------------------------------------------------------------------
        #Funções de Cruzamento
        if Op_Cruzamento == 3:
            Ponto_Corte = np.random.randint(1,Tam_Individuo)
            for i in range(Tam_Individuo):
                if i < Ponto_Corte:   
                    Mascara_Bits[0,i] = 0
                elif i >= Ponto_Corte:
                    Mascara_Bits[0,i] = 1         
                    
            Primeiro_Individuo = 0;
            Segundo_Individuo = 0;
            cont = 0            
            
            while (cont < Tam_Populacao):        
                while (Primeiro_Individuo == Segundo_Individuo):
                    Primeiro_Individuo = np.random.randint(0, Tam_Populacao)            
                    Segundo_Individuo = np.random.randint(0, Tam_Populacao)               
                Taxa_Cruzamento = np.random.random()               
                if Taxa_Cruzamento <= Prob_Cruzamento:
                    for j in range (Tam_Individuo):                             
                        if Mascara_Bits[0,j] == 0:
                            Populacao_Cruzamento[cont,j] = Populacao_Selecionada[Primeiro_Individuo,j]
                            Populacao_Cruzamento[cont+1,j] = Populacao_Selecionada[Segundo_Individuo,j]                   
                        elif Mascara_Bits[0,j] == 1:
                            Populacao_Cruzamento[cont,j]=Populacao_Selecionada[Segundo_Individuo,j]                    
                            Populacao_Cruzamento[cont+1,j]=Populacao_Selecionada[Primeiro_Individuo,j]
                elif Taxa_Cruzamento > Prob_Cruzamento:          
                    Populacao_Cruzamento[cont] = Populacao_Selecionada[Primeiro_Individuo]          
                    Populacao_Cruzamento[cont+1] = Populacao_Selecionada[Segundo_Individuo]
                cont = cont + 2
        elif Op_Cruzamento == 4:
            
            for i in range(Tam_Individuo):
                Mascara_Bits[0,i] = np.random.choice([0,1])        
#            print Mascara_Bits    
            Primeiro_Individuo = 0;
            Segundo_Individuo = 0;
            cont = 0            
            
            while (cont < Tam_Populacao):        
                while (Primeiro_Individuo == Segundo_Individuo):
                    Primeiro_Individuo = np.random.randint(0,Tam_Populacao)            
                    Segundo_Individuo = np.random.randint(0,Tam_Populacao)               
                Taxa_Cruzamento = np.random.random()                      
                if Taxa_Cruzamento <= Prob_Cruzamento:
                    for j in range(Tam_Individuo):                             
                        if Mascara_Bits[0,j] == 0:
                            Populacao_Cruzamento[cont,j] = Populacao_Selecionada[Primeiro_Individuo,j]
                            Populacao_Cruzamento[cont+1,j] = Populacao_Selecionada[Segundo_Individuo,j]                   
                        elif Mascara_Bits[0,j] == 1:
                            Populacao_Cruzamento[cont,j]=Populacao_Selecionada[Segundo_Individuo,j]                    
                            Populacao_Cruzamento[cont+1,j]=Populacao_Selecionada[Primeiro_Individuo,j]
                elif Taxa_Cruzamento > Prob_Cruzamento:          
                    Populacao_Cruzamento[cont] = Populacao_Selecionada[Primeiro_Individuo]          
                    Populacao_Cruzamento[cont+1] = Populacao_Selecionada[Segundo_Individuo]
                cont = cont + 2     
                
        #---------------------------------------------------------------------------------------------
        #Funções de Mutação
        if Op_Mutacao == 5:
            Populacao_Mutacao = Populacao_Cruzamento
            i = 0
            while (i < Tam_Populacao):
                Prob_Mutacao = np.random.randint(0,Tam_Individuo)
                if Prob_Mutacao <= Taxa_Mutacao:
                    Bit = round(np.random.random())
                    if Populacao_Mutacao[i, Bit] == 1:
                        Populacao_Mutacao[i, Bit] = 0
                    else:
                        Populacao_Mutacao[i, Bit] = 1
                i = i + 1
        elif Op_Mutacao == 6:
            Populacao_Mutacao = Populacao_Cruzamento
            i = 0
            while (i < Tam_Populacao):
                for j in range(Tam_Individuo):
                    Prob_Mutacao = np.random.randint(0,Tam_Individuo)
                    if Prob_Mutacao <= Taxa_Mutacao:
                        if Populacao_Mutacao[i, j] == 1:
                            Populacao_Mutacao[i,j] = 0
                        else: 
                            Populacao_Mutacao[i, j] = 1
                i = i + 1

        #----------------------------------------------------------------------------------------------
        Populacao_Inicial[:,:] = Populacao_Mutacao[:,:]
        
        Geracao = Geracao + 1
    #----------------------------------------------------------------------------------------------
    #Funções que geram os resultados solicitados
    Maior_Fitness_Execucao[Execucao-1,0] = np.max(Fitness)
    Menor_Fitness_Execucao[Execucao-1,0] = np.min(Fitness)
    Media_Fitness_Execucao[Execucao-1,0] = np.mean(Fitness)
    if np.max(Fitness) == 27:
        Num_sucessos = Num_sucessos + 1
        
    Execucao = Execucao + 1
    
print u'ALGORTIMO GENÉTICO FINALIZADO. GERANDO OS RESULTADOS...\n'        
print u'Quantidade de sucessos: ' + str(Num_sucessos)
print u'Maior valor de Fitness: ' + str(np.max(Maior_Fitness_Execucao))
print u'Menor valor de Fitness: ' + str(np.min(Menor_Fitness_Execucao))
print u'Valor Médio dos Fitness: ' + str(np.mean(Media_Fitness_Execucao))
print u'Desvio padrão: ' + str(np.std(Maior_Fitness_Execucao))
print u'Primeiro, segundo e terceiro quartil: ' + str(mquantiles(Fitness))

mpl.pyplot.boxplot(Maior_Fitness_Execucao)
mpl.pyplot.title(u'Melhores Fitness obtidos nas 100 execuções')

#Teste de Wilcoxon
#Teste_Wilcoxon = sp.stats.ranksums()