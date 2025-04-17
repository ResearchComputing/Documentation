from node_counter import * 
import numpy as np 


all_nodes = get_all_node_names()

if not all_nodes:
    print("No nodes found or error fetching node list. Exiting.", file=sys.stderr)
    sys.exit(1)

grouped_nodes_dict = group_nodes_by_feature(all_nodes)

# Prepare data for DataFrame
data_for_df = []
for feature_set, node_data_list in grouped_nodes_dict.items():
    # Create feature string representation
    if feature_set == ("ERROR_RETRIEVING",):
         feature_str = "ERROR_RETRIEVING_DETAILS"
    elif not feature_set:
         feature_str = "NO_FEATURES"
    else:
         feature_str = ",".join(feature_set)

    # Iterate through the list of (node_name, cpu_count) tuples
    for node_name, cpu_count in node_data_list:
        data_for_df.append({
            "NodeName": node_name,
            "Features": feature_str,
            "CPUTot": cpu_count  # Add the CPU count here
        })

if not data_for_df:
    print("No node data could be processed to put into DataFrame.")
else:
    # Create DataFrame
    nodes_df = pd.DataFrame(data_for_df)

    # Optional: Sort DataFrame by NodeName
    nodes_df = nodes_df.sort_values(by="NodeName").reset_index(drop=True)


# Categorize by institution
conditions = [
    nodes_df['Features'].str.contains('csu', na=False, case=True),   # Highest priority
    nodes_df['Features'].str.contains('amc', na=False, case=True),   # Next priority
    nodes_df['Features'].str.contains('rmacc', na=False, case=True) # Lowest priority among targets
]

# Define the corresponding choices for each condition
choices = ['CSU', 'AMC', 'RMACC']

# Use np.select to create the 'Category' column
# The 'default' argument handles cases where none of the conditions are met
nodes_df['Category'] = np.select(conditions, choices, default='UCB')

grouped_by_category = nodes_df.groupby('Category')

print("\n--- Total number of nodes ---")
print(nodes_df['CPUTot'].value_counts(dropna=False).sum())

print("\n--- Total number of cores ---")
print(nodes_df['CPUTot'].sum())


print("\n \n --- Breaking things down by institution ---")

for category_name, group_df in grouped_by_category:

    print(f"\n--- {category_name} counts ---")

    # Categorize nodes based on their features
    conditions = [
        group_df['Features'].str.contains('cpu', na=False, case=True),  
        group_df['Features'].str.contains('a100', na=False, case=True),  
        group_df['Features'].str.contains('mi100', na=False, case=True),  
        group_df['Features'].str.contains('l40', na=False, case=True), 
        group_df['Features'].str.contains('gh200', na=False, case=True), 
        group_df['Features'].str.contains('himem', na=False, case=True) 
    ]
    
    # Define the corresponding choices for each condition
    choices = ['CPU', 'a100', 'mi100', 'l40', 'gh200', 'himem']

    group_df['hardware_type'] = np.select(conditions, choices, default='Other')

    grouped_by_hardware_type = group_df.groupby('hardware_type')

    total_nodes = 0
    for feature, subgroup_df in grouped_by_hardware_type:

        print(f"    {feature} nodes:")

        temp_dict = dict(subgroup_df['CPUTot'].value_counts(dropna=False))
        for key,val in temp_dict.items():
            print(f"     {val} nodes with {key} cores")
            
        total_nodes_category = subgroup_df['CPUTot'].value_counts(dropna=False).sum()
        total_nodes += total_nodes_category
        print(f"     --> Total of {total_nodes_category} {feature} nodes")
        print("")
    print(f"Total number of nodes contributed by {category_name}: {total_nodes}")
    print("")


print("\n \n --- Breaking things down by partition ---")

partition_names = get_all_partition_names()
for partition_name in partition_names:
    if partition_name == 'amilan*':
       partition_name = 'amilan' 
    num_nodes = get_num_nodes_partition(partition_name)
    print(f"Partition {partition_name} has {num_nodes} nodes")