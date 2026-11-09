# Remote VS Code Sessions

For many users the Open OnDemand [VS Code-Server](../open_ondemand/vs_code-server.md) application is sufficient and significantly easier to use. However, some users may prefer to remotely connect their local VS Code to our system. Additionally, remote connection can be needed if you are utilizing extensions that need the newest version of VS Code to function correctly or are only compatible with the official release of VS Code. To ensure minimal disruption to login nodes, remote VS Code sessions cannot be established with our login nodes. Instead, they must be ran on our compute nodes. On this page we provide you with instructions for setting up a remote VS Code session on our compute nodes. 

```{important}
- Remote VS Code Sessions are only available for institutions with ssh access to CURC resources. 
- The instructions created for Windows machines assume that you are utilizing WSL with the Ubuntu distribution. The instructions provided on this page will not work with PowerShell and have not been tested on other shells or distributions available on Windows. We highly recommend that you utilize WSL with the Ubuntu distribution. For instructions on installing WSL with the Ubuntu distribution, please see [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install). 
```

## Setting up Remote VS Code


1. Open a terminal on your local computer.

    ```{note}
    In all subsequent steps you should use this terminal when asked to execute something in your local terminal. 
    ```

    (tabset-ref-terminal)=
    `````{tab-set}
    :sync-group: tabset-terminal
    ````{tab-item} Mac and Linux
    :sync: terminal-access-mac-linux
    On a Mac or Linux system a terminal can be launched by searching for the terminal application. 
    ````
    ````{tab-item} Windows 
    :sync: terminal-access-windows

    Once you have setup WSL with the Ubuntu distribution, you can use any of these options to launch your Ubuntu terminal:

    - Search for and launch the "Ubuntu" application 
    - Launch the WSL application
    - In PowerShell launch directly into WSL: 
        ```
        wsl -d ubuntu --cd ~
        ``` 
    ````
    `````

2. Generate an SSH key on your local machine (allows you to connect to the compute node session).

    ```{tip}
    When creating your SSH key it is recommended that you do not create a passphrase. You can skip the addition of a passphrase by hitting "Enter" when prompted to input a passphrase.  
    ```

    To create an SSH key, you can execute the following from your local terminal:
    ```
    [ralphie@local-machine ~]$ mkdir -p ~/.ssh
    [ralphie@local-machine ~]$ ssh-keygen -t ed25519 -f ~/.ssh/id_hpc_compute
    ```

3. Once your SSH key has been generated, you will need to obtain your public key so that we can add it to the CURC system. To do this, you can output the content of `id_hpc_compute.pub` as follows:
    ```
    [ralphie@local-machine ~]$ cat ~/.ssh/id_hpc_compute.pub
    ```

4. On a CURC login node add the output of `id_hpc_compute.pub` obtained in the previous step to `~/.ssh/authorized_keys` using your favorite editor and execute the following (which will be the directory we use for all VS Code related items):
    ```
    [ralphie@login-ci5 ~]$ mkdir -p /projects/$USER/remote_vscode
    ```

5. On your local machine add the following to the top of `~/.ssh/config`:

    ```{important}
    - Make sure to replace `<CURC username>` with your CU Research Computing username. 
    - On Windows make sure you are editing the config file associated with your WSL user.
    ```

    ```
    Include ~/.ssh/config.d/*
    Host hpc-login
        HostName login.rc.colorado.edu
        User <CURC username>
        PubkeyAuthentication no
        PreferredAuthentications keyboard-interactive,password
        ControlMaster auto
        ControlPath ~/.ssh/cm-%C
        ControlPersist 5m
    ```


