# Launching Remote VS Code Sessions


Blah Blah utility of doing this 

```{important}
Only available for institutions with ssh access to CURC resources. 
```


```{note}
Go back through this and be more descriptive on items. Will likely need to come up with accompanying Windows instructions via tabs.
```

## Setting up Remote VS Code


1. Generate an ssh key on your local machine (allows you to connect to the compute node session)

(tabset-ref-ssh-keygen)=
`````{tab-set}
:sync-group: tabset-terminal-access


````{tab-item} Mac and Linux
:sync: terminal-access-mac-linux

```
ssh-keygen -t ed25519 -f ~/.ssh/id_hpc_compute
```

````

````{tab-item} Windows 
:sync: terminal-access-windows

Gross why would you use Windows...

````

`````

2. On a CURC login node add `id_hpc_compute.pub` to `authorized_keys` and execute:
```
mkdir /projects/$USER/remote_vscode
```

3. On your local machine add the following to `~/.ssh/config`:
```{important}
```
Make sure to replace `<CURC username>` with your CU Research Computing username
```
Host hpc-login
    HostName login.rc.colorado.edu
    User <CURC username>
    PubkeyAuthentication no
    PreferredAuthentications keyboard-interactive,password
    ControlMaster auto
    ControlPath ~/.ssh/cm-%C
    ControlPersist 5m
```

4. Add the following to the top of `~/.ssh/config`
```
Include ~/.ssh/config.d/*
```

5. Add the script `connect-remote-vscode.sh` to automatically connect you to the node session you already have established:
```{note}
TODO: instructions for adding this to your path
```

```
#!/usr/bin/env bash
set -euo pipefail

# Validate arguments.
if [[ $# -ne 1 ]]; then
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
code --remote ssh-remote+hpc-compute
```

6. Install `code` cli locally
    a. Open Visual Studio Code.
    b. Open the Command Palette with Cmd + Shift + P.
    c. Search for and select `Shell Command: Install 'code' command in PATH`.
    d. Restart iTerm2 (or open a new terminal session).
    e. Verify the installation of the `code` CLI by executing the following in your command line:
        ```
        code --version
        ```

7. Add the Remote-SSH settings in VS Code:
    a. Open VS Code.
    b. Press Cmd + Shift + P to open the Command Palette.
    c. Search for Preferences: Open User Settings (JSON) and select it.
    d. Add the following settings (do not remove existing settings):
        ```{important}
        Make sure to replace `<CURC username>` with your CU Research Computing username
        ```
        ```"remote.SSH.serverInstallPath": {    
                "hpc-compute": "/projects/<CURC username>/remote_vscode"
            },
            "remote.SSH.showLoginTerminal": true,
            "remote.SSH.useLocalServer": false,
        ```
    e. Make sure to save these settings, if you do not have automatic save on.


## Launching Remote VS Code Session

1. On a CURC login node launch a job:
```
[ralphie@login-ci5 ~]$ remote-vscode
Submitting job for remote VS Code session ...
salloc: Granted job allocation 35110350
salloc: Nodes c3cpu-c15-u34-1 are ready for job
```
```{note}
Make special note of the compute node your job launched on e.g. `c3cpu-c15-u34-1` in the example above. 
```

2. On your local computer execute `connect-remote-vscode.sh` using your CURC username and the compute node your job launched on e.g. 
```
[ralphie@local-machine ~]$ ./connect-remote-vscode.sh ralphie c3cpu-c15-u34-1
```

3. After execution of step 2. you will see that a new VS Code window opens up. In this new window you will see in the terminal of the VS Code session that you are prompted for a password. Authenticate through the regular means. 

4. Once authentication is successful you will see VS Code setting up the remote connection.

5. Congrats, you did it champ!







