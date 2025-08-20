"""
Modern RNA Analysis Methods - 2024 Updated Best Practices
레거시 코드를 업데이트할 때 참고할 현대적인 방법들
"""

# 현대적인 정규화 방법들
MODERN_NORMALIZATION_METHODS = {
    "TMM": {
        "description": "Trimmed Mean of M-values normalization",
        "library": "edgeR",
        "recommended_for": "RNA-seq count data",
        "advantages": ["Robust to outliers", "Accounts for library composition"]
    },
    "DESeq2": {
        "description": "DESeq2 median-of-ratios normalization",
        "library": "DESeq2",
        "recommended_for": "RNA-seq differential expression",
        "advantages": ["Handles low counts well", "Built-in shrinkage estimation"]
    },
    "TPM": {
        "description": "Transcripts Per Million",
        "library": "Various",
        "recommended_for": "Cross-sample comparisons",
        "advantages": ["Length-normalized", "Interpretable units"]
    }
}

# 현대적인 필터링 기준
MODERN_FILTERING_CRITERIA = {
    "min_count_per_sample": 10,  # 이전: 5
    "min_samples_expressed": 0.5,  # 50% of samples (이전: 고정값 2)
    "min_cpm_threshold": 1.0,  # CPM 기준
    "remove_low_variance": True,  # 낮은 분산 유전자 제거
    "variance_percentile": 10  # 하위 10% 분산 유전자 제거
}

# 현대적인 통계 방법들
MODERN_STATISTICAL_METHODS = {
    "differential_expression": {
        "DESeq2": {
            "description": "Negative binomial GLM with shrinkage",
            "advantages": ["Handles overdispersion", "Shrinkage estimation", "Multiple testing correction"],
            "recommended": True
        },
        "edgeR": {
            "description": "Negative binomial GLM with empirical Bayes",
            "advantages": ["Fast computation", "Flexible design matrices", "Robust dispersion estimation"],
            "recommended": True
        },
        "limma-voom": {
            "description": "Linear modeling with precision weights",
            "advantages": ["Fast", "Flexible contrasts", "Good for complex designs"],
            "recommended": True
        }
    },
    "multiple_testing_correction": {
        "BH_FDR": {
            "description": "Benjamini-Hochberg False Discovery Rate",
            "recommended": True,
            "cutoff": 0.05
        },
        "qvalue": {
            "description": "Storey's q-value method",
            "recommended": True,
            "cutoff": 0.05
        }
    }
}

# 현대적인 QC 메트릭들
MODERN_QC_METRICS = {
    "library_size": "Total number of mapped reads",
    "detected_genes": "Number of genes with non-zero counts",
    "mitochondrial_percentage": "Percentage of mitochondrial gene expression",
    "ribosomal_percentage": "Percentage of ribosomal gene expression",
    "complexity": "Library complexity (unique genes / total reads)",
    "gc_content": "GC content bias assessment",
    "duplication_rate": "PCR duplication rate",
    "insert_size_distribution": "Insert size metrics (for paired-end)",
    "strand_specificity": "Strand-specific mapping rates"
}

# 현대적인 차원 축소 방법들
MODERN_DIMENSIONALITY_REDUCTION = {
    "PCA": {
        "description": "Principal Component Analysis",
        "use_case": "Linear dimensionality reduction",
        "parameters": {"n_components": "auto", "scaling": "standard"}
    },
    "t-SNE": {
        "description": "t-distributed Stochastic Neighbor Embedding",
        "use_case": "Non-linear visualization",
        "parameters": {"perplexity": 30, "learning_rate": 200}
    },
    "UMAP": {
        "description": "Uniform Manifold Approximation and Projection",
        "use_case": "Non-linear dimensionality reduction",
        "parameters": {"n_neighbors": 15, "min_dist": 0.1},
        "recommended": True
    }
}

# 현대적인 pathway 분석 방법들
MODERN_PATHWAY_ANALYSIS = {
    "databases": {
        "KEGG_2024": "Latest KEGG pathway database",
        "Reactome_2024": "Reactome pathway database",
        "GO_2024": "Gene Ontology annotations",
        "MSigDB_v2024": "Molecular Signatures Database",
        "WikiPathways_2024": "Community-curated pathways"
    },
    "methods": {
        "GSEA": {
            "description": "Gene Set Enrichment Analysis",
            "advantages": ["Considers all genes", "Accounts for gene ranking"],
            "recommended": True
        },
        "fgsea": {
            "description": "Fast Gene Set Enrichment Analysis",
            "advantages": ["Fast computation", "Accurate p-values"],
            "recommended": True
        },
        "clusterProfiler": {
            "description": "Statistical analysis of functional profiles",
            "advantages": ["Multiple databases", "Visualization tools"],
            "recommended": True
        }
    }
}