6. Add the script `connect-remote-vscode.sh` (provided in the dropdown below) to your local machine. This script automates the launching of the remote VS Code session. 

    ```{tip}
    We recommend that you add `connect-remote-vscode.sh` to your home directory i.e. the path `~/connect-remote-vscode.sh`
    ```

    ::::{dropdown} Show `connect-remote-vscode.sh` script
    :icon: note

    ```
    #!/usr/bin/env bash
    set -euo pipefail

    # Validate arguments.
    if [[ $# -ne 2 ]]; then
        echo "Usage: $(basename "$0") <CURC username> <compute-node>" >&2
        exit 1
    fi

    curc_username="$1"
    node="$2"

    # SSH configuration.
    ssh_dir="$HOME/.ssh"
    config_dir="$ssh_dir/config.d"
    config_file="$config_dir/hpc-vscode"

    mkdir -p "$config_dir"
    chmod 700 "$config_dir"

    # Create temporary configuration for atomic replacement.
    tmp=$(mktemp "$config_dir/.hpc-vscode.XXXXXX")
    trap 'rm -f "$tmp"' EXIT

    cat > "$tmp" <<EOF
    Host hpc-compute
        StrictHostKeyChecking accept-new
        HostName $node
        User $curc_username
        ProxyJump hpc-login
        IdentityFile ~/.ssh/id_hpc_compute
        IdentitiesOnly yes
    EOF

    chmod 600 "$tmp"
    mv -f "$tmp" "$config_file"

    echo "Compute node: $node"
    echo "SSH alias:    hpc-compute"

    # Ensure VS Code CLI is available.
    if ! command -v code >/dev/null 2>&1; then
        echo "ERROR: VS Code CLI ('code') not found in PATH." >&2
        exit 1
    fi

    # Authenticate to the login node before launching VS Code.
    echo "Authenticating to HPC login node..."
    ssh hpc-login true

    # Verify that the multiplexed connection is active.
    if ! ssh -O check hpc-login >/dev/null 2>&1; then
        echo "ERROR: SSH multiplexed connection is not active." >&2
        exit 1
    fi

    # Launch VS Code using the existing SSH connection.
    echo "Launching VS Code on $node..."
    code --new-window --remote ssh-remote+hpc-compute
    ```
    ::::

7. To enable ease of use, we recommend making the `connect-remote-vscode.sh` script executable. To make the script executable, you can execute the following in your local machine's terminal (this assumes that the script is in the path `~/connect-remote-vscode.sh`):
    ```
    [ralphie@local-machine ~]$ chmod +x ~/connect-remote-vscode.sh
    ```

8. Install VS Code locally, if you haven't already using the [Download Visual Studio Code](https://code.visualstudio.com/download) page. 

9. Install VS Code's `code` command line interface (CLI) on your local machine. This CLI is used within our script `connect-remote-vscode.sh`.

    (tabset-ref-code-cli)=
    `````{tab-set}
    :sync-group: tabset-code-cli
    ````{tab-item} Mac and Linux
    :sync: code-cli-mac-linux

    On a Mac or Linux system you will likely need to install the code CLI. This can be done as follows:

    1. Open Visual Studio Code.
    2. Open the "Command Palette" 
        - On Mac this can typically be done with Cmd + Shift + P
        - On Linux this can typically be done with Ctrl + Shift + P
    3. Search for and select `Shell Command: Install 'code' command in PATH`.
    4. Restart your terminal session
    5. Verify the installation of the `code` CLI by executing the following in your terminal (which should show the version of `code` you have installed):
        ```
        code --version
        ```

    ````

    ````{tab-item} Windows 
    :sync: code-cli-windows

    For Windows machines the `code` CLI should have been automatically installed when you installed VS Code. To verify that it is installed, execute the following in your terminal (which should show the version of `code` you have installed):
    ```
    code --version
    ```

    ````
    `````

10. Install the `Remote - SSH` VS Code extension in your local VS Code. This must be installed in addition to the code CLI and is not installed by default. 

