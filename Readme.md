#  MineSweeper : Inference-Informed Action

### Representation
The representation is a 2D array of squares, with each square storing several fields. For each cell we have the following information:​​   
1. **status = False​**     
*Check if a specific cell has a mine or not.​*
2. **isVisited = False**    
*​Check if a cell is opened or not.​*  
3. **flagged = False**   
*Is the cell marked or not?.​*  
4. **visible= "-"**  ​
*Initially all cells are blocked.*  
5. **​value = 0**  
*​The value inside the cells; 1 - 8 provides the clue information​For the neighbours which have mines or 9 if it is a mine.*

Through the program these attributes are going to be updated accordingly and the clue cell information will be used to determine which cells to be flagged and which one are safe to be opened.

We ran the traditional game with the defined difficulty levels and obtained the accuracy levels of the algorithm as shown below:

| Level of Difficulty | No. of maze solved out of 50 | Accuracy |
|---------------------|------------------------------|----------|
| Beginner(9x9 with 10 mines)| 5 | 10% ~ 15% |
| Intermediate (16x16 with 40mines) | 3 | 6% |
| Advanced (30x30 with 185mines) | 1 | 2% |

### Efficiency
For our implementation, we observed that the algorithm does not have any problem until the size of the maze is extremely large. It can solve 50x50 minesweeper maze with low mine density(10% mines). After 50x50, the computer runs out of memory or the system crashes. This is a problem-specific constraint as the Minesweeper problem is an NP-Complete problem. As the dimensions of the maze increases, the memory requirement will increase exponentially.The problem that the algorithm faces is where it has to guess between two choices which have equal probability of being a mine. This is an implementation specific constraint as there will always be such scenarios where the algorithm will have to make a guess.

# Contributions
1. Divyaprakash Dhurandhar
Involved in the development of base classes and algorithmic understanding of the simple square analysisalgorithm for solving the minesweeper maze. Developed parts of the simple square analysis algorithm. Generated performance results for the minesweeper solver and contributed in the final report.

2. Abdulaziz Almuzaini
Worked on implementation in creating classes and the algorithms. Involved in answering the questionsand analyzing the algorithms, data and the results. Created graph, tables and other visualizations for the reports.

3. Sri Gautham Subramani
Worked on the implementation of randomized selection of the algorithm. Involved in computing testcases for answering questions, explaining the inference, generating results and evaluating performance of the algorithm.

4. Shubhada Suresh
Contributed in development of algorithms and involved in report writing especially the bonus questions.Involved in analyzing the algorithm, generating results and evaluating performance of the algorithm.