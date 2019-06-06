from pathlib import Path

import pandas as pd

from centreseq.bin.tree.cluster_data_structures import ClusterVariants


def generate_variant_summary_df(cluster_variants_list: [ClusterVariants]) -> pd.DataFrame:
    """ Creates a DataFrame containing summary information on all variants generated by snp-sites """
    columns = ['cluster', 'cluster_sequence_length', 'num_variants']
    rows = [[variants.parent_cluster.cluster_id, variants.parent_cluster.cluster_sequence_length, variants.num_variants]
            for variants in cluster_variants_list]
    df = pd.DataFrame(rows, columns=columns)
    df['variant_rate'] = df['num_variants'] / df['cluster_sequence_length']
    return df


def generate_variant_detail_df(cluster_variants_list: [ClusterVariants]) -> pd.DataFrame:
    """ Creates a DataFrame containing detailed information on every ClusterVariants object """

    # Loop through all clusters til we find a valid list of sample IDs
    sample_ids = []
    for variants in cluster_variants_list:
        if len(variants.variant_sample_ids) > 0:
            sample_ids = variants.variant_sample_ids
            break

    columns = ['cluster', 'cluster_length', 'chrom', 'pos', 'ref', 'alt'] + sample_ids
    rows = []
    for variants in cluster_variants_list:
        for v in variants.variant_list:
            genotypes = v.genotypes
            chrom = v.CHROM
            pos = v.POS
            ref = v.REF
            alt = ",".join(v.ALT)
            row = [variants.parent_cluster.cluster_id,
                   variants.parent_cluster.cluster_sequence_length,
                   chrom,
                   pos,
                   ref,
                   alt]
            for genotype in genotypes:
                row.append(genotype[0])
            rows.append(row)
    df = pd.DataFrame(rows, columns=columns)
    return df


def write_tsv_from_df(df: pd.DataFrame, outpath: Path) -> Path:
    """ Wrapper for pd.DataFrame.to_csv with preferred defaults """
    df.to_csv(outpath, sep="\t", index=None)
    return outpath


def read_summary_report(summary_report: Path) -> pd.DataFrame:
    """ Wrapper for pd.DataFrame.read_csv with preferred defaults """
    return pd.read_csv(summary_report, sep="\t", na_filter=False)