11. Add necessary `Remote - SSH` settings in VS Code using the following steps:

    (tabset-ref-remote-ssh)=
    `````{tab-set}
    :sync-group: tabset-remote-ssh
    ````{tab-item} Mac and Linux
    :sync: remote-ssh-mac-linux

    1. Open VS Code.
    2. Open the "Command Palette" in VS Code. This can typically be done using `Cmd + Shift + P` or `Ctrl + Shift + P`.
    3. Search for `Preferences: Open User Settings (JSON)` and select it.
    4. Add the following settings to your JSON:
        ```{important}
        - Make sure to replace `<CURC username>` with your CU Research Computing username.
        - Do not remove existing settings, unless they conflict with the ones provided.
        - If JSON settings exist, make sure to add a comma where appropriate.
        - If you have no JSON settings, make sure to surround the following with `{}`.
        ```
        ```
        "remote.SSH.serverInstallPath": {"hpc-compute": "/projects/<CURC username>/remote_vscode"},
        "remote.SSH.showLoginTerminal": true,
        "remote.SSH.useLocalServer": false,
        "remote.SSH.remotePlatform": {"hpc-compute": "linux"},
        ```
        For example, say you have the following JSON for your settings: 
        ```
        {
            "workbench.colorTheme": "Dark+",
            "files.autoSave": "afterDelay",
            "chat.disableAIFeatures": true
        }
        ```
        We would add the items as follows:
        ```
        {
            "workbench.colorTheme": "Dark+",
            "files.autoSave": "afterDelay",
            "chat.disableAIFeatures": true,
            "remote.SSH.serverInstallPath": {"hpc-compute": "/projects/<CURC username>/remote_vscode"},
            "remote.SSH.showLoginTerminal": true,
            "remote.SSH.useLocalServer": false,
            "remote.SSH.remotePlatform": {"hpc-compute": "linux"},
        }
        ```
    5. Make sure to save these settings, if you do not have automatic save on.
   

    ````

    ````{tab-item} Windows 
    :sync: remote-ssh-windows

    1. Create the file `~/ssh.bat` in WSL and add the following content
        ```
        @echo off
        C:\Windows\System32\wsl.exe -d Ubuntu --exec /usr/bin/ssh %*
        ```
    2. Open VS Code.
    3. Open the "Command Palette" in VS Code. This can typically be done using `Ctrl + Shift + P`.
    4. Search for `Preferences: Open User Settings (JSON)` and select it.
    5. Add the following settings to your JSON:
        ```{important}
        - Make sure to replace `<CURC username>` with your CU Research Computing username.
        - Make sure to replace `<WSL username>` with your username as it is displayed in the WSL terminal.
        - Do not remove existing settings, unless they conflict with the ones provided.
        - If JSON settings exist, make sure to add a comma where appropriate.
        - If you have no JSON settings, make sure to surround the following with `{}`.
        ```
        ```
        "remote.SSH.path": "\\\\wsl.localhost\\Ubuntu\\home\\<WSL username>\\ssh.bat",
        "remote.SSH.serverInstallPath": {"hpc-compute": "/projects/<CURC username>/remote_vscode"},
        "remote.SSH.showLoginTerminal": true,
        "remote.SSH.useLocalServer": false,
        "remote.SSH.enableDynamicForwarding": false,
        "remote.SSH.remotePlatform": {"hpc-compute": "linux"},
        ```
        For example, say you have the following JSON for your settings: 
        ```
        {
            "workbench.colorTheme": "Dark+",
            "files.autoSave": "afterDelay",
            "chat.disableAIFeatures": true
        }
        ```
        We would add the items as follows:
        ```
        {
            "workbench.colorTheme": "Dark+",
            "files.autoSave": "afterDelay",
            "chat.disableAIFeatures": true,
            "remote.SSH.path": "C:\\Users\\<WSL username>\\ssh.bat",
            "remote.SSH.serverInstallPath": {"hpc-compute": "/projects/<CURC username>/remote_vscode"},
            "remote.SSH.showLoginTerminal": true,
            "remote.SSH.useLocalServer": false,
            "remote.SSH.enableDynamicForwarding": false,
            "remote.SSH.remotePlatform": {"hpc-compute": "linux"},
        }
        ```
    5. Make sure to save these settings, if you do not have automatic save on.


    ````
    `````





    


## Launching Remote VS Code Session

1. On a CURC login node launch a job (the compute node provided is where our remote VS Code session will run):

    TODO: do we want to create a helper script for folks i.e. `remote-vscode` below?
    ```
    [ralphie@login-ci5 ~]$ remote-vscode
    Submitting job for remote VS Code session ...
    salloc: Granted job allocation 35110350
    salloc: Nodes c3cpu-c15-u34-1 are ready for job
    ```
    ````{tip}
    If you want to submit to non-standard compute resources you can use use `salloc --no-shell`, rather than `remote-vscode` e.g. 
    ```
    salloc --no-shell <Slurm directives>
    ```
    ````

    ```{note}
    Make special note of the compute node your job launched on e.g. `c3cpu-c15-u34-1` in the example above. 
    ```

2. On your local computer execute `connect-remote-vscode.sh` using your CURC username and the compute node your job launched on e.g. 
    ```
    [ralphie@local-machine ~]$ ~/connect-remote-vscode.sh ralphie c3cpu-c15-u34-1
    ```

3. After execution of step 2. you will see that a new VS Code window opens up. In this new window you will see in the terminal of the VS Code session that you are prompted for a password. Authenticate through the regular means. 

4. Once authentication is successful you will see VS Code setting up the remote connection.
    ```{tip}
    VS Code needs to setup the remote connection and the environment associated with the remote session. This process can take quite awhile when you first execute this launch. Subsequent sessions should be significantly faster. 

    - You will know the remote session is being setup when you see "Opening Remote ..." in the lower left corner.
    - The remote session has been connected when you see "SSH: hpc-compute" in the lower left corner. 

    ```

5. Once you see "SSH: hpc-compute" in the lower left corner you are all set! You can begin navigating the CURC filesystem within your remote VS Code session.

    ```{warning}
    When the job you created in step 1 finishes, your remote connection will disconnect. If this happens and you would still like to be connected to VS Code remotely, simply close VS Code and repeat the steps in this section.   
    ```