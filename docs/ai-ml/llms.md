# Running Large Language Models

Large Language Models (LLMs) have become extremely popular. Although LLMs such as ChatGPT and Google's Gemini are extremely useful, there are two primary downsides to using such a service: data privacy and cost. Additionally, it is often the case that more specialized LLMs are needed (rather than large general models), or researchers want to train models to fit their specialized case. To address these cases, users can run open-source LLMs locally. In this section, we provide several approaches to setting up and running open-source LLMs on Alpine and Blanca using popular frameworks. 

```{warning}
Before running or working with LLMs on CURC resources, please be sure that you are adhering to all [CURC User Policies](https://curc.readthedocs.io/en/latest/additional-resources/policies.html) and CU's policies and guidance around Artificial Intelligence outlined in the pages [Artificial Intelligence at CU Boulder](https://www.colorado.edu/information-technology/artificial-intelligence-cu-boulder) and [Resources & Guidance](https://www.colorado.edu/information-technology/ai-cu-boulder/resources-guidance). 
```

## Accessing stored LLMs on CURC

To streamline access and reduce redundant storage of LLMs, CURC has created a shared space for common LLMs. This is a CURC managed space. As such, users cannot install models themselves in this space. However, if you believe a model should be available in this directory, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). To access the models stored in this shared space, users should utilize the environment variable `CURC_LLM_DIR`, followed by their framework of choice. For more information about what models and frameworks are provided, please consult the tabs below. 
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
    - An open-source model from OpenAI 
    - This model has been quantized using the MXFP4 format
    - Requires about 14 GB of GPU memory 
- `gemma3:12b`
    - An open-source model from Google 
    - This model has been quantized using the Q4_K_M format
    - Requires around 8 GB of GPU memory 
- `llama3.1:8b`
    - An open-source model from Meta
    - This model has been quantized using the Q4_K_M format
    - Requires about 5 GB of GPU memory 
- `embeddinggemma:latest`
    - An open-source embedding model from Google 
    - Used for turning text data into a numerical vector representation 
    - Requires approximately 1 GB of GPU memory
    
If you are using your own installation of Ollama and would like to use a CURC-provided model, you should set the Ollama model path as follows:
```
export OLLAMA_MODELS=$CURC_LLM_DIR/ollama
```
```{note}
- If you are loading our Ollama module e.g. `module load ollama`, we automatically set the model path to this directory for you. 
- `OLLAMA_MODELS` must be set. If this variable is not set, models will be downloaded into your home directory. 
```

````

````{tab-item} Transformers by Hugging Face
:sync: curc-llms-hf-transformers

For the Transformers framework, we provide the following models: 
- `gpt-oss-20b`
    - An open-source model from OpenAI 
    - This model has been quantized using the MXFP4 format
    - Requires about 14 GB of GPU memory 
- `gemma-3-12b-it`
    - An open-source model from Google 
    - This model has not been quantized and its tensors are in BF16 precision
    - Requires more than 20 GB of GPU memory to run non-quantized version
- `Llama-3.1-8B-Instruct`
    - An open-source model from Meta
    - This model has not been quantized and its tensors are in BF16 precision
    - Requires more than 20 GB of GPU memory to run non-quantized version
    
:::{note}
These models are contained in the following path: 
```
$CURC_LLM_DIR/hf-transformers
```
:::

````


`````

## Using LLM Frameworks

In this section, we provide instructions for obtaining access to common LLM frameworks. Additionally, we provide simple examples that demonstrate how to use these LLM frameworks. 
```{important}
- Due to the rapid pace of development in most LLM frameworks, CURC will provide only the most up-to-date version for the provided framework modules. These versions will be updated during our regular monthly planned maintenance. If you need older or newer versions of these frameworks, we provide detailed instructions below for installing specific versions of the frameworks. 
- Current instructions and modules are only available for NVIDIA GPUs.
```

### Ollama 

[Ollama](https://ollama.com/) is an open-source, lightweight, and extremely beginner friendly tool that enables users to run LLMs locally and retrieve models that are compatible with the system they are running on. 

(tabset-ref-ollama)=
`````{tab-set}
:sync-group: tabset-ollama

````{tab-item} CURC provided install
:sync: ollama-quickstart

