# SRA Toolkit on Alpine

SRA Toolkit provides tools for downloading data, converting data into SRA format, and extracting SRA data into other data formats.

## Loading the Module

From an Alpine compute node:
``` bash
module load sra-toolkit
```

## Configuring SRA Toolkit 

Some SRA Toolkit commands, such as `fasterq-dump`, generate large temporary files that are approximately the size of the final output file(s). SRA Toolkit writes these 
temporary, 
or cache, files to `/home/$USER`. CURC `/home/$USER` is limited to 2 GB, so users must direct this cache somewhere else. We recommend `/scratch/alpine`, since each user has up 
to 10 TB and it is automatically purged every 90 days. 

Users should redirect the cache using SRA Toolkit's `vdb-config -i`. Settings are saved and persist across sessions, so this is only necessary the first time you run SRA 
Toolkit on CURC Alpine.

Before running the configuration command, create an `sra` directory in your scratch space.

``` bash
mkdir /scratch/alpine/$USER/sra
```
This directory must be empty, so don't add anything to it.

Now start the `vdb-config` program.

``` bash
module load sra-toolkit
vdb-config -i
```

A configuration window will open in your terminal, with a set of file operations listed across the top of the window (save, exit, discard, and default). The primary tabs for the configuration window are MAIN, CACHE, AWS, GCP, NET, and TOOLS. The first letter of each file operation and tab is underlined, which indicates the key stroke needed to select each. The configuration window's elements can also be navigated by pressing the `tab` key and then activted by pressing the `enter` key.

```{image} ./software_images/config_window.png
:alt: A screenshot of the sra toolkit configuration terminal window, showing the first option on the MAIN tab has been selected. That option is "Enable Remote Access". The configuration window is described in detail under the header "Configuring SRA Toolkit" 
:align: center
```


Navigate to the CACHE tab using your tab key. Press enter when the red cursor lands on CACHE. Keep pressing tab until the red cursor is on `location of user-repository: [ 
choose ]`. 

```{image} ./software_images/navigating_to_cache_location.png
:alt: A screenshot of the sra toolkit configuration terminal window, showing the first option on the CACHE tab has been enabled, "enable local file-caching", and the active cursor set to "location of user-repository". The configuration window is described in detail under the header "Configuring SRA Toolkit".
:align: center
```

Press enter. A `select directory` window will appear.

```{image} ./software_images/file_navigator.png
:alt: A screenshot of the sra toolkit's file browser, showing a default directory path of "/home/lrf20@xsede.org" and a list of directories that only includes "[..]". On the bottom of the window are options for OK, Cancel, Goto, and Create Dir.
:align: center
```


Tab over to `[ Goto ]` and press enter. A new pop-up window will appear. Delete the existing file path (e.g., `/home/lrf20@xsede.org`) using your delete/backspace key and enter 
the absolute path of your new `sra` cache directory. 

`vdb-config -i` requires your specified directory to exist (it won't create it for you) and be an *empty* directory. You must also have read/write permissions. The program will 
not save your selection if these criteria aren't met. 

```{image} ./software_images/select_new_cache_dir_2.png
:alt: A screenshot of the sra toolkit's file browser, showing a secondary window for the "goto path" configuration. The following path has been entered, "/scratch/alpine/lrf20@xsede.org/sra". The options OK and Cancel are listed at the bottom of the "goto path" window. 
:align: center
```

Tab over to `[ OK ]` and press enter. Confirm the directory listed at the top of the 'select directory' window says `/scratch/alpine/<your username/sra>` Tab over to `[ OK ]` 
and press enter.

```{image} ./software_images/see_new_path.png
:alt: A screenshot of the sra toolkit's file browser, showing a directory path of "/scratch/alpine/lrf20@xsede.org/sra" and a list of directories that only includes "[..]". On the bottom of the window are options for OK, Cancel, Goto, and Create Dir.
:align: center
```

A window asking you to confirm the change will appear. Select `[ yes ]`.

```{image} ./software_images/confirm_new_dir.png
:alt: A screenshot of the sra toolkit configuration terminal window, showing a secondary window to confirm "do you want to change the location to '/scratch/alpine/lrf20@xsede.org/sra'" with the option "yes" selected. The configuration window is described in detail under the header "Configuring SRA Toolkit"
:align: center
```


Tab over to `[ save ]` and press enter. A window will appear telling you the changes have been saved successfully. Select `[ ok ]`.

Tab to `[ exit ]` and press enter.

SRA Toolkit is ready for use!

## Common SRA Toolkit Issues

- Download errors are common with commands like `prefetch`, `fasterq-dump`, and `hisat2`, as the NCBI SRA server can be overwhelmed. 




