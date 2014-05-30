'''
Created on May 8, 2012

@author: El Coco
'''
from synonyms.thesaurus import ThesaurusClient
import itertools
import logging

logger = logging.getLogger(__name__)

class NameGenerator:
    def __init__(self):
        self.synonymClient = ThesaurusClient()
        
    def getNames(self, seeds):
        seedsSynonyms = []
        for seed in seeds:
            synonyms = self.synonymClient.getSynonyms(seed)
            synonyms.append(seed.title())
            seedsSynonyms.append(synonyms)
        return map("".join, itertools.product(*seedsSynonyms))
    
if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    logging.basicConfig(level="DEBUG")
    
    seeds = ["party", "route"]
    
    generator = NameGenerator()
    response = generator.getNames(seeds)
    for name in response:
        print name
    
    
    