from Bio import SeqIO
from Bio import Entrez
import wikipedia

Entrez.email = "steven@stevenweaer.org"
output_filename = "opsins.fas"

def get_species_from_prot_accession(id):
    handle = Entrez.efetch(db="protein", id=id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    # Get db_source
    return record.annotations["organism"]

def get_wiki(id):
    try:
        search = wikipedia.page(id)
    except:
        search = wikipedia.search(id)
    return search

with open('organisms.txt', 'r') as f:
    lines = f.readlines()
    recs = map(lambda x : get_wiki(x), lines)

for rec in recs:
    try:
        print(rec.title)
    except:
        print(rec)
