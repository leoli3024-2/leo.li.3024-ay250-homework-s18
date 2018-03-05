# Homework 4

## Processor Type
Macbook Pro with 2.9 GHz Intel Core i7, 8 Cores

## Running the program

All work is done through a jupyter notebook file. Running the file should give clear outputs, and all cells should run without any error. The plot appears at the last but one cell, with the last cell serving to save the plot as a high-resolution image for future references. In my work, I used os.popen() to run terminal command in python. 

## Dicussion of the plot

![Results](https://github.com/leoli3024-2/leo.li.3024-ay250-homework-s18/blob/master/hw_4/Performances.png)

In general, we reproduce the results given in the assignment instruction document. We see same patterns/features in the example plots: the parallelization methods are only in advantages if the number of darts thrown is very large. At a smaller/lower amount, the simple serial method is way much faster than the rest two. This is because the parallelization methods require overhead time to set up the communications and distribute work between workers (cores). As the number of thrown-darts increases, the execution time of multiprocessing implementation first surpasses that of serial method at near 10^4 (at near <10^3 in example), and the execution time of ipyparallel module then surpasses near 10^5 (between 10^4 and 10^5 in example). Beyond 10^5 (100,000) darts thrown, the two parallelization methods' execution times converge to around the same time. After 100,000, all three methods perform with a nearly linear relationship (execution time against number of darts thrown). Note that this happens in a log-log space, meaning that they are changing at an exponential rate in linear-linear space. A few other discrepancies occur at the early stage (smaller amount of darts thrown). Though my serial approach runtime is lower than the one in example, both ipyparallel and multiprocessing implementations start at a higher (slower) time. Besides, the shape of the relationships of these two start to shift/change at a much later time (with larger amount of darts). Since my processor type is with 8 cores, so there (I believe) would require a larger amount of time to communication across cores, which may occupy a bit more time <- eventually leads to a slower starting execution time and observable improvements over increase of darts thrown.

