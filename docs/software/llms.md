# Running Large Language Models Locally 

Large Language Models (LLMs) have become extremely popular. Although LLMs such as ChatGPT and Google's Gemini are extremely useful, there are two primary downsides to using such a service: data privacy and cost. Additionally, it is often the case that more specialized LLMs are needed (rather than large general models) or researchers want to train these models to fit their specialized case. These cases provide a need for running local LLMs. In this section, we provide several approaches for setting up and running open-source LLMs locally on Alpine and Blanca, using popular frameworks. 

```{warning}
Before running or working with LLMs on CURC resources, please be sure that you are adhering to all [CURC User Policies](https://curc.readthedocs.io/en/latest/additional-resources/policies.html) and CU's policies and guidance around Artificial Intelligence outlined at [Artificial Intelligence at CU Boulder](https://www.colorado.edu/information-technology/artificial-intelligence-cu-boulder) and [Resources & Guidance](https://www.colorado.edu/information-technology/ai-cu-boulder/resources-guidance#accordion-1981143711-1). 
```

## Ollama 

[Ollama](https://ollama.com/) is an open-source, lightweight, and extremely beginner friendly tool that enables users to run LLMs locally and retrieve models that are compatible with the system you are running on. Given Ollama is in rapid development, functionality is constantly changing. Additionally, the newest models often require the newest version of Ollama to properly function. For this reason, at the moment, CURC is not providing an Ollama module. Instead, we provide detailed instructions below for installing the version of Ollama that works for your use case. 

### Installing Ollama 
Here is how I grabbed ollama's precompiled binaries:

export ollama_v="v0.2.1"
mkdir -p /projects/$USER/$ollama_v
cd /projects/$USER/$ollama_v

# grab ollama binary version
curl -L https://github.com/ollama/ollama/releases/download/${ollama_v}/ollama-linux-amd64 -o ollama

# make binary executable
chmod +x ollama

Now, you can start up an ollama serve on your Blanca node:

1. Start up an interactive job on your Blanca node
2. Export the following variables (feel free to change):

export PATH=$PATH:/projects/$USER/$ollama_v
export OLLAMA_TMPDIR=$SCRATCHDIR/$USER/ollama_temp
export OLLAMA_HOST=0.0.0.0:9999
export OLLAMA_MODELS=/projects/$USER/my_ollama_models
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1

3. Make your directories, just in case they do not exist

mkdir -p $OLLAMA_TMPDIR
mkdir -p $OLLAMA_MODELS

4. Now start an ollama server in the background

nohup ollama serve > /dev/null 2>&1 &

4. Run ollama!

ollama run llama3:8b


When you do this, you can access it from the terminal. Additionally, when you start the ollama serve you can connect to this from any RC resource using the IP. You can get the IP of your Blanca node by running the command:

hostname -I

Using this IP, you can then connect to the serve using the following (assuming the Blanca node IP is "10.123.45.67")

http://10.123.45.67:9999

If you have any questions or issues, please let me know!