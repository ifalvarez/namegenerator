'''
Created on May 8, 2012

@author: El Coco
'''
from restful.restful_lib import Connection
from xml.dom.minidom import parseString
import logging
import re

logger = logging.getLogger(__name__)

class ThesaurusClient:
    """Class to use Thesaurus.com from python"""
    def __init__(self, _host="http://thesaurus.com"):
        self.conn = Connection(_host)
        
    def get(self, _url, _params={}, _headers={}):
        resp = self.conn.request_get(
             _url, _params, _headers
        )
        status = resp[u'headers']['status']
        if status == '200' or status == '304':
            return resp[u"body"]
        else:
            raise StandardError('Error. Response from server was: ', resp)

    def getSynonyms(self, word):
        try:
            synonyms = self.get('/browse/' + word)
            synonyms = re.findall('<table.*?class="the_content">.*?</table>', synonyms, flags=re.DOTALL)[0]
            synonyms = re.findall('<tr.*?>.*?</tr>', synonyms, flags=re.DOTALL)[3]
            synonyms = re.findall('<td.*?>.*?</td>', synonyms, flags=re.DOTALL)[1]
            labels = ["a", "b", "span", "td"]
            for l in labels:
                synonyms = re.sub('<{0}.*?>(.*?)</{0}>'.format(l), "\g<1>", synonyms, flags=re.DOTALL)
            synonyms = re.sub("\n", "", synonyms, flags=re.DOTALL)
            synonyms = synonyms.split(",")
            for i, s in enumerate(synonyms):
                synonyms[i] = s.title().strip().replace(" ", "")
        except:
            logger.warn('Word "{0}": error while searching synonyms')
            synonyms = [word.title()]
        return synonyms

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    logging.basicConfig(level="DEBUG")
    client = ThesaurusClient()
    response = client.getSynonyms("factory")
    pp.pprint(response)
    
    
    