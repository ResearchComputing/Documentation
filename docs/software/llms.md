# Running Large Language Models

Large Language Models (LLMs) have become extremely popular. Although LLMs such as ChatGPT and Google's Gemini are extremely useful, there are two primary downsides to using such a service: data privacy and cost. Additionally, it is often the case that more specialized LLMs are needed (rather than large general models) or researchers want to train models to fit their specialized case. To address these cases, users can run local open-source LLMs. In this section, we provide several approaches for setting up and running open-source LLMs on Alpine and Blanca using popular frameworks. 

```{warning}
Before running or working with LLMs on CURC resources, please be sure that you are adhering to all [CURC User Policies](https://curc.readthedocs.io/en/latest/additional-resources/policies.html) and CU's policies and guidance around Artificial Intelligence outlined in the pages [Artificial Intelligence at CU Boulder](https://www.colorado.edu/information-technology/artificial-intelligence-cu-boulder) and [Resources & Guidance](https://www.colorado.edu/information-technology/ai-cu-boulder/resources-guidance#accordion-1981143711-1). 
```

## Accessing stored LLMs on CURC

To streamline access and reduce redundant storage of LLMs, CURC has created a shared space for common LLMs. This is a CURC managed space, as such, users cannot install models themselves in this space. However, if you believe a model should be available in this directory, please reach out to <rc-help@colorado.edu>. To access these models, users should utilize the environment variable `CURC_LLM_DIR` followed by their framework of choice. For more information about what models and frameworks are provided, please consult the tabs below. 
```{important}
The path specified by `CURC_LLM_DIR` is only available on compute nodes.  
```

(tabset-ref-curc-llms)=
`````{tab-set}
:sync-group: tabset-curc-llms

````{tab-item} Ollama
:sync: curc-llms-ollama

For the Ollama framework, we provide the following models: 
- `gpt-oss:20b`
- `gemma3:12b`
- `llama3.1:8b`

If you are using your own installation of Ollama, you should set the Ollama model path as follows:
```
export OLLAMA_MODELS=$CURC_LLM_DIR/ollama
```
```{note}
If you are loading our Ollama module e.g. `module load ollama`, we automatically set the model path to this directory for you. 
```

````

````{tab-item} Transformers by Hugging Face
:sync: curc-llms-hf-transformers

Add content here 

````


`````

## Using LLM Frameworks

In this section, we provide instructions for obtaining access to common LLM frameworks. Additionally, we provide simple examples that demonstrate how to use these LLM frameworks. 
```{important}
- Due to the rapid pace of development in most LLM frameworks, CURC will provide only the most up-to-date version for the provided framework modules. These versions will be updated during our regular monthly planned maintenance. If you need older or newer versions of these frameworks, we provide detailed instructions below for installing the version of the framework that works for your use case and common ways to use this framework. 
- Current instructions and modules are only available for NVIDIA GPUs.
```

### Ollama 