# 현대적인 시각화 도구들
MODERN_VISUALIZATION_TOOLS = {
    "interactive_plots": {
        "plotly": "Interactive web-based plots",
        "bokeh": "Interactive visualization library",
        "altair": "Declarative statistical visualization"
    },
    "specialized_plots": {
        "volcano_plot": "Enhanced volcano plots with annotations",
        "ma_plot": "MA plots with density information",
        "heatmap": "Clustered heatmaps with dendrograms",
        "pathway_plots": "Network-based pathway visualization"
    },
    "quality_control": {
        "fastqc_plots": "Sequence quality visualization",
        "alignment_plots": "Mapping statistics visualization",
        "expression_plots": "Expression distribution plots"
    }
}

# 현대적인 하우스키핑 유전자 (2024년 업데이트)
MODERN_HOUSEKEEPING_GENES = {
    "stable_genes": [
        "ENSG00000075624",  # ACTB
        "ENSG00000111640",  # GAPDH
        "ENSG00000089157",  # RPLP0
        "ENSG00000198888",  # MT-ND1
        "ENSG00000198763",  # MT-ND2
        "ENSG00000142541",  # RPL13A
        "ENSG00000089009",  # RPL6
        "ENSG00000108107"   # RPL8
    ],
    "validation_required": True,
    "tissue_specific": True,
    "updated_date": "2024-08-01"
}

# 현대적인 분석 파이프라인 구조
MODERN_PIPELINE_STRUCTURE = {
    "preprocessing": [
        "Quality control assessment",
        "Adapter trimming",
        "Quality filtering",
        "Contamination screening"
    ],
    "alignment": [
        "Reference genome alignment",
        "Splice-aware alignment",
        "Multi-mapping handling",
        "Alignment quality assessment"
    ],
    "quantification": [
        "Gene-level quantification",
        "Transcript-level quantification",
        "Isoform analysis",
        "Novel transcript detection"
    ],
    "normalization": [
        "Library size normalization",
        "Composition bias correction",
        "Batch effect correction",
        "Technical variation removal"
    ],
    "analysis": [
        "Differential expression analysis",
        "Pathway enrichment analysis",
        "Network analysis",
        "Functional annotation"
    ],
    "validation": [
        "qPCR validation",
        "Independent dataset validation",
        "Functional validation",
        "Clinical correlation"
    ]
}

# 현대적인 성능 최적화 방법들
MODERN_PERFORMANCE_OPTIMIZATION = {
    "parallel_processing": {
        "multiprocessing": "CPU parallelization",
        "dask": "Distributed computing",
        "ray": "Scalable machine learning"
    },
    "memory_optimization": {
        "chunking": "Process data in chunks",
        "sparse_matrices": "Use sparse matrix formats",
        "memory_mapping": "Memory-mapped file access"
    },
    "gpu_acceleration": {
        "cupy": "GPU-accelerated NumPy",
        "rapids": "GPU-accelerated data science",
        "tensorflow": "Deep learning frameworks"
    }
}

def get_updated_methods_summary():
    """현대적인 방법들의 요약 정보 반환"""
    return {
        "normalization": "TMM, DESeq2, TPM 방법 사용 권장",
        "statistical_analysis": "DESeq2, edgeR, limma-voom 사용 권장",
        "multiple_testing": "BH-FDR, q-value 방법 사용",
        "visualization": "Interactive plots (plotly, bokeh) 권장",
        "pathway_analysis": "GSEA, fgsea, clusterProfiler 사용",
        "performance": "병렬 처리 및 GPU 가속 활용",
        "databases": "2024년 최신 버전 데이터베이스 사용"
    }

if __name__ == "__main__":
    print("Modern RNA Analysis Methods - 2024 Best Practices")
    print("=" * 50)
    
    summary = get_updated_methods_summary()
    for category, recommendation in summary.items():
        print(f"{category.upper()}: {recommendation}")
