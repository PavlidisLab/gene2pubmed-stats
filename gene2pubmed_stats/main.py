import argparse
import pandas as pd
import sys
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

GENE2PUBMED_URL = 'https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2pubmed.gz'

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)
    parser_a = subparsers.add_parser('publications-per-gene')
    parser_a.add_argument('--taxon-id', type=int)
    args = parser.parse_args(sys.argv[1:])
    logger.info('Reading from {}...'.format(GENE2PUBMED_URL))
    df = pd.read_csv(GENE2PUBMED_URL, sep='\t', compression='gzip')
    publication_counts_by_gene_id = df.groupby(['#tax_id', 'GeneID']).count().rename(columns={'PubMed_ID': 'Number of publications'})
    publication_counts_by_gene_id.loc[args.taxon_id].to_csv(sys.stdout, sep='\t')

if __name__ == '__main__':
    sys.exit(main())
