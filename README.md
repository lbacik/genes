[![codecov](https://codecov.io/gh/lbacik/genes/branch/main/graph/badge.svg?token=LP0KIDNBQ5)](https://codecov.io/gh/lbacik/genes)

# Simple library for playing with genetic algorithms

Install
    
    pip install genes

Use

    from genes import *

To create **initial population** (randomly):

    inital_population: Population = population_factory.create_population(POPULATION, LENGTH, PERCENTAGE)

where:

`POPULATION` - is a number of _individuals_ 

`LENGTH` - is a Genotype length

`PERCENTAGE` - each Genotype is randomly created, and consists a list of Gens (the length of which 
is determined by the `LENGTH`) - this factor allows to set percentage of chance to _get_ "1" for a particular Gen. 

Sample **FitnessFunction**:

    class SimpleFitnessFunction(FitnessFunction):
    
        def fit(self, genotype: Genotype) -> float:
            n = 0
            for gen in genotype:
                if gen is True:
                    n += 1
            return n

Having the initial population and fitness function defined, the **Genetic Algorithm** can be started:

    genes_api = genes_api_from_params_factory(
        SimpleFitnessFunction(),
        GAFactoryParams(
            population=POPULATION,
            selection_limit=POPULATION // 2,
            children_per_pair=4,
            mutation_probability=0.2,
        )
    )
    gen = genes_api.calculate(inital_population, GENERATIONS)

where:

`GENERATIONS` - is how many generations we want to calculate

To print the last generated generation type (the first column is the fitness function result): 

    print(gen)
    
    77	111011111011011110101110111111110001110111111101110111011111111111110101101010011111111000111111111
    78	111111111011011110101110111111110001110111111101110111011111111111110101101010011111111000111111111
    78	111111111011011110101110111111110001110111111101110111011111111111110101101010011111111000111111111
    77	111111111011011110101110111111110001100111110101110111011111111111111101101010011111110100111111111
    78	111111111011011110101110111111110001110111110101110111011111111111111101101010011111110100111111111
    78	111111111011011110101110111111110001110111110101110111011111111111111101101010011111110100111111111
    78	111111111011011110101110111111110001110111111101110111011111111111110101101010011111111000111111111
    ...


Dependencies required to play with plots: 

    import json
    import pandas as pd
    import matplotlib


Example:

    p = pd.read_json(json.dumps(genes_api.stats.population_history_stats))
    p.plot(figsize=(20,6))

![](data/plot01.png)