import pandas as pd
import numpy as np
from scipy import stats

class GeneExpressionAnalyzer:
    def __init__(self):
        self.gene_annotations = {
            'ENSG00000139618': {'symbol': 'BRCA2', 'biotype': 'protein_coding', 'chromosome': '13'},
            'ENSG00000012048': {'symbol': 'BRCA1', 'biotype': 'protein_coding', 'chromosome': '17'},
            'ENSG00000141510': {'symbol': 'TP53', 'biotype': 'protein_coding', 'chromosome': '17'},
            'ENSG00000171862': {'symbol': 'PTEN', 'biotype': 'protein_coding', 'chromosome': '10'},
            'ENSG00000134086': {'symbol': 'VHL', 'biotype': 'protein_coding', 'chromosome': '3'}
        }
        
        self.pathway_info = {
            'DNA_REPAIR': ['ENSG00000139618', 'ENSG00000012048'],
            'TUMOR_SUPPRESSOR': ['ENSG00000141510', 'ENSG00000171862'],
            'CELL_CYCLE': ['ENSG00000141510']
        }
        
        self.expression_thresholds = {
            'low_expression': 1.0,
            'high_expression': 10.0,
            'fold_change_cutoff': 2.0,
            'pvalue_cutoff': 0.05
        }
    
    def load_expression_data(self, file_path):
        """RNA-seq 발현 데이터 로드"""
        try:
            data = pd.read_csv(file_path, sep='\t', index_col=0)
            return data
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_path}")
            return None
    
    def annotate_genes(self, expression_data):
        """유전자에 어노테이션 정보 추가"""
        annotated_data = expression_data.copy()
        
        # 유전자 심볼 추가
        gene_symbols = []
        biotypes = []
        chromosomes = []
        
        for gene_id in expression_data.index:
            if gene_id in self.gene_annotations:
                gene_symbols.append(self.gene_annotations[gene_id]['symbol'])
                biotypes.append(self.gene_annotations[gene_id]['biotype'])
                chromosomes.append(self.gene_annotations[gene_id]['chromosome'])
            else:
                gene_symbols.append('Unknown')
                biotypes.append('Unknown')
                chromosomes.append('Unknown')
        
        annotated_data['gene_symbol'] = gene_symbols
        annotated_data['biotype'] = biotypes
        annotated_data['chromosome'] = chromosomes
        
        return annotated_data
    
    def identify_pathway_genes(self, gene_list):
        """pathway별 유전자 분류"""
        pathway_results = {}
        
        for pathway, genes in self.pathway_info.items():
            pathway_genes = [gene for gene in gene_list if gene in genes]
            pathway_results[pathway] = pathway_genes
        
        return pathway_results
    
    def differential_expression_analysis(self, control_samples, treatment_samples, expression_data):
        """차등 발현 분석"""
        results = []
        
        for gene_id in expression_data.index:
            control_values = expression_data.loc[gene_id, control_samples].values
            treatment_values = expression_data.loc[gene_id, treatment_samples].values
            
            # t-test 수행
            t_stat, p_value = stats.ttest_ind(treatment_values, control_values)
            
            # fold change 계산
            control_mean = np.mean(control_values)
            treatment_mean = np.mean(treatment_values)
            
            if control_mean > 0:
                fold_change = treatment_mean / control_mean
            else:
                fold_change = np.inf
            
            # 유의성 판단
            is_significant = (p_value < self.expression_thresholds['pvalue_cutoff'] and 
                            abs(np.log2(fold_change)) > np.log2(self.expression_thresholds['fold_change_cutoff']))
            
            results.append({
                'gene_id': gene_id,
                'fold_change': fold_change,
                'log2_fold_change': np.log2(fold_change) if fold_change > 0 else np.nan,
                'p_value': p_value,
                'significant': is_significant
            })
        
        return pd.DataFrame(results)

# 사용 예시
if __name__ == "__main__":
    analyzer = GeneExpressionAnalyzer()
    
    # 샘플 데이터 생성 (실제로는 파일에서 로드)
    sample_data = pd.DataFrame({
        'Control_1': [5.2, 3.1, 8.7, 2.4, 6.8],
        'Control_2': [4.8, 2.9, 9.1, 2.1, 7.2],
        'Treatment_1': [8.3, 5.4, 12.1, 1.8, 4.2],
        'Treatment_2': [7.9, 5.8, 11.7, 1.5, 3.9]
    }, index=['ENSG00000139618', 'ENSG00000012048', 'ENSG00000141510', 'ENSG00000171862', 'ENSG00000134086'])
    
    # 분석 실행
    annotated = analyzer.annotate_genes(sample_data)
    print("어노테이션된 데이터:")
    print(annotated.head())
    
    # 차등 발현 분석
    de_results = analyzer.differential_expression_analysis(
        ['Control_1', 'Control_2'], 
        ['Treatment_1', 'Treatment_2'], 
        sample_data
    )
    print("\n차등 발현 분석 결과:")
    print(de_results)