[Ollama](https://ollama.com/) is an open-source, lightweight, and extremely beginner friendly tool that enables users to run LLMs locally and retrieve models that are compatible with the system they are running on. 

(tabset-ref-ollama)=
`````{tab-set}
:sync-group: tabset-ollama

````{tab-item} Quickstart
:sync: ollama-quickstart

In this tab, we provide instructions for using our system installed Ollama. Although these instructions greatly simplify the steps needed to use Ollama, the system installed Ollama or provided API may not fit your needs. If you need to install a different version of Ollama or need to customize the provided environment, you will need to follow the instructions in the [In-depth instructions tab](?tabset-ollama=ollama-indepth#tabset-ref-ollama){.external}. 

To begin, we first need to jump on an NVIDIA GPU compute node (i.e. submitting a job to either the `aa100` or `atesting_a100` partition). For the purposes of this tutorial, we will start an interactive session on the `atesting_a100` partition.
```
sinteractive --partition=atesting_a100 --qos=testing --nodes=1 --gres=gpu --ntasks=10 --time=01:00:00
```
Once the session has successfully started, 



::::{dropdown} Show how to use a different model path
:icon: note 

In cases where you want to use a model that is different from CURC installed models, you will need to 


First, set the different module path and make sure it exists e.g. 
```
export OLLAMA_MODELS=/projects/$USER/my_ollama_models
mkdir -p $OLLAMA_MODELS
```
You will then need to restart the serve. To do this, we first need to stop the current session by killing the Ollama process. You can find this process using the following:
```
[user1@c3gpu-c2-u13 ~]$ ps -u $USER | grep ollama 
2210854 pts/0    00:00:00 ollama
```
The number at the beginning of this output is the Ollama process (e.g. `2210854`). You then need to kill this process e.g. 
```
kill 2210854
``` 
Once the process has been successfully killed, you can then restart the Ollama serve: 
```
nohup ollama serve > /dev/null 2>&1 &
```
You can now install any compatible model you want by pulling the model down and running it. For more information on this topic, see the [Ollama README.md](https://github.com/ollama/ollama/blob/main/README.md). 

::::


````

````{tab-item} In-depth instructions
:sync: ollama-indepth


# Installation

::::{dropdown} Show 
:icon: note

To begin, let's create a directory specifically for the version of Ollama that we want to install (here we choose version `v0.11.10`):
```
export ollama_v="v0.11.10"
mkdir -p /projects/$USER/ollama/$ollama_v
cd /projects/$USER/ollama/$ollama_v
```
```{tip}
For available versions, consult [Ollama's release page](https://github.com/ollama/ollama/releases).
```
Now, we grab the Ollama binary for this version:
```
curl -LO https://github.com/ollama/ollama/releases/download/${ollama_v}/ollama-linux-amd64.tgz 
tar -xzf ollama-linux-amd64.tgz
rm ollama-linux-amd64.tgz
```
After execution, this command should create a `bin` and `lib` directory containing our Ollama binary and associated libraries, respectively.
::::

# Running an LLM from the command line

::::{dropdown} Show 
:icon: note
Now that we have Ollama installed, we will startup an Ollama serve on a GPU compute node and interact with the LLM from the command line.

1. Start up an interactive job on a GPU node. For testing purposes, we will use our A100 testing partition:
    ```
    sinteractive --partition=atesting_a100 --qos=testing --nodes=1 --gres=gpu --ntasks=10 --time=01:00:00
    ```
    ```{important}
    For non-testing workflows, users should request NVIDIA GPUs using the `aa100` partition. 
    ```
2. Now that we have a session started, we will export important environment variables using the `ollama_v` variable we established in the previous section. 
    ```{warning}
    Maybe put this stuff in the .bashrc
    ```
    ```
    export PATH=/projects/$USER/ollama/$ollama_v/bin:$PATH
    export LD_LIBRARY_PATH=/projects/$USER/ollama/$ollama_v/lib:$LD_LIBRARY_PATH
    export OLLAMA_TMPDIR=$SCRATCHDIR/$USER/ollama_temp
    export OLLAMA_NUM_PARALLEL=1
    export OLLAMA_MAX_LOADED_MODELS=1
    ```
3. When starting an Ollama serve, it is important to pick a host port that is not used by others. You can use the following code to set this port:
    ```
    while true; do
    rand=$(( (RANDOM << 15) | RANDOM ))
    port=$((rand % (9999 - 9000 + 1) + 9000))
    if ! lsof -i :$port &>/dev/null; then
        export OLLAMA_HOST=0.0.0.0:$port
        break
    fi
    done
    ```
4. Now, we select the directory where our Ollama models are stored.
    ```
    export OLLAMA_MODELS=/projects/$USER/my_ollama_models
    ```
    ```{note}
    Before setting this variable, consult [Accessing stored LLMs on CURC](#accessing-stored-llms-on-curc) to see if CURC already provides the model you intend to use! 
    ```
5. Ensure that the proper directories exist
    ```
    mkdir -p $OLLAMA_TMPDIR
    mkdir -p $OLLAMA_MODELS
    ```
6. Now, we can start an Ollama serve in the background
    ```
    nohup ollama serve > /dev/null 2>&1 &
    ```
7. At this point, Ollama is up and running. We can now run Ollama from the command line! Let's run a very simple model. 
    ```{important}
    The following command will install the model, if you do not have it. Before executing this command, see if CURC already provides the model you want to run! This will save you storage space and time. For more information, see [Accessing stored LLMs on CURC](#accessing-stored-llms-on-curc).
    ```
    ```
    ollama run llama3.1:8b
    ```
9. After running the model, a prompt will appear where you can ask your question.
    ```
    >>> In one sentence, how cool is CU Research Computing?
    CU Research Computing is pretty cool because it provides a robust suite of services and expert 
    support to help researchers tackle complex computational challenges and accelerate their work.
    ```
10. To get out of the prompt:
    ```
    >>> /bye
    ```
::::

# Running an LLM from a Python script

::::{dropdown} Show 
:icon: note

Alternatively, one can run Ollama from within a Python script. 

Refer to steps on creating an Ollama serve 

To get access to our Ollama install in Python, we need to install Ollama's Python API. We will do this by creating a mamba environment and installing the necessary packages in that environment. 

Link to conda docs 

Create a mamba environment specifically for this package: 
```
module load miniforge
mamba create -n ollama_api python=3.12
mamba activate ollama_api
pip install ollama
```

Start up the serve 

```python
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1:8b', messages=[
  {
    'role': 'user',
    'content': 'In one sentence, how cool is CU Research Computing?',
  },
])

print(response.message.content)
```

```
python test.py 
CU Research Computing is an exceptionally cool and powerful resource that provides researchers with access to high-performance computing clusters, advanced data storage systems, and expert support to facilitate cutting-edge research and innovation.
```

For more tutorials and usages of the API, see https://github.com/ollama/ollama-python

::::

````

`````

### Transformers by Hugging Face 

Add introduction to Transformers 

(tabset-ref-hf-transformers)=
`````{tab-set}
:sync-group: tabset-hf-transformers

````{tab-item} Quickstart
:sync: hf-transformers-ollama

Quick start

````

````{tab-item} In-depth instructions 
:sync: hf-transformers-indepth


# Installation

::::{dropdown} Show 
:icon: note

1. Create a hugging face account: https://huggingface.co/join

2. Generate a token for our system using https://huggingface.co/settings/tokens
Do read permissions for simplicity and copy the token 

3. Start up an interactive job on a GPU node. For testing purposes, we will use our A100 testing partition:
    ```
    sinteractive --partition=atesting_a100 --qos=testing --nodes=1 --gres=gpu --ntasks=10 --time=01:00:00
    ```

module load miniforge 
mamba create -n hf-transformers-env 
mamba activate hf-transformers-env
mamba install conda-forge::transformers

pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
pip install datasets evaluate accelerate timm
pip install huggingface_hub[cli]

```{note}
Here we specifically grab the newest stable PyTorch version that is compatible with CUDA 12.9. 
```

```{warning} 
put in .bashrc or create script maybe? 
```
export HF_HOME=/projects/$USER/hf_transformers
export HF_HUB_CACHE=/projects/$USER/hf_transformers/.cache

mkdir -p $ HF_HUB_CACHE

4. Do auth login on our system 
```
hf auth login
```
When prompted for the token, provide the one you gave above.
Add token as git credential? (Y/n) n 

5. While logged in go to the Hugging Face model card that you want to run and accept the terms of use (if it has them).

```{note}
Depending on the model, it can take 30 minutes or more to get access to the model. 
```

6. Once you have received the email that you have access to your model (if it is a gated model), you can then proceed to use the model: 
```
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B", dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")

model_inputs = tokenizer(["The secret to baking a good cake is "], return_tensors="pt").to(model.device)

generated_ids = model.generate(**model_inputs, max_length=30)
print(tokenizer.batch_decode(generated_ids)[0])
```


::::

# Running an LLM 

::::{dropdown} Show 
:icon: note

```{tip}
Before installing a model, see if CURC already provides this model! This will save you storage space and time. For more information, see [Accessing stored LLMs on CURC](#accessing-stored-llms-on-curc).
```

https://huggingface.co/docs/transformers/installation

https://huggingface.co/models

::::

````

`````