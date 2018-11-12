class Dna(str):
    
    
    def __init__(self, dna_seq):  
        self.dna_seq = dna_seq
        codes = 'AaCcGgTtRrWwSsYyKkVvHhDdBbNn'
        for i in self:            
            if i not in codes:
                raise Exception('String is a DNA sequence')
            
    def gc(self):
        self = self.upper()
        gc_percent = round(((self.count('G') + self.count('C'))*100)/len(self), 1)
        gc_percent_str = str(gc_content) + '%'
        return gc_percent_str
    
    def reverse_complement(self):
        self = self.upper()
        return self.translate(self.maketrans('ACGT', 'TGCA'))
    
    def transcribe(self):
        self = self.upper()
        return self.translate(self.maketrans('ACGT', 'UCGA'))
    
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
        compl_sequence = self.translate(self.maketrans('AUGC', 'UACG'))
        return compl_sequence
