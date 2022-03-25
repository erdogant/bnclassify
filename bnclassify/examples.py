# --------------------------------------------------
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://erdogant.github.io/bnlearn
# Licence     : MIT
# --------------------------------------------------

from bnclassify import bnclassify as bn
print(bn.__version__)
dir(bn)

# %% This is faster:
import bnlearn as bn

# %%
# Load example dataset
df = bn.import_example('sprinkler')

edges = [('Cloudy', 'Sprinkler'),
         ('Cloudy', 'Rain'),
         ('Sprinkler', 'Wet_Grass'),
         ('Rain', 'Wet_Grass')]

# Make the actual Bayesian DAG
DAG = bn.make_DAG(edges, verbose=0, methodtype='bayes')
model = bn.parameter_learning.fit(DAG, df, verbose=3)
bn.print_CPD(DAG)

model = bn.parameter_learning.fit(DAG, df, verbose=3)
bn.print_CPD(model)


# %%
import bnlearn as bn

# Example dataset
source=['Cloudy','Cloudy','Sprinkler','Rain']
target=['Sprinkler','Rain','Wet_Grass','Wet_Grass']
weights=[1,2,1,3]

# Convert into sparse datamatrix
df = bn.vec2df(source, target, weights=weights)
# Make DAG
DAG = bn.make_DAG(list(zip(source, target)), verbose=0)
# Make plot
bn.plot(DAG, interactive=True)
