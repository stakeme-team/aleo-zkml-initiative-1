<img width="960" alt="aleo-zkml-initiative-1" src="https://github.com/stakemepro/aleo-zkml-initiative-1/assets/104348282/9c701594-4f27-4ed7-a4dd-1610bc9082ea">

## aleo-zkml-initiative-1

> **Zero-Knowledge Machine Learning** *(ZKML)* is  concept that marries the realms of privacy-focused cryptographic techniques and machine learning. Aleo, a zero-knowledge blockchain, contributes to the ZKML space by providing a platform to develop private applications. With its unique programming model, developers can write privacy-preserving, verifiable computations with ease, which are then compiled into zero-knowledge proofs. In the context of ZKML, Aleo can enable the training and execution of machine learning models in a zero-knowledge environment, ensuring that no information about the data, apart from the output, is revealed. This is a big step towards privacy-preserving AI/ML solutions.

STAKEME took part in the zkml-initiative-1 hackathon and the work was done in two sections: **zkML Algorithms** and **Python Developer Tooling**
<hr>
In the zkML Algorithms section: The Linear Regression ML algorithm was developed using the Leo language. More detailed description is in Google Colaboratory (you can use online) or you can download .ipynb (Jupyter Notebook)
<br></br>
Google Colaboratory: <a href="https://colab.research.google.com/drive/1c3_Pu7yELRymKxCocp4PKbJ3uGVsXTq7?usp=sharing">https://colab.research.google.com/drive/1c3_Pu7yELRymKxCocp4PKbJ3uGVsXTq7?usp=sharing</a>
<hr>
In the Python Developer Tooling section: the following modules have been developed
<br></br>
<li>Running Leo from Python</li>
<li>Convert types Python/Leo</li>
<br></br>

**Running Leo from Python**
</br>
Usage
```python
from interp_leo.uitls import convert_from_leo_type
from interp_leo.leo_program import LeoProgram

leo_program = LeoProgram(path=os.getcwd() + '/path_to_aleo_application')
leo_program.func(...)
```
leo_program will automatically parse all functions and you will be able to access these functions directly in python. When passing arguments, they will be automatically converted to Leo type

**Convert types Python/Leo**
```python
convert_from_leo_type('1u128') #128
convert_to_leo_type(10, 'u128') #10i128
```
Note: In case of exceeding the range of available numbers of a certain type, an error will be issued