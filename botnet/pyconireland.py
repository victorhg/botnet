import re
import urllib
from BeautifulSoup import BeautifulSoup


class PyconIreland(object):
    def __init__(self):
        self.load_website_information()

    def load_website_information(self):
        f = urllib.urlopen('http://www.python.ie/pyconireland/conference')
        data = f.read()
        f.close()
        self.soup = BeautifulSoup(data)

    def find_speaker(self, speaker_name):
        """Returns Information about any of the speakers at Pycon Ireland 2010"""
        speaker_name = speaker_name.lower().replace(' ', '-')
        search_results = self.soup.findAll('div', id=re.compile('.*speaker-.*%s.*' % speaker_name ))
        if not len(search_results): 
            return 'No speaker was found. Are you in the right conference? Pycon Ireland2010? Try again plz... :)'
            
        result = ''
        for speaker in search_results:
            result += "Name: %s \n" % speaker.h3.string
            result += "Bio: \n %s\n\n" % speaker.div.div.string
        
        return result
    
    def find_talk(self, content_name):
        "Retrieves information about talks. Search for the authors name or the talks name"
        content_name = content_name.lower().replace(' ', '-')
        result = ''
        #Searching for speaker' name
        search_results = self.soup.findAll('a', href=re.compile('.*speaker-.*%s.*' % content_name ))
        if len(search_results):
            for item in search_results:
                talk = item.parent.parent.parent
                result += self._format_talk(talk)
                
        #searching for Talk's name       
        search_results = self.soup.findAll('div', id=re.compile('talk-.*%s.*' % content_name))
        if len(search_results):
            for talk in search_results:
                result += self._format_talk(talk)
        
        if not len(result):
            result = "No Talk has been found..."
                
        return result

    def _format_talk(self, talk):
            result = 'Talk: %s \n' % talk.h3.string
            description = talk.findNext(attrs={'class':'conference-description'}).div.prettify()
            p = re.compile(r'<.*?>\n')
            description = p.sub('', description)
            result += 'Description: \n %s \n\n' % description
            return result
