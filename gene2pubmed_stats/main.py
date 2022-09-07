import argparse
import pandas as pd
import sys
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

GENE2PUBMED_URL = 'https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2pubmed.gz'

def publications_per_gene(args):
    logger.info('Reading from {}...'.format(GENE2PUBMED_URL))
    df = pd.read_csv(GENE2PUBMED_URL, sep='\t', compression='gzip')
    publication_counts_by_gene_id = df.groupby(['#tax_id', 'GeneID']).count().rename(columns={'PubMed_ID': 'Number of publications'})
    publication_counts_by_gene_id.loc[args.taxon_id].to_csv(sys.stdout, sep='\t')

def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=lambda args: parser.print_help() or 1)
    subparsers = parser.add_subparsers()
    parser_a = subparsers.add_parser('publications-per-gene')
    parser_a.add_argument('--taxon-id', type=int)
    parser_a.set_defaults(func=publications_per_gene)
    args = parser.parse_args(sys.argv[1:])
    return args.func(args)

if __name__ == '__main__':
    sys.exit(main())
