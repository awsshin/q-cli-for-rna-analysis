#!/usr/bin/env python3
"""
Legacy RNA Analysis Pipeline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

class LegacyRNAAnalysisPipeline:
    def __init__(self):
        self.normalization_method = "simple_cpm"
        self.min_count_threshold = 5
        self.min_samples_expressed = 2
        self.statistical_test = "t_test"
        
        self.housekeeping_genes = [
            "ENSG00000075624",
            "ENSG00000111640",
            "ENSG00000089157"
        ]
        
        self.pathway_database_version = "KEGG_2018"
    
    def load_count_matrix(self, file_path):
        """Count matrix 로딩"""
        print("Loading count matrix...")
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        header = lines[0].strip().split('\t')
        data_dict = {col: [] for col in header[1:]}
        gene_ids = []
        
        for line in lines[1:]:
            parts = line.strip().split('\t')
            gene_ids.append(parts[0])
            for i, value in enumerate(parts[1:]):
                data_dict[header[i+1]].append(float(value))
        
        df = pd.DataFrame(data_dict, index=gene_ids)
        return df
    
    def filter_low_expression_genes(self, count_matrix):
        """유전자 필터링"""
        print(f"Filtering genes with criteria: min_count={self.min_count_threshold}")
        
        expressed_samples = (count_matrix >= self.min_count_threshold).sum(axis=1)
        filtered_genes = expressed_samples >= self.min_samples_expressed
        
        filtered_matrix = count_matrix[filtered_genes]
        print(f"Retained {len(filtered_matrix)} genes after filtering")
        
        return filtered_matrix
    
    def normalize_expression(self, count_matrix):
        """발현 정규화"""
        print(f"Normalizing using method: {self.normalization_method}")
        
        if self.normalization_method == "simple_cpm":
            library_sizes = count_matrix.sum(axis=0)
            cpm_matrix = count_matrix.div(library_sizes, axis=1) * 1e6
            
            log_cpm = np.log2(cpm_matrix + 1)
            
            return log_cpm
    
    def quality_control_analysis(self, normalized_matrix):
        """품질 관리 분석"""
        print("Performing quality control analysis...")
        
        qc_metrics = {}
        
        for sample in normalized_matrix.columns:
            sample_data = normalized_matrix[sample]
            
            qc_metrics[sample] = {
                'total_detected_genes': (sample_data > 0).sum(),
                'mean_expression': sample_data.mean(),
                'median_expression': sample_data.median(),
                'housekeeping_expression': sample_data[
                    sample_data.index.isin(self.housekeeping_genes)
                ].mean() if any(sample_data.index.isin(self.housekeeping_genes)) else np.nan
            }
        
        qc_df = pd.DataFrame(qc_metrics).T
        return qc_df
    
    def perform_pca_analysis(self, normalized_matrix):
        """PCA 분석"""
        print("Performing PCA analysis...")
        
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(normalized_matrix.T)
        
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(scaled_data)
        
        pca_df = pd.DataFrame(
            pca_result,
            columns=['PC1', 'PC2'],
            index=normalized_matrix.columns
        )
        
        explained_variance = pca.explained_variance_ratio_
        
        return pca_df, explained_variance
    
    def differential_expression_legacy(self, normalized_matrix, group1_samples, group2_samples):
        """차등 발현 분석"""
        print(f"Performing differential expression using {self.statistical_test}")
        
        results = []
        
        for gene in normalized_matrix.index:
            group1_values = normalized_matrix.loc[gene, group1_samples].values
            group2_values = normalized_matrix.loc[gene, group2_samples].values
            
            from scipy.stats import ttest_ind
            t_stat, p_value = ttest_ind(group1_values, group2_values)
            
            mean1 = np.mean(group1_values)
            mean2 = np.mean(group2_values)
            
            if mean2 > 0:
                fold_change = mean1 / mean2
            else:
                fold_change = np.inf
            
            results.append({
                'gene_id': gene,
                'group1_mean': mean1,
                'group2_mean': mean2,
                'fold_change': fold_change,
                'log2_fold_change': np.log2(fold_change) if fold_change > 0 else np.nan,
                'p_value': p_value,
                't_statistic': t_stat
            })
        
        de_df = pd.DataFrame(results)
        
        de_df['p_adjusted'] = de_df['p_value'] * len(de_df)
        de_df['p_adjusted'] = de_df['p_adjusted'].clip(upper=1.0)
        
        return de_df
    
    def generate_legacy_plots(self, pca_df, explained_variance, output_dir="./"):
        """플롯 생성"""
        print("Generating plots...")
        
        plt.figure(figsize=(8, 6))
        plt.scatter(pca_df['PC1'], pca_df['PC2'], alpha=0.7)
        
        for i, sample in enumerate(pca_df.index):
            plt.annotate(sample, (pca_df.iloc[i, 0], pca_df.iloc[i, 1]))
        
        plt.xlabel(f'PC1 ({explained_variance[0]:.1%} variance)')
        plt.ylabel(f'PC2 ({explained_variance[1]:.1%} variance)')
        plt.title('PCA Analysis')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f"{output_dir}/pca_plot.png", dpi=150)
        plt.close()
        
        print(f"PCA plot saved to {output_dir}/pca_plot.png")

# 사용 예시
def run_legacy_pipeline():
    """파이프라인 실행"""
    pipeline = LegacyRNAAnalysisPipeline()
    
    np.random.seed(42)
    sample_count_matrix = pd.DataFrame(
        np.random.poisson(50, (1000, 8)),
        columns=[f'Sample_{i+1}' for i in range(8)],
        index=[f'ENSG{i:08d}' for i in range(1000)]
    )
    
    print("=== RNA Analysis Pipeline ===")
    
    filtered_matrix = pipeline.filter_low_expression_genes(sample_count_matrix)
    normalized_matrix = pipeline.normalize_expression(filtered_matrix)
    qc_results = pipeline.quality_control_analysis(normalized_matrix)
    pca_results, variance = pipeline.perform_pca_analysis(normalized_matrix)
    
    print("\nQuality Control Results:")
    print(qc_results.head())
    
    print(f"\nPCA Results - PC1: {variance[0]:.1%}, PC2: {variance[1]:.1%}")
    
    group1 = ['Sample_1', 'Sample_2', 'Sample_3', 'Sample_4']
    group2 = ['Sample_5', 'Sample_6', 'Sample_7', 'Sample_8']
    
    de_results = pipeline.differential_expression_legacy(normalized_matrix, group1, group2)
    significant_genes = de_results[de_results['p_adjusted'] < 0.05]
    
    print(f"\nFound {len(significant_genes)} significantly differentially expressed genes")
    print("Top 5 significant genes:")
    print(significant_genes.nsmallest(5, 'p_adjusted')[['gene_id', 'log2_fold_change', 'p_adjusted']])
    
    pipeline.generate_legacy_plots(pca_results, variance)

if __name__ == "__main__":
    run_legacy_pipeline()
