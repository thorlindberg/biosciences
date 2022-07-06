This project aimed to demonstrate that programming can be applied in the field of Bioscience, for the purpose of gaining insights into genetic heredity of traits and characters. The code for this project is written in the [Python programming language](https://www.python.org "https://www.python.org"), and an anonymised social security dataset is utilised for the analysis.

As a result of these efforts, a series of tables and graphs can be produced when the developed code is applied to a dataset matching the given structure. The methods were developed with universiality in mind, enabling their application on any dataset irrespective of its information contents.

In reflecting on the code, it has become evident that the methods developed should have been phrased as abstracted algorithms, which can be combined to gain a specific insight, rather than as solutions to specific questions. The consequence of this implementation is that the methods cannot be combined in any way, and the code patterns could be improved with recursive methods.

<br>

**Project**

The source material for this project is a series of questions, requirements, and a dataset representing an anonymised social security database. Each question is answered through a specific method that is only applicable to the respective question, and the `main.py` code calls these methods after retrieving an input directory and initialising the dataset as an object.

<br>

**Results**

The methods called in the `main.py` code produce a series of tables and graphs, and each method calls a `helper function` to save its result as a file in the input directory. 

<br>

**Methods**

The developed methods receive the input directory and initialised dataset object as parameters, and they have no return, as their results are saved to the input directory. Each method is structured to prefix the functional implementation with a multi-line string describing the purpose and parameters of the respective method.

<br>

**Helper functions**

The developed helper functions are called either during initialisation of the dataset or from the developed methods. Each helper function is structured to prefix the functional implementation with a multi-line string describing the purpose, parameters and expected return (if any) of the respective helper function.
