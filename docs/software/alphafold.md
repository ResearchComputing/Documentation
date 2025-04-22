# AlphaFold

## AlphaFold Overview
AlphaFold is a program that predicts the three-dimensional structure of proteins from their amino acid sequences. It is currently available as module on CURC Alpine. Please contact <rc-help@colorado.edu> if you would like to run AlphaFold on Blanca.

(tabset-ref-batch-scripting)=
`````{tab-set}
:sync-group: tabset-batch-scripting

````{tab-item} AlphaFold 2 
:sync: batch-scripting-ex1

Load the default AlphaFold 2 module:
```
module load alphafold/2.3.1
```

View run options:
```
run_alphafold
```
#### AlphaFold 2 Module
Loading the AlphaFold 2 module does the following:

- redirects temporary files from `/tmp` to `/scratch/alpine/$USER`
    - you can override this path by resetting TMPDIR *after* you load the module:
        ```
        module load alphafold/2.3.1
        export TMPDIR=<path/of/your/choosing>
        ```
- activates the AlphaFold 2 conda environment

- sets `CURC_AF_DBS` and `CURC_AF_EXAMPLES` environment variables (see "AlphaFold 2 Databases" and "AlphaFold 2 Examples" sections, below)

- creates a shortcut to the AlphaFold 2 script so you can run the program with `run_alphafold`

#### AlphaFold 2 Databases
The AlphaFold 2 databases are located in `/gpfs/alpine1/datasets/bioinformatics/alphafold`.
Note that this directory is not visible from a login node. Loading the AlphaFold 2 module stores this path in `CURC_AF_DBS`.

#### AlphaFold 2 Examples
Several example fasta files are located in `/curc/sw/install/bio/alphafold/examples`.
Loading the AlphaFold 2 module stores this path in `CURC_AF_EXAMPLES`:

```
ls $CURC_AF_EXAMPLES
dummy.fasta  multimer.fa  rcsb_pdb_7DDD.fasta  T1050.fasta
```
#### Example Job Script
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
module load alphafold/2.3.1

#change directory
cd /projects/$USER

#run AlphaFold
run_alphafold -d $CURC_AF_DBS -o . -f $CURC_AF_EXAMPLES/dummy.fasta -t 2020-05-14 -m "monomer" -g true
```

````
````{tab-item} AlphaFold 3
:sync: batch-scripting-ex2

AlphaFold 3 has a substantially updated diffusion-based architecture that is capable of predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues. That neccessitates a different kind of input than the fasta input in AlphaFold 2.

On CURC’s Alpine system, AlphaFold 3 is available as a containerized module. It uses Apptainer/Singularity under the hood and is fully self-contained except for the separately downloaded model parameters (required).

#### AlphaFold 3 Module
Load AlphaFold 3 module:
```
module load alphafold/3.0.0
```
View run options:
```
run_alphafold --help
```
Loading the AlphaFold 3 module does the following:
- sets environment variables used by the wrapper script:
    - `AF3_IMAGE`: Path to the AlphaFold 3 container image 
    - `AF3_CODE_DIR`: Directory containing the AlphaFold 3 codebase
    - `AF3_DATABASES_DIR`: Location of the required AlphaFold 3 reference databases

- redirects temporary files to `/scratch/alpine/$USER`
    - you can override this path by resetting TMPDIR *after* you load the module:
        ```
        module load alphafold/3.0.0
        export TMPDIR=<path/of/your/choosing>
        ```
- creates a shortcut to the AlphaFold 3 script so you can run the program with `run_alphafold`

#### AlphaFold 3 Model Weights
```{important}
Due to license restrictions for AlphaFold 3 model weights, you must read and comply with the [Model Parameters](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md) and [Outputs](https://github.com/google-deepmind/alphafold3/blob/main/OUTPUT_TERMS_OF_USE.md) Terms of Use. In short, only non-profit activity is allowed, unethical use of the outputs is disallowed and make sure to cite the AlphaFold 3 paper in any publication. To gain access to AlphaFold 3 at CURC, request access to the weights by filling out [this form](https://docs.google.com/forms/d/e/1FAIpQLSfWZAgo1aYk0O4MuAXZj8xRQ8DafeFJnldNOnh_13qAx2ceZw/viewform). You will receive two e-mails. First is acknowledgement of receipt of the request form. The second, in a day or so, is the approval with a link to download the weights. Once you have downloaded them, put them in a filesystem you have access to on Alpine.
```

#### AlphaFold 3 Input
AlphaFold 3 uses JSON input files instead of FASTA.
You can either:
- Provide a single JSON file via `--json_path=<path of input>`
- Or a directory of JSONs via `--input_dir=<path of input>`

#### AlphaFold 3 Databases
Databases used by AlphaFold 3 are pre-installed and accessible via:
`/gpfs/alpine1/datasets/bioinformatics/alphafold3`. Note that this directory is not visible from a login node. Loading the AlphaFold 3 module stores this path in `AF3_DATABASES_DIR`.

#### AlphaFold 3 Workflow
AlphaFold 3 runs in two stages:

Stage 1 (MSA Search): CPU and I/O-intensive; uses jackhmmer and hhmsearch.

Stage 2 (Inference): GPU-intensive; performs structure prediction.

To better utilize limited GPU resources, these stages can be split using flags:
 - `--norun_inference` → Run only the MSA/data pipeline (Stage 1)
 - `--norun_data_pipeline` → Run only the inference step (Stage 2)

#### AlphaFold 3 Examples
Example input files and scripts are in `/curc/sw/install/bio/alphafold/3.0.0/examples`.
Loading the AlphaFold 3 module stores this path in `AF3_EXAMPLES`:
```
ls $AF3_EXAMPLES
alphafold3_alpine_cpu.sh  alphafold3_alpine_gpu.sh  alphafold3_alpine.sh  fold_protein_2PV7
```
This folder includes:
- `alphafold3_alpine.sh`: Sample batch script to run the complete AlphaFold 3 pipeline.
- `alphafold3_alpine_cpu.sh`: Sample batch script to run only Stage 1(MSA Search).
- `alphafold3_alpine_gpu.sh`: Sample batch script to run only Stage 2 (Inference).

You can copy the examples folder to a location where you have write permissions and customize the scripts:

```bash
cd /projects/$USER
cp -R /curc/sw/install/bio/alphafold/3.0.0/examples .
cd examples
```

#### Example Job Script
Path of the script: `$AF3_EXAMPLES/alphafold3_alpine.sh`

``` bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=30:00
#SBATCH --partition=al40
#SBATCH --qos=normal
#SBATCH --gres=gpu:1
#SBATCH --job-name=af3_test
#SBATCH --output=af3_test_%j.out
#SBATCH --ntasks=8
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<your email address>

# Load the AlphaFold 3 module
module purge
module load alphafold/3.0.0

# Set input JSON, output directory, and model parameter path
export INPUT_FILE=$AF3_EXAMPLES/fold_protein_2PV7/alphafold_input.json
export OUTPUT_DIR=/path/to/output
export AF3_MODEL_PARAMETERS_DIR=/path/to/alphafold3/params

# Run AlphaFold 3
run_alphafold --json_path=$INPUT_FILE --output_dir=$OUTPUT_DIR --model_dir=$AF3_MODEL_PARAMETERS_DIR
```
````
`````