# Process data so that it can be used with Geneformer.

import scanpy as sc
import pandas as pd
import numpy as np

# change this to the directory that contains the datasets
data_dir = 'C:/Users/nbrouwer1/Documents/VS_projects/prepare_data/input_files/sciplex_selections/'

fn = data_dir + 'sciPlex2_A549_all4_drugs_and_doses.h5ad'

adata_orig = sc.read_h5ad(fn)
adata_orig.var_names_make_unique()
adata_orig.obs = adata_orig.obs.rename(columns={'n.umi':'n_counts'})
adata_orig.var = adata_orig.var.rename(columns={'Ensemble Id':'ensembl_id'})
#How do we assign labels?
adata_orig.obs['treated_label'] = np.where((adata_orig.obs['dose'] == '0.0'), 'Untreated', adata_orig.obs['drug'])
adata_orig.var['ensembl_id']  = [s.split('.')[0] for s in adata_orig.var['ensembl_id']]

adata_orig.write_h5ad('C:/Users/nbrouwer1/Documents/VS_projects/prepare_data/input_files/sciplex_processed/sciplex2_processed2.h5ad')

print('DATA PROCESSED')