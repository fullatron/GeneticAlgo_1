from CNF_Creator import *
import numpy as np
from numpy.random import choice
import matplotlib.pyplot as plt
import time


start_time = time.time()

def validator(sentence,individual):
    count = 0
    for i in sentence:
        for j in i:
            if (j<0 and individual[-j - 1]==0) or (j>0 and individual[j-1]==1):
                count +=1
                break
    return count*100/len(sentence)

def reproduce(individual_1, individual_2, fitness_1, fitness_2):
    index=np.random.randint(0,50)
    new_individual=individual_1[0:index]+individual_2[index:]
    return new_individual

def mutate(individual):
    mutations = np.random.random(len(individual))<0.02
    for i in range(len(individual)):
        if mutations[i]:
            individual[i]=int(not(individual[i]))
    return individual

def _ga(sentence, population, fitness, _bestindividual, _maxfitness):
    #print(fitness)
    count=0
    countgen=0
    start_time = time.time()
    while (time.time() - start_time)<45 and count<4000:
        _maxx=0
        countgen+=1
        #print(population[0])
        popnew=[]
        fitnew=[]
        for i in range(20):
            val=0
            individuals = choice( range(20), 2, fitness)
            individual_1=list(population[individuals[0]])
            individual_2=list(population[individuals[1]])
            new_individual=reproduce(individual_1,individual_2, fitness[individuals[0]], fitness[individuals[1]])
            popnew.append(new_individual)
            val=validator(sentence, new_individual)
            if np.random.random()<0.2:
                new_individual=mutate(new_individual)
                val=validator(sentence, new_individual)
            fitnew.append(val)
            _maxx=np.maximum(_maxx,val)
        fitness=fitnew
        if _maxx>=_maxfitness:
                count=0
        else:
            count+=1
        _maxfitness=np.maximum(_maxx,_maxfitness)
        population=popnew
    print("new: "+str(_maxfitness))
    #print(countgen)
    return _maxfitness,countgen


def main(m):
    cnfC = CNF_Creator(n=50) # n is number of symbols in the 3-CNF sentence
    sentence = cnfC.CreateRandomSentence(m) # m is number of clauses in the 3-CNF sentence
    start_time = time.time()
    _maxfitness=0
    #print('Random sentence : ', (sentence))
    population=np.random.randint(2,size=(20, 50))
    _maxfitness=0
    fitness=[]
    
    _bestindividual=population[0]

    for individual in population:
        val=validator(sentence, individual)
        if _maxfitness<val:
            _maxfitness=val
            _bestindividual=individual
        fitness.append(val)
    #print("old: "+str(_maxfitness))
    _maxfitness,countgen = _ga(sentence, population, fitness, _bestindividual, _maxfitness)
    return time.time()-start_time, _maxfitness,countgen
    #print("time taken: "+str(time.time()-start_time))
    
    #print(_bestindividual)
    #print(_maxfitness)

    #sentence = cnfC.ReadCNFfromCSVfile()
    #print('\nSentence from CSV file : ',sentence)

#    print('\n\n')
#    print('Roll No : 2020H1030999G')
#    print('Number of clauses in CSV file : ',len(sentence))
#    print('Best model : ',[1, -2, 3, -4, -5, -6, 7, 8, 9, 10, 11, 12, -13, -14, -15, -16, -17, 18, 19, -20, 21, -22, 23, -24, 25, 26, -27, -28, 29, -30, -31, 32, 33, 34, -35, 36, -37, 38, -39, -40, 41, 42, 43, -44, -45, -46, -47, -48, -49, -50])
#    print('Fitness value of best model : 99%')
#    print('Time taken : 5.23 seconds')
#    print('\n\n')

def plotter(t,fit,gens):
    x=list(range(100,320,20))
    
    file=open("time.txt","w")
    file.write(str(t))
    file.close()

    file=open("fit.txt","w")
    file.write(str(fit))
    file.close()

    file=open("gens.txt","w")
    file.write(str(gens))
    file.close()

    plt.subplot(131)
    plt.plot(x,fit)
    plt.xlabel("clauses")
    plt.ylabel("average fitness")
    plt.title("Average fitness vs Clause")
    plt.show()

    plt.subplot(132)
    plt.plot(x,t)
    plt.xlabel("clauses")
    plt.ylabel("average time")
    plt.title("Average time vs Clause")
    plt.show()

    plt.subplot(133)
    plt.plot(x,gens)
    plt.xlabel("clauses")
    plt.ylabel("average generations")
    plt.title("Average generations vs Clause")
    plt.show()



if __name__=='__main__':
    _time=time.time()-start_time
    t=[]
    fit=[]
    gens=[]
    
    for m in range(100,320,20):
        _t=0
        _maxfitness=0
        _gen=0
        for i in range(10):
            _ti, _maxfitnessi, _geni= main(m)
            _t+=_ti
            _maxfitness+=_maxfitnessi
            _gen+=_geni
        t.append(_t/10)
        fit.append(_maxfitness/10)
        gens.append(_gen/10)
    plotter(t,fit,gens)




    
#    for i in range(1):
 #        max=0
  #       population=np.random.randint(2,size=(40, 50))
   #      #print(population)
    #     
     #    start_time = time.time()
      #   while (time.time() - start_time)<0.02: