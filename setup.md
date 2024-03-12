# Setup

Create and activate python virtual environment
```
echo ".venv*" >> .gitignore
python3 -m venv .venv-hl
source .venv-hl/bin/activate
```

Install required modules
```
python -m pip install --upgrade pip
pip install biopython
pip install melt
pip install headloop
```

Test `melt`
```
# should output 44.4
Tm ATGCATGC
# should output 26.4
Tm --dna 200 --na 50 --mg 3 --dntp 0.8 ATGCATGC
```

Test `Headloop`
```
python
from headloop.designer import design
design('CTGGTCCAGTGCGTTATTGG', 'AGCCAAATGCTTCTTGCTCTTTT', 
        'CTACAGGACGTACCTGCACCCGGATTCACCAGCGCCCG', 'antisense')
```

**Output**

(SeqRecord(seq=Seq('CCTGCACCCGGATTCACCAGCTGGTCCAGTGCGTTATTGG'), id='Sense HL', name='<unknown name>', description='WARNING: Could not optimise sense headloop tag (Tm difference > 3°C)', dbxrefs=[]), SeqRecord(seq=Seq('GGTGCAGGTACGTCCTGTAGAGCCAAATGCTTCTTGCTCTTTT'), id='Antisense HL', name='<unknown name>', description='Tm difference < 3°C', dbxrefs=[]))

Output installed modules
```
python -m pip freeze > requirements.txt
```