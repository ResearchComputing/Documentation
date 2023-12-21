# AlphaFold

## AlphaFold Overview
AlphaFold is a program to
It is currently available as module on CURC Alpine. Please contact <rc-help@colorado.edu> if you would like to run AlphaFold on Blanca.

## Running AlphaFold

Load the default AlphaFold module:
```
module load alphafold
```

View run options:
```
run_alphafold
```

### AlphaFold Module

Loading the AlphaFold module does the following:

- redirects temporary files from `/tmp` to `/scratch/alpine/$USER`
    - you can override this path by resetting TMPDIR *after* you load the module:
        ```
        module load alphafold
        export TMPDIR=<path/of/your/choosing>
        ```
- activates the AlphaFold conda environment

- sets `CURC_AF_DBS` and `CURC_AF_EXAMPLES` environment variables (see 'AlphaFold Databases' and 'AlphaFold Examples' sections, below`)

- creates a shortcut to the AlphaFold script so you can run the program with `run_alphafold`


### AlphaFold Databases
The AlphaFold databases are located in `/gpfs/alpine1/datasets/bioinformatics/alphafold`. Note that this directory is not visible from a login node. Loading the AlphaFold module stores this path in `CURC_AF_DBS`.

### AlphaFold Examples
Several example fasta files are located in `/curc/sw/install/bio/alphafold/examples`. Loading the AlphaFold module stores this path in `CURC_AF_EXAMPLES`:

```
ls $CURC_AF_EXAMPLES
dummy.fasta  multimer.fa  rcsb_pdb_7DDD.fasta  T1050.fasta
```

### Example Job Script

This example job script below is saved in `/curc/sw/install/bio/alphafold/2.3.1`. You can copy it to any space you have write permissions and make the desired changes:
```bash
cd /projects/$USER
cp /curc/sw/install/bio/alphafold/2.3.1/alphafold_alpine.sh .
```

``` bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=06:00:00
#SBATCH --partition=aa100
#SBATCH --qos=normal
#SBATCH --gres=gpu:1
#SBATCH --job-name=multimer_test
#SBATCH --output=multimer_test_%j.out
#SBATCH --ntasks=40
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<your email address>

module purge
module load alphafold

#change directory
cd /projects/$USER

#run AlphaFold
run_alphafold -d $CURC_AF_DBS -o . -f $CURC_AF_EXAMPLES/dummy.fasta -t 2020-05-14 -m "monomer" -g true
```
