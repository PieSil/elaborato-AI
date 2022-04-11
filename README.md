# Studio dell'algoritmo Min-Conflicts applicato al Map Coloring Problem

### Testo Elaborato:

In questo esercizio si implementano (in un linguaggio di programmazione a scelta) le strategie di ricerca locale min-conflicts e constraint weighting descritte in in R&N 2021 6.4. 
Si comparano quindi le due strategie sul problema della colorazione di mappe, (si possono generare problemi casuali con la strategia suggerita nell’esercizio 6.10 in R&N 2021), 
studiando empiricamente il tempo di esecuzione in funzione del numero di variabili n del problema, 
facendo crescere n quanto più possibile (nei limiti ragionevoli imposti dall’hardware disponibile).

## Descirizione Moduli Sorgente

### constants.py

Utilizzato per definire le costanti utilizzate all'interno degli script, come ad esempio il parametro Max Steps per l'algoritmo Min-Conflicts
od il percorso di directory rilevanti, come quelle che contegono i file in cui sono memorizzati i problemi generati automaticamente od i risultati ottenuti.

### problem_generator.py

Uno script che genera una serie di problemi di Map-Coloring seguendo la procedura definita nell'esercizio 6.10 in R&N 2021, 
ogni problema così generato viene memorizzato in un file .txt all'interno della directory "csps".

### problem_solver.py

Uno script che carica i problemi contenuti nella directory "csps" ed esegue, su ognuno di essi, 
l'algoritmo Min-Conflicts sia in modo classico (senza euristiche di alcun tipo), che utilizzando l'euristica constraint weighting.
Lo script registra i tempi di esecuzione ed il numero di passi impiegato per risolvere ciascun problema, successivamente, detto <img src="https://render.githubusercontent.com/render/math?math=S"> l'insieme di problemi che hanno la stessa dimensione,
calcola la media del tempo di esecuzione e del numero di passi dei problemi in <img src="https://render.githubusercontent.com/render/math?math=S">.
I valori medi così calcolati sono poi memorizzati sotto forma di file .txt nella directory "results".
Lo script registra e memorizza allo stesso modo il numero totale di problemi risolti e non risolti utilizzando sia l'algoritmo classico che la versione con constraint-weighting.

### plotter.py

Lo script carica i risultati contenuti nei file presenti nella directory "results" e li utilizza per realizzare dei plot in modo da visualizzare più chiaramente i risultati.
Lo script stampa inoltre la variazione percentuale media dei valori medi del numero di passi e dei tempi di esecuzione registrati.
I plot sono poi memorizzati sotto forma di file .png nella directory "plots".

### algorithm.node

Contiene la definizione della classe Node, rappresentata da un id numerico, una coordinata x ed un coordinata y (utilizzate durante la generazione di un problema di Map-Coloring) 
ed un insieme di vicini.

### algorithm.solver

Contiene la definizione dell'algoritmo Min-Conflicts, l'euristica constraint weighting può essere abilitata o disabilitata attraverso l'utilizzo del 
parametro useWeights.

### algorithm.problem

Contiene la definizione della classe Problem, caratterizzata da numero di nodi (dimensione), numero di colori da utilizzare, insieme dei nodi, 
insieme degli archi, un dizionario che associa un peso ad ogni arco (i pesi sono inizializzati a 1) ed infine il numero massimo di vicini che un nodo 
può avere, è stato deciso di limitare il numero massimo di vicini di ciascun nodo poiche è stato osservato che, a causa della procedura utilizzata per generare i problemi,
si ottenevano spesso problemi in cui un singolo nodo (od un insieme ristretto di nodi) risultava collegato a numerosi nodi i quali non erano però collegati tra loro, 
rendendo quindi triviale il problema di Map-Coloring; detta <img src="https://render.githubusercontent.com/render/math?math=n"> la dimensione del problema, il valore massimo di vicini per ciascun nodo è stato fissato a <img src="https://render.githubusercontent.com/render/math?math=\sqrt{n}">.

### utils.result_utility

Definisce la classe ResultFileManager, utilizzata per memorizzare e caricare i risultati calcolati dallo script: problem_solver.py

### utils.problem_utility

Definisce la classe ProblemFileManager, utilizzata per memorizzare e caricare i problemi creati tramite lo script: problem_generator.py

### utils.segment_functions

Definisce delle funzioni utilizzate durante la procedura di generazione di un problema, tali funzioni sono utilizzate per verificare se due segmenti 
<img src="https://render.githubusercontent.com/render/math?math=(P1, P2)"> e <img src="https://render.githubusercontent.com/render/math?math=(Q1, Q2)"> si intersecano o meno.


