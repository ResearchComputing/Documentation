# Running Large Language Models

Large Language Models (LLMs) have become extremely popular. Although LLMs such as ChatGPT and Google's Gemini are extremely useful, there are two primary downsides to using such a service: data privacy and cost. Additionally, it is often the case that more specialized LLMs are needed (rather than large general models) or researchers want to train models to fit their specialized case. The current solution to these issues is to run local open-source LLMs. In this section, we provide several approaches for setting up and running open-source LLMs on Alpine and Blanca using popular frameworks. 

```{warning}
Before running or working with LLMs on CURC resources, please be sure that you are adhering to all [CURC User Policies](https://curc.readthedocs.io/en/latest/additional-resources/policies.html) and CU's policies and guidance around Artificial Intelligence outlined in the pages [Artificial Intelligence at CU Boulder](https://www.colorado.edu/information-technology/artificial-intelligence-cu-boulder) and [Resources & Guidance](https://www.colorado.edu/information-technology/ai-cu-boulder/resources-guidance#accordion-1981143711-1). 
```

## Accessing stored LLMs on CURC

Where 

Why this is important 

## Using LLM Frameworks

Given most LLM frameworks are in rapid development, functionality is constantly changing. Additionally, the newest models often require the newest version of the framework to properly function. For this reason, at the moment, CURC is not providing modules for these LLM frameworks. Instead, we provide detailed instructions below for installing the version of the framework that works for your use case and common ways to use this framework. 

```{note}
Current instructions are only available for NVIDIA GPUs.
```

(tabset-ref-llm-frameworks)=
`````{tab-set}
:sync-group: tabset-llm-frameworks

````{tab-item} Ollama
:sync: llm-frameworks-ollama

[Ollama](https://ollama.com/) is an open-source, lightweight, and extremely beginner friendly tool that enables users to run LLMs locally and retrieve models that are compatible with the system they are running on. 

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


::::

````

````{tab-item} Transformers by Hugging Face
:sync: llm-frameworks-huggingface

Add introduction to Transformers 

# Installation

::::{dropdown} Show 
:icon: note

::::

# Running an LLM 

::::{dropdown} Show 
:icon: note

```{tip}
Before installing a model, see if CURC already provides this model! This will save you storage space and time. For more information, see [Accessing stored LLMs on CURC](#accessing-stored-llms-on-curc).
```

::::

````

`````