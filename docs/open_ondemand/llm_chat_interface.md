# LLM Chat Interface

The **LLM Chat Interface** is an interactive Open OnDemand application that provides a browser-based chat experience to support a variety of [use cases](#use-cases). It is powered by [Chainlit](https://docs.chainlit.io) and [Ollama](https://ollama.com). When you launch a session, the application starts an Ollama server on a GPU-equipped compute node and connects it to CURC-hosted large language models (LLMs). You can ask questions, draft and debug code, summarize documents, and analyze images (with vision-capable models), all from your web browser. 

```{important}
The LLM Chat Interface is currently offered as a beta service. Functionality, available models, and resource allocations may change as we gather feedback and refine the service. Please report issues or make suggestions through the [CURC support form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form).
```

## Launching the LLM Chat Interface

1. Log in to [Open OnDemand](https://curc.readthedocs.io/en/latest/open_ondemand/index.html) using your CURC credentials.
2. Navigate to either the **Interactive Apps** drop-down menu or the **My Interactive Sessions** tab and select **LLM Chat Interface**.
3. Review the launch form fields:

   - Ollama model path: Select which model library Ollama should load. The default **CURC LLM Models** uses CURC-hosted Ollama models. You may also provide the **absolute path** to your own Ollama model directory, if you have downloaded or fine-tuned models there. See [Ollama documentation](../ai-ml/llms.md#ollama) for more details.
   - Configuration type: 
      - If you selected **Preset configuration** (recommended for most users), choose **10 cores, 1 GPU, 1 hour**. This submits your job to the `a100 testing` partition with one GPU, which is required to run the LLM backend
      - If you selected **Custom configuration**, you **must** request at least one GPU in the **gres** field (for example, `gpu:1:a100_3g.20gb`). See the [Limitations](#limitations) section for guidance on GPU memory (VRAM) and model size. For details on custom configuration options, see [Configuring Open OnDemand interactive applications](./configuring_apps.md).

4. Click **Launch** and wait for your session to start. When the job is ready, click **Connect to LLM Chat Interface** to open the chat in a new browser tab.

```{important}
When a session is launched with Preset configuration, the job is submitted to Alpine testing hardware (`aa100` partition and `gpu-testing` QoS). Testing resources are shared and limited in capacity, so sessions may queue during high demand. For longer runtimes or heavier workloads, use Custom configuration and request appropriate resources (jobs will be subject to queue waits and may not start immediately).
```

## Getting started

Once you click **Connect to LLM Chat Interface**, you land on the welcome screen. 

### Chat history

Chat history is saved per user under `/projects` directory, so you can resume past conversations from the sidebar. Conversation data is stored at:

```
/projects/<your_username>/.chainlit_data
```

### Model selection

Available models are loaded dynamically from the Ollama server when your session starts. To switch models:

1. Open the **model selector** in the application header (labeled with the current model name).
2. Browse the list of **Chat Profiles**. Each entry shows:
   - The model name
   - Capability tags such as **Chat** or **Vision**
   - Parameter size and quantization level
3. Select a model. **New messages** in the current thread use the newly selected model. When you resume an older thread from the sidebar, the model saved with that thread is used.

```{tip}
Choose a smaller, chat-focused model for quick questions and code snippets. Switch to a vision model only when you need to analyze images, since vision models typically require more GPU memory and may respond more slowly.
```

### Message actions

After each assistant reply, action buttons may appear:

| Action | Description |
| --- | --- |
| Regenerate | Ask the model to produce a new reply to your last message. |
| Copy code block | Copy the first fenced code block from the reply to your clipboard. |
| New chat | Clear the current conversation and return to the welcome screen. |
| Switch to vision model | Switch to a vision-capable model (shown when the current model does not support images). |

### Attaching files, text, and images

Browser-based file upload is **disabled** in this application. Files must already exist on CURC filesystems. To attach a file, you **must** use the `/file` command followed by the file's **absolute path**. This keeps data on cluster storage and avoids uploading large files through the web interface.

#### How to attach files

**Every attachment must start with `/file`.** When your prompt includes a file, structure your message as follows:

1. **First line:** `/file` followed by one or more absolute file paths (space-separated for multiple files).
2. **Following lines:** Your question or instruction to the model.

##### Example 1

```
/file /projects/$USER/data/results.csv
What trends do you see in this file?
```

##### Example 2: Multiple files upload

```
/file /projects/$USER/my_report.pdf /projects/$USER/script.py
Summarize the report and check whether the script implements the methods described.
```

If you send `/file` with paths but no follow-up question, the assistant is asked to analyze the attached file(s) by default.

```{important}
Do **not** paste a bare filesystem path without the `/file` prefix, as the assistant will not attach the file. When files are attached successfully, the assistant displays a confirmation as such **File attached from Alpine filesystem**.
```

#### Allowed locations

Attachments must be absolute paths under one of these:

- `/home/$USER/document.txt` 
- `/projects/$USER/myfile.pdf` 
- `/scratch/alpine/$USER/output.log` 
- `/pl/active/<allocation_name>/data.csv`

#### Supported file types

| Type | Extensions / formats | Notes |
| --- | --- | --- |
| **Text and code** | `.py`, `.js`, `.ts`, `.html`, `.css`, `.json`, `.yaml`, `.md`, `.sh`, `.r`, `.sql`, `.csv`, and many others | Full file contents are injected into the prompt. |
| **Plain text** | `.txt`, `.md`, `.rst` | Same as above. |
| **PDF** | `.pdf` | Text is extracted automatically. Scanned or image-only PDFs may not yield text (see [Limitations](#limitations)). |
| **Images** | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`, `.tif`, `.tiff` | Requires a **Vision** model. |

#### Attachment limits

| Limit | Value |
| --- | --- |
| Maximum files per message | 20 |
| Maximum file size | 500 MB per file |
| Maximum PDF text extracted | 120,000 characters per PDF (longer documents are truncated) |

## Limitations

### GPU memory (VRAM) and model size

Every LLM Chat Interface session runs on **GPU hardware**. The preset configuration requests **one GPU**. Custom configurations also **require** at least one GPU in **gres**.

Large language models load into GPU video memory (VRAM). Important constraints:

- **Larger models use more VRAM.** A model's parameter size (shown in the model selector) is a rough guide: multi-billion-parameter models need substantially more memory than smaller ones.
- **Only one GPU is allocated by default in custom configuration.** Very large models may fail to load, run slowly, or return errors if they exceed available VRAM on the assigned node.
- **Vision models and long contexts increase memory pressure.** Attaching images, long PDFs, or maintaining a long conversation history all consume context window space and can contribute to out-of-memory failures or empty responses.

```{important}
This assistant was **not** trained on [CU Research Computing (CURC) documentation](https://curc.readthedocs.io). It does **not** have reliable, up-to-date knowledge of CURC-specific systems, policies, or procedures. The model may produce plausible-sounding but **incorrect** answers for system specific topics. **Always verify** CURC-specific information against official documentation.
```

### Other limitations

- **Context window.** The backend uses a large but finite context window (32,768 tokens). Extremely long files, many attachments, or very long threads may be truncated or cause degraded responses.
- **Not for sensitive or regulated data.** Do not paste export-controlled, HIPAA, or other restricted data into the chat. Treat prompts and attachments as you would any shared compute resource.
- **Resuming old threads** reloads conversation text but does not re-inject large files from previous conversations; re-attach the files if you need the model to see them again.


## Use cases

* Ask general coding questions
```
Write a short Python function that reads a CSV and computes column means.
```

* Summarizing and questioning documents
```
/file /projects/$USER/papers/methods_supplement.pdf
List the experimental parameters in a table and note anything ambiguous.
```
* Image and plot reviews
```
/file /projects/$USER/figures/confusion_matrix.png
Is this figure publication-ready? Suggest axis labels and caption text.
```
* Deploying custom-trained or fine-tuned models that can answer questions about your lab's protocols, instrumentation, research methods, and internal documentation.
