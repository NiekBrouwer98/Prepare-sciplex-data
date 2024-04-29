# Load datasets

This repository contains three notebooks that load and inspect the datasets sciplex2, sciplex3 and combosciplex.

The implementation is based on the following repositories:
* https://github.com/theislab/cpa-reproducibility/blob/main/notebooks/Fig2_sciplex.ipynb
* https://www.kaggle.com/code/alexandervc/sciplex3-loader-by-blocks-and-extract-parts/notebook
* https://github.com/theislab/sc-pert/blob/main/datasets/Srivatsan_2019_sciplex3.ipynb

The data is obtained from:
* sciplex2: https://www.kaggle.com/datasets/alexandervc/scrnaseq-exposed-to-multiple-compounds/data
* sciplex3: https://figshare.com/articles/dataset/Srivatsan_et_al_2019_sciPlex/19122572
* combosciplex: https://figshare.com/articles/dataset/combosciplex/25062230/1

I have added some examples how to preprocess and visualize the data, however Geneformer takes the raw count data as input, see the code citation below:

> Input data is a directory with .loom or .h5ad files containing raw counts from single cell RNAseq data, including all genes detected in the transcriptome without feature selection. The input file type is specified by the argument file_format in the tokenize_data function.