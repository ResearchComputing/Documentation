import subprocess
import shlex
import sys
from collections import defaultdict
import re
import pandas as pd 

def run_slurm_command(command):
    """Runs a Slurm command and returns its stdout."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        return result.stdout.strip()
    except FileNotFoundError:
        print(f"Error: Command not found. Is Slurm installed and in PATH?", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}", file=sys.stderr)
        print(f"Return Code: {e.returncode}", file=sys.stderr)
        print(f"Stderr: {e.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred running command '{command}': {e}", file=sys.stderr)
        sys.exit(1)

def get_all_node_names():
    """Gets a list of unique node names from Slurm."""
    print("Fetching unique node list...")
    command = "sinfo -N -h -o '%N' | sort -u"
    output = run_slurm_command(command)
    node_list = output.splitlines()
    print(f"Found {len(node_list)} unique nodes.")
    return node_list

def get_all_partition_names():
    """Gets a list of unique partition names from Slurm."""
    command = "sinfo -h -o '%P' | sort -u"
    output = run_slurm_command(command)
    partition_list = output.splitlines()
    return partition_list

def get_num_nodes_partition(partition_name):
    """Gets the number of nodes in a particular partition from Slurm."""
    command = f"sinfo -N -p {partition_name} -h -o '%N' | sort -u | wc -l"
    output = run_slurm_command(command)
    return output

def get_node_details(node_name):
    """Gets the AVAILABLE features and CPUTot for a specific node using scontrol."""
    command_args = ["scontrol", "show", "node", node_name]
    features_tuple = tuple() # Default to empty tuple for features
    cpu_tot = None          # Default to None for CPU count

    try:
        result = subprocess.run(
            command_args,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        output = result.stdout

        # Parse the output for both AvailableFeatures and CPUTot
        for line in output.splitlines():
            line = line.strip()
            parts = line.split() # Split line into words based on spaces

            # Check for AvailableFeatures=
            for part in parts:
                 if part.startswith("AvailableFeatures="):
                     features_str = part.split("=", 1)[1]
                     if features_str and features_str != "(null)":
                         features_list = [f for f in re.split(r'[,\s]+', features_str) if f]
                         features_tuple = tuple(sorted(features_list))

            # Check for CPUTot=
            for part in parts:
                if part.startswith("CPUTot="):
                    try:
                        cpu_tot = int(part.split("=", 1)[1])
                    except (ValueError, IndexError):
                        print(f"Warning: Could not parse CPUTot value from '{part}' for node {node_name}", file=sys.stderr)
                        cpu_tot = -1 # Indicate parsing error

        if cpu_tot is None:
             print(f"Warning: Could not find 'CPUTot=' for node {node_name}", file=sys.stderr)
             cpu_tot = -1 # Indicate not found

        return features_tuple, cpu_tot

    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to get info for node {node_name}.", file=sys.stderr)
        print(f"  Command: {' '.join(command_args)}", file=sys.stderr)
        print(f"  Stderr: {e.stderr.strip()}", file=sys.stderr)
        return None, None # Indicate failure for both
    except Exception as e:
        print(f"An unexpected error occurred getting details for node '{node_name}': {e}", file=sys.stderr)
        return None, None # Indicate failure for both


def group_nodes_by_feature(node_list):
    """
    Groups nodes by features and collects CPUTot.
    Returns a dict where keys are feature tuples and values are lists of
    (node_name, cpu_count) tuples.
    """
    nodes_by_feature = defaultdict(list)
    total_nodes = len(node_list)

    print("Querying details (Features, CPUTot) for each node (this may take a while)...")
    for i, node_name in enumerate(node_list):
        print(f"  Processing node {i+1}/{total_nodes}: {node_name}...", end='\r')
        features_tuple, cpu_count = get_node_details(node_name)

        if features_tuple is not None: # Check if feature retrieval succeeded (implicitly checks cpu_count too)
            nodes_by_feature[features_tuple].append((node_name, cpu_count))
        else:
             # Append node to error group, use a placeholder for cpu_count
             nodes_by_feature[("ERROR_RETRIEVING",)].append((node_name, None))

    print("\nFinished querying node details.")
    return dict(nodes_by_feature)