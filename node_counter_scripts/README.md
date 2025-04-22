# Running node count script

To run the script that breaks down node counts by 
contributors and partitions, you will first need to 
create an environment that has all the required 
dependencies. A base Python install plus Pandas 
should give you everything you need. For convenience, 
we provide node_count_env.yaml in this directory. To 
create the environment, do the following: 
```
mamba env create -f node_count_env.yaml
```
To activate the created environment, do the following: 
```
mamba activate node-count-env
```

Now that the environment is setup, you can obtain the 
breakdown of different nodes by doing the following run:
```
python run.py
```
