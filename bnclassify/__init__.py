from bnlearn.bnlearn import bnlearn as bnclassify


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.0'

# module level doc-string
__doc__ = """
BNCLASSIFY - bnclassify (or bnlearn) is an Python package for learning the graphical structure of Bayesian networks, estimate their parameters, perform inference, sampling and comparing networks.
======================================================================================================================================================================================================

Description
-----------
* Learning a Bayesian network can be split into two problems:
    * Structure learning: Given a set of data samples, estimate a DAG that captures the dependencies between the variables.
    * Parameter learning: Given a set of data samples and a DAG that captures the dependencies between the variables.
    * Making inferences.
    * Parameter and structure learning is for *discrete* nodes
        * Score-based structure estimation (BIC/BDeu/K2 score; exhaustive search, hill climb/tabu search)
        * Constraint-based structure estimation (PC)
        * Hybrid structure estimation (MMHC)


Example
-------
>>> https://github.com/erdogant/bnlearn

References
----------
* https://github.com/erdogant/bnlearn
* https://towardsdatascience.com/a-step-by-step-guide-in-detecting-causal-relationships-using-bayesian-structure-learning-in-python-c20c6b31cee5
* https://towardsdatascience.com/a-step-by-step-guide-in-designing-knowledge-driven-models-using-bayesian-theorem-7433f6fd64be

"""
