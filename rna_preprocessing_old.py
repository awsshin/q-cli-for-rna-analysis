import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def process_rna_data(file_path):
    data = pd.read_csv(file_path, sep='\t', index_col=0)
    
    filtered_data = data[data.sum(axis=1) > 10]
    filtered_data = filtered_data[filtered_data.sum(axis=1) > 10]
    
    normalized_data = pd.DataFrame()
    for col in filtered_data.columns:
        total = filtered_data[col].sum()
        normalized_data[col] = (filtered_data[col] / total) * 1000000
    
    log_data = np.log2(normalized_data + 1)
    
    mean_values = []
    std_values = []
    for col in log_data.columns:
        mean_values.append(log_data[col].mean())
        std_values.append(log_data[col].std())
    
    stats_df = pd.DataFrame({
        'sample': log_data.columns,
        'mean': mean_values,
        'std': std_values
    })
    
    plt.figure(figsize=(10, 6))
    plt.boxplot([log_data[col] for col in log_data.columns])
    plt.xticks(range(1, len(log_data.columns) + 1), log_data.columns, rotation=45)
    plt.title('RNA Expression Distribution')
    plt.ylabel('Log2(CPM + 1)')
    plt.tight_layout()
    plt.savefig('rna_boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return log_data, stats_df

if __name__ == "__main__":
    result_data, stats = process_rna_data('/path/to/rna_counts.txt')
    print("Processing completed")
    print(stats.head())
