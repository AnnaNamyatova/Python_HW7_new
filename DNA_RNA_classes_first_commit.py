class Dna(str):
    
    
    def __init__(self, dna_seq):  
        self.dna_seq = dna_seq
        codes = 'AaCcGgTtRrWwSsYyKkVvHhDdBbNn'
        for i in dna_seq:            
            if i not in codes:
                raise Exception('String is not a DNA sequence')
            
    def gc(self):
        self = self.upper()
        gc_percent = round(((self.count('G') + self.count('C'))*100)/len(self), 1)
        gc_percent_str = str(gc_content) + '%'
        return gc_percent_str
    
    def reverse_complement(self):
        self = self.upper()
        compl_sequence = self.translate(self.maketrans('ACGTRWSYKMVHDBN', 'TGCAYWSRMKBDHVN'))
        return compl_sequence[::-1]
    
    def transcribe(self):
        self = self.upper()
        return self.translate(self.maketrans('ACGTRWSYKMVHDBN', 'UGCAYWSRMKBDHVN'))
    
class Rna(str):

    
    def __init__(self, rna_seq):        
        self.rna_seq = rna_seq
        codes = 'AaCcGgUuRrWwSsYyKkVvHhDdBbNn'
        for i in self:            
            if i not in codes:
                raise Exception('String is not a RNA sequence')
            
    def gc(self):
        self = self.upper()
        gc_percent = round((self.count('G') + self.count('C'))*100/len(self), 1)
        gc_percent_str = str(gc_content) + '%'
        return gc_percent_str
    
    def reverse_complement(self):
        self = self.upper()
        compl_sequence = self.translate(self.maketrans('ACGURWSYKMVHDBN', 'UGCAYWSRMKBDHVN'))
        return compl_sequence[::-1]
