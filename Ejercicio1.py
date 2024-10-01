import Cuantico
import math
##Ejercicio número 1
def Create_GC(N_Nodes,Slits):
    Grafo=[[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
           [(0.5, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
           [(0.5, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
           [(0, 0), (0.33, 0.0), (0.0, 0.0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], 
           [(0, 0), (0.33, 0.0), (0.0, 0.0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
           [(0, 0), (0.33, 0.0), (0.33, 0.0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
           [(0, 0), (0.0, 0.0), (0.33, 0.0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
           [(0, 0), (0.0, 0.0), (0.33, 0.0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]
    return Grafo
def MultRCE():
    Slits=2
    Targets=5
    N_Nodes=Slits+Targets+1
    State=[[1]]
    for i in range(N_Nodes-1):
        State.append([0])
    grafo=Create_GC(N_Nodes,Slits)
    print("\nEl estado del sitema al inicio es:\n")
    print(State)
    print("\nEl estado del grafo con numeros complejos es: \n")
    for i in grafo:
        print(i)
    print("\nEl estado del grafo en probabilidad es: \n")
    for i in Cuantico.probs(grafo):
        print(i)
    print("\nEl estado del grafo despues de 2 time clicks es: \n")
    Ttik=Cuantico.MC(grafo,grafo)
    for i in Ttik:
        print(i)
    print("\nEl estado del grafo en probabilidad en 2 time clicks es:\n ")
    for i in Cuantico.probs(Ttik):
        print(i)
    print("\nEl estado del sistema despues de 2 time cliks es:\n ")
    resul=Cuantico.states(Cuantico.probs(Ttik),State)
    print(resul)
    for i in range(len(resul)):
        resul[i]=resul[i]*100
    Cuantico.grafics(resul,N_Nodes,2,"Porcentaje(%)")
MultRCE()