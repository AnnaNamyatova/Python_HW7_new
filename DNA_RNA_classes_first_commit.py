class Dna(str):  #The uploaded DNA should run from 3' to 5' end
    
    
    def __init__(self, dna_seq):  
        self.dna_seq = dna_seq.upper()
        codes = 'AaCcGgTtRrWwSsYyKkVvHhDdBbNn'
        for i in dna_seq:            
            if i not in codes:
                raise Exception('String is not a DNA sequence')
            
    def gc(self):
        self = self.dna_seq
        gc_percent = round(((self.count('G') + self.count('C') + self.count('S'))*100)/len(self), 1)        
        return (str(gc_percent) + '%')
    
    def reverse_complement(self):
        self = self.dna_seq        
        compl_sequence = self.translate(self.maketrans('ACGTRWSYKMVHDBN', 'TGCAYWSRMKBDHVN'))
        return compl_sequence[::-1]
    
    def transcribe(self):
        self = self.dna_seq
        return self.translate(self.maketrans('ACGTRWSYKMVHDBN', 'UGCAYWSRMKBDHVN'))
    
class Rna(str):

    
    def __init__(self, rna_seq):        
        self.rna_seq = rna_seq.upper()
        codes = 'AaCcGgUuRrWwSsYyKkVvHhDdBbNn'
        for i in self:            
            if i not in codes:
                raise Exception('String is not a RNA sequence')
            
    def gc(self):
        self = self.rna_seq
        gc_percent = round((self.count('G') + self.count('C') + self.count('S'))*100/len(self), 1)        
        return (str(gc_percent) + '%')
    
    def reverse_complement(self):
        self = self.upper()
        compl_sequence = self.translate(self.maketrans('ACGURWSYKMVHDBN', 'UGCAYWSRMKBDHVN'))
        return compl_sequence[::-1]