In this tab, we provide instructions for using our system installed Ollama. Although these instructions greatly simplify the steps needed to use Ollama, the system installed Ollama or provided API may not fit your needs. If you need to install a different version of Ollama or need to customize the provided environment, you will need to follow the instructions in the [Self-install instructions tab](?tabset-ollama=ollama-indepth#tabset-ref-ollama){.external}. 

To begin, we first need to jump on an NVIDIA GPU compute node (i.e. submitting a job to either the `aa100` or `atesting_a100` partition). For the purposes of this tutorial, we will start an interactive session on the `atesting_a100` partition.
```
sinteractive --partition=atesting_a100 --qos=testing --nodes=1 --gres=gpu --ntasks=10 --time=01:00:00
```
Once the session has successfully started, we can startup an Ollama server and set default environment variables by loading the Ollama module:
```
module load ollama
```
:::{tip}
If you would like to point to your own directory that contains Ollama compatible models, you can do this as you load the module e.g.: 
```
export OLLAMA_MODELS=/projects/$USER/my_ollama_models; module load ollama
```
:::

At this point, you can use Ollama from the command line. If you would like to also use Ollama from within Python (needed for the [Using Ollama in a Python script](#using-ollama-in-a-python-script) section below), then you will need to activate our provided [uv](../software/uv.md) environment:
```
module load uv 
source $CURC_UV_ENV_DIR/ollama-python-api-env/bin/activate
``` 

````

````{tab-item} Self-install instructions
:sync: ollama-indepth

Below we provide detailed instructions for users who want to install their own version of Ollama and compatible Python API. 

## Ollama install 

To begin, let's create a directory specifically for the version of Ollama that we want to install (here we choose version `v0.15.4`):
```
export ollama_v="v0.15.4"
mkdir -p /projects/$USER/ollama/$ollama_v
cd /projects/$USER/ollama/$ollama_v
```
```{tip}
For available versions, consult [Ollama's release page](https://github.com/ollama/ollama/releases).
```
Now, we grab the Ollama binary and libraries for this version:
```
curl -LO https://github.com/ollama/ollama/releases/download/${ollama_v}/ollama-linux-amd64.tar.zst
tar --use-compress-program=unzstd -xf ollama-linux-amd64.tar.zst
rm ollama-linux-amd64.tar.zst
```
:::{tip}
Older Ollama versions were not compressed with `zst`. If you are trying to install one of these older versions that has the file extension `tgz`, you can obtain the binary and libraries as follows: 
```
curl -LO https://github.com/ollama/ollama/releases/download/${ollama_v}/ollama-linux-amd64.tgz 
tar -xzf ollama-linux-amd64.tgz
rm ollama-linux-amd64.tgz
```
:::

After execution, these commands should create a `bin` and `lib` directory containing our Ollama binary and associated libraries, respectively.

## Setting up the Ollama install 

Now that we have Ollama installed, we need to start up an Ollama server on an NVIDIA GPU compute node (i.e. submitting a job to either the `aa100` or `atesting_a100` partition). We will then be able to interact with Ollama and our LLMs from the command line. For the purposes of this tutorial, we will start an interactive session on the `atesting_a100` partition:
```
sinteractive --partition=atesting_a100 --qos=testing --nodes=1 --gres=gpu --ntasks=10 --time=01:00:00
```
```{important}
For non-testing workflows, users should request NVIDIA GPUs using the `aa100` partition. 
```

Now that we have a session started, we will export important environment variables using the `ollama_v` variable we established in the previous section. 
```
export ollama_v="v0.15.4"
export PATH=/projects/$USER/ollama/$ollama_v/bin:$PATH
export LD_LIBRARY_PATH=/projects/$USER/ollama/$ollama_v/lib:$LD_LIBRARY_PATH
export OLLAMA_TMPDIR=$SCRATCHDIR/$USER/ollama_temp
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
```
When starting an Ollama server, it is important to pick a host port that is not used by others. You can use the following code to set this port:
```
while true; do
rand=$(( (RANDOM << 15) | RANDOM ))
ollama_port=$((rand % (60000 - 40000 + 1) + 40000))
if ! ss -tuln | grep -q ":$ollama_port"; then
    export OLLAMA_HOST=0.0.0.0:$ollama_port
    break
fi
done
```
We can now set the directory where our Ollama models are stored.
```{note}
- Before setting this variable, consult [Accessing stored LLMs on CURC](#accessing-stored-llms-on-curc) to see if CURC already provides the model you intend to use! 
- `OLLAMA_MODELS` must be set. If this variable is not set, models will be downloaded into your home directory. 
```
```
export OLLAMA_MODELS=/projects/$USER/my_ollama_models
```
```{important}
All environment variables that have been set so far need to be set every time you want to use your install of Ollama. 
```

Ensure that the proper directories exist.
```
mkdir -p $OLLAMA_TMPDIR
mkdir -p $OLLAMA_MODELS
```
Finally, we can start an Ollama server in the background
```
nohup ollama serve > /dev/null 2>&1 &
```
This will enable us to use Ollama from the command line.

## Installing the Ollama Python API 

In the previous section, we set up the Ollama server. This will need to be done before you use the Ollama Python API. To use the Ollama Python API, you will also need to install the appropriate packages. This can be done by creating an environment (e.g. `ollama_api`). We will do this below using [uv](../software/uv.md):
```
module load uv
uv venv $UV_ENVS/ollama-python-api-env
source $UV_ENVS/ollama-python-api-env/bin/activate
uv pip install ollama
```
::::

````
`````
#### Running Ollama from the command line 

::::{dropdown} Show 
:icon: note

Before proceeding with these instructions, be sure that the Ollama server is up and running. Once the Ollama server is up and running, we can interact with an LLM from the command line! Let's run a very simple model, say the 8 billion parameter Llama 3.1 model:
```
ollama run llama3.1:8b
```
```{note}
If you are pointing to your own model directory, this command will install the model, if you do not have it. Depending on the model, this install can take awhile to complete. 
```
After running the model, Ollama will begin loading the model into memory. Note that this can take several minutes to do, depending on the model. Once the model has been loaded into memory, a prompt will appear where you can ask your question:
```text
>>> In one sentence, how cool is CU Research Computing?
CU Research Computing is pretty cool because it provides a robust suite of services and expert 
support to help researchers tackle complex computational challenges and accelerate their work.
```
To get out of the prompt perform the following action:
```
>>> /bye
```
::::

#### Using Ollama in a Python script

::::{dropdown} Show 
:icon: note

Before proceeding with these instructions, be sure that the Ollama server is up and running and the Ollama Python API is available. To begin, we need to create a Python script that specifies the model we want to use and input we want to provide to that model. Let's create a script called `llama_query.py` with the following content:
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
In this script we tell Ollama to use the `llama3.1:8b` model, provide it the query `In one sentence, how cool is CU Research Computing?`, and then print the response of the LLM.

To run the model, all we need to do is run this script: 
```
python llama_query.py
```
At the time of running this model, we obtain the following output:
```text
CU Research Computing is an exceptionally cool and powerful resource that provides researchers 
with access to high-performance computing clusters, advanced data storage systems, and expert 
support to facilitate cutting-edge research and innovation.
```
This of course is just a simple example showing how one can query Ollama models from within a Python script. This functionality opens the door for more complex queries and scripts. This example also touches on just one aspect of the Python API. For more tutorials and documentation of the API, see the `examples` directory and `README.md` file in the official [ollama-python](https://github.com/ollama/ollama-python) GitHub repository. 
::::

### Transformers by Hugging Face 

[Transformers](https://huggingface.co/docs/transformers/en/index#transformers) is Hugging Face's LLM framework. It should be noted that Transformers and Ollama are not exactly comparable, as Transformers includes additional functionality. However, it does provide a framework for accessing and running LLMs.  

(tabset-ref-hf-transformers)=
`````{tab-set}
:sync-group: tabset-hf-transformers

````{tab-item} CURC provided install
:sync: hf-transformers-ollama

In this tab, we provide instructions for using our system installed Transformers. Although these instructions greatly simplify the steps needed to use Transformers, the system installed Transformers and associated libraries may not fit your needs. If you need to install a different version or need to customize the provided environment, you will need to follow the instructions in the [Self-install instructions tab](?tabset-hf-transformers=hf-transformers-indepth#tabset-ref-hf-transformers){.external}. 

To begin, we first need to jump on an NVIDIA GPU compute node (i.e. submitting a job to either the `aa100` or `atesting_a100` partition). For the purposes of this tutorial, we will start an interactive session on the `atesting_a100` partition.
```
sinteractive --partition=atesting_a100 --qos=testing --nodes=1 --gres=gpu --ntasks=10 --time=01:00:00
```
Once you are on the GPU compute node, you can load the Transformers module, which contains the minimal libraries needed to run LLMs and sets important environment variables:
```
module load hf-transformers
```
Once this module has been loaded, you will be within the [uv](../software/uv.md) environment named `hf-transformers-env`. This environment will allow you to run all Transformers usage examples on this page. 

````

````{tab-item} Self-install instructions
:sync: hf-transformers-indepth

## Installing Transformers

In this section, we describe how to set up a minimal [uv](../software/uv.md) environment, which provides access to Transformers. To begin, we will jump on a standard CPU node. Please note that jumping on a GPU node to create the environment is not necessary. However, when you run the LLMs, you will want to be on a GPU node for most models.
```
sinteractive --ntasks=4 --partition=acompile --qos=compile --nodes=1 --time=01:00:00
```

Once a session has been established, we now need to create an environment that will allow us to work with the Transformers library and dependencies needed by the LLMs we would like to use. For this example, we will create a virtual environment called `hf-transformers-env`, use Python 3.12, and assume that only PyTorch is needed for our LLMs. First we create our environment:
```
module load uv 
uv venv $UV_ENVS/hf-transformers-env --python 3.12
```
Now, we activate the environment and install all of our dependencies: 
```
source $UV_ENVS/hf-transformers-env/bin/activate
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
uv pip install huggingface_hub[cli] protobuf tiktoken bitsandbytes
uv pip install -U transformers datasets evaluate accelerate timm kernels
```
```{note}
Here we specifically grab the newest stable PyTorch version that is compatible with CUDA 12.9. This will ensure that PyTorch can run on all NVIDIA GPU models currently on CURC resources. 
```
At this point, all libraries needed to run our LLM examples have been installed. However, it is very important to set the following environment variables and make sure that the associated directories exist (this will ensure that your home directory does not fill up):
```
export HF_HOME=/projects/$USER/hf_transformers
export HF_HUB_CACHE=/projects/$USER/hf_transformers/.cache
export HF_HUB_DISABLE_TELEMETRY=True
mkdir -p $HF_HUB_CACHE
```
```{important}
All environment variables that have been set need to be set every time you want to use your install of Transformers.
```

````

`````

#### Downloading Transformers Compatible Models

::::{dropdown} Show 

```{note}
Before proceeding with a model install, consult [Accessing stored LLMs on CURC](#accessing-stored-llms-on-curc) to see if CURC already provides the model you intend to use! 
```

In order to install models from Hugging Face, you will need to create an account using <https://huggingface.co/join>. Once you have an account, you will then need to generate a token for our system using the documentation provided under the [User access tokens](https://huggingface.co/docs/hub/en/security-tokens#user-access-tokens) page. If you only intend to install publicly available models and data, then usually read permissions are sufficient for the token. 

After you have your account set up, you can search models using the [Hugging Face Models](https://huggingface.co/models) page. Here you can refine your search based on the task you want to complete, model size, and dependent libraries. Once you have identified a model that you would like to run, review the model card, paying attention to the libraries needed and examples provided. If necessary, accept the terms of use for the model. For example, [Meta's Llama 3.1](https://huggingface.co/meta-llama/Llama-3.1-8B) requires you to accept a community license agreement. However, at the time of writing this documentation, OpenAI's [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) does not require a license agreement. 
```{note}
Depending on the model, it can take 30 minutes or more to get access to the model once you have accepted the terms of use. 
```

At this point, all necessary libraries should be installed in either your custom environment or CURC's provided environment and we can begin downloading the LLMs we would like to run. If you are using our Transformers module, `HF_HOME` and `HF_HUB_CACHE` will point to your project's directory, ensuring that your home directory does not fill up. If you are not using our module, be sure these variables are appropriately set before proceeding. There are several ways to install a model, however, we often suggest that you use the `huggingface-cli`. For more in-depth information about `huggingface-cli` (such as how to view models and delete them) see [Command Line Interface (CLI)](https://huggingface.co/docs/huggingface_hub/en/guides/cli#command-line-interface-cli). The [hf cache scan](https://huggingface.co/docs/huggingface_hub/en/guides/cli#hf-cache-scan) and [hf cache delete](https://huggingface.co/docs/huggingface_hub/en/guides/cli#hf-cache-delete) sections are particularly useful for managing models.

Once the `huggingface-cli` is available, you can set up your token associated with our system using the following
```
hf auth login
```
When prompted for the token, provide the one you generated at the beginning of this section. When asked if you would like to "Add token as git credential?" you may type "n", if you do not intend to use the token as a git credential. For new users, "n" is usually preferred for simplicity. 
:::{important}
To protect your tokens, it is suggested that you remove system-wide read privileges:
```
chmod o-r /projects/$USER/hf_transformers/stored_tokens
chmod o-r /projects/$USER/hf_transformers/token
```
:::
Now that we have our tokens set up and we have accepted the terms of use, we can install our model from the command line. Here, we will install a very simple Gemma model ([google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it)) into our directory `/projects/$USER/hf_transformers/gemma-3-270m-it`:
```
hf download --local-dir /projects/$USER/hf_transformers/gemma-3-270m-it google/gemma-3-270m-it 
```
```{tip}
On Hugging Face, there are often different types of LLMs. For example, some have "instruct" in their name or specify that they are instruct models. Instruct models are, as the name implies, instruction models. These models are most likely what you want as they are ideal for specifying tasks for the LLM to perform and are the models used in common chat interfaces. In contrast, the base models make no assumption about structure and are attempting to only complete the text provided. 
```
After this installation completes, you will then have access to your installed model! See the next section for instructions on running this LLM from Python. 
::::

#### Running an LLM from Python using Transformers

::::{dropdown} Show 
:icon: note

In this section, we assume that you have installed all necessary libraries and the model you would like to run (or are using our module and provided models). Additionally, we assume you are on an NVIDIA GPU compute node. Please note that the below instructions are just one possible way to run an LLM using Transformers. There are also other methods, such as [Pipelines](https://huggingface.co/docs/transformers/en/main_classes/pipelines#pipelines) that exist. 

Now that we are ready to run our LLM, there is one last important consideration we need to make before running the model: whether to quantize the LLM. Many models provided on Hugging Face are not quantized, and for this reason, are very large. Depending on the GPU you are using, this can be a big problem because you may not have enough space on the GPU's VRAM. For example, our `atesting_a100` partition only provides 20 GB of GPU memory (VRAM), which is often too small for medium-sized models that have not been quantized. When this is the case, we often want to perform [Quantization](https://huggingface.co/docs/transformers/v4.56.2/quantization/overview) to reduce the memory footprint. Below we provide an example where we do not utilize quantization and one where we do.  


(tabset-ref-transformers-run)=
`````{tab-set}
:sync-group: tabset-transformers-run

````{tab-item} No quantization
:sync: transformers-run-no-quant

In this tab, we run our `gpt-oss-20b` model without quantization. Quantization is not needed for this model, as by default, the model obtained from Hugging Face has been quantized using the MXFP4 format. Additionally, it nicely fits on one of our `atesting_a100` GPUs. To run the `gpt-oss-20b` model without quantization let's create the following script named `transformers_run_no_quant.py`:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import os 

# Get our system-defined path to CURC's shared LLMs
CURC_LLM_DIR = os.getenv('CURC_LLM_DIR')

# Specify that we want to use the gpt-oss-20b model that is in CURC's shared LLM directory 
path_to_model=f"{CURC_LLM_DIR}/hf-transformers/gpt-oss-20b"

# Obtain the model-defined tokenizer
tokenizer = AutoTokenizer.from_pretrained(path_to_model)

# Load the model onto the GPU and do not apply quantization 
model = AutoModelForCausalLM.from_pretrained(path_to_model, device_map="cuda")

# Specify the task we want the LLM to perform
messages = [{"role": "user", "content": "Write a paragraph about cookies."}]

# Format the input we will provide to the LLM and load this onto the GPU 
inputs = tokenizer.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)

# Generate the LLM response 
outputs = model.generate(**inputs, max_new_tokens=200)

# Print the provided LLM response
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
```
Once the script has been created, we can then run the script as follows: 
```
python transformers_run_no_quant.py
```
At the time of running this script, we obtain the following output: 
```text
<|channel|>analysis<|message|>The user: "Write a paragraph about cookies." Simple task. They likely want a paragraph. 
Could be about cookies (dessert) or cookie (browser cookie). ambiguous. The general reading is cookie as baked good. 
Provide descriptive paragraph. Write about ingredients, aroma, crispness, making. Could mention varieties. I should 
respond in a single paragraph. There's no other instruction. So produce a short, engaging paragraph.

Probably best to describe cookies. Let's go with a general paragraph about cookies. Ensure it's cohesive.
<|end|><|start|>assistant<|channel|>final<|message|>Cookies are the tiny, comforting bursts of sweetness that have 
delighted taste buds across the globe for generations. A classic chocolate‑chip cookie, with its buttery dough studded 
with melty chocolate morsels, offers a perfect balance of chewy center and slightly crisp edges—a texture symphony that 
warms the soul. The dough itself is an artful blend of flour, sugar, eggs, and butter, seasoned with vanilla and a hint 
of salt to amplify
```

````

````{tab-item} Applying Quantization 
:sync: transformers-run-quant

In this tab, we run our `Llama-3.1-8B-Instruct` model with quantization. Quantization is needed for this model if we want to run it on our `atesting_a100` GPUs. Here we will utilize QLoRA or 4-bit quantization. To run `Llama-3.1-8B-Instruct` with quantization, let's create the following script named `transformers_run_quant.py`:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import os 

# Get our system-defined path to CURC's shared LLMs
CURC_LLM_DIR = os.getenv('CURC_LLM_DIR')

# Specify that we want to use the Llama-3.1-8B-Instruct model that is in CURC's shared LLM directory 
path_to_model=f"{CURC_LLM_DIR}/hf-transformers/Llama-3.1-8B-Instruct"

# Use QLoRA or 4-bit quantization 
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",            
    bnb_4bit_use_double_quant=True,        
    bnb_4bit_compute_dtype=torch.bfloat16  
)

# Obtain the model-defined tokenizer
tokenizer = AutoTokenizer.from_pretrained(path_to_model)

# Load the model onto the GPU and apply quantization using bitsandbytes 
model = AutoModelForCausalLM.from_pretrained(path_to_model, device_map="cuda", quantization_config=bnb_config, dtype=torch.bfloat16)


# Specify the task we want the LLM to perform
messages = [{"role": "user", "content": "Write a paragraph about cookies."}]

# Format the input we will provide to the LLM and load this onto the GPU 
inputs = tokenizer.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)

# Generate the LLM response 
outputs = model.generate(**inputs, max_new_tokens=200)

# Print the provided LLM response
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
```

Once the script has been created, we can then run the script as follows: 
```
python transformers_run_quant.py
```
At the time of running this script, we obtain the following output: 
```text
Cookies are a classic sweet treat that brings joy to people of all ages. Whether you prefer the classic
chocolate chip, the spicy kick of snickerdoodle, or the delicate flavor of shortbread, there's a cookie 
out there for everyone. With a wide range of textures and flavors to choose from, cookies are the perfect 
snack to satisfy your sweet tooth. They can be enjoyed on their own, paired with a glass of cold milk, or 
used as a topping for ice cream or yogurt. Whether you're baking a batch from scratch or grabbing a few 
from the store, cookies are a timeless treat that's sure to put a smile on your face.<|eot_id|>
```

````

`````
:::{tip}
If you are in an interactive session, it is often preferred to stream the content to the terminal, rather than print out the output (e.g. use the `print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))` statement above). This can be done my replacing the `model.generate` function and the proceeding lines with the following:
```python
from transformers import TextStreamer
streamer = TextStreamer(tokenizer)
output = model.generate(**inputs, max_new_tokens=200, streamer=streamer)
```
Once the model begins to generate the output, you will be able to see it appear in the terminal in real time. 
:::
::::