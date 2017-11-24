from Bio import SeqIO
from Bio import Entrez

Entrez.email = "steven@stevenweaer.org"
output_filename = "opsins.fas"

def get_nuc_from_prot_accession(id):
	handle = Entrez.efetch(db="protein", id=id, rettype="gb", retmode="text")
	record = SeqIO.read(handle, "genbank")

	# Get db_source
	source = record.annotations["db_source"]

	handle = Entrez.efetch(db="nucleotide", id=source,rettype="gb", retmode="text")
	record = next(SeqIO.parse(handle, "genbank"))
	return record

# add sequence to concatenated FASTA file

with open('all_species_with_accession', 'r') as f:
	lines = f.readlines()
	recs = map(lambda x : get_nuc_from_prot_accession(x), lines)

SeqIO.write(recs, output_filename, "fasta")
