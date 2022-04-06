import urllib.request
import urllib.parse
import json

numberOfFilms = 0
endpoint="https://challenges.hackajob.co/swapi/api/people/?"
param={ 'search': character}
#urlencoding required here, otherwise it will give incorrect url error
newparam=urllib.parse.urlencode(param)
Searchurl= endpoint + newparam
with urllib.request.urlopen(Searchurl) as url:
	data=json.loads(url.read().decode())
	# typical complex data structure problem: Hash -> Array -> Hash -> Array
	numberOfFilms=len(data['results'][0]['films'])
		
		
print (numberOfFilms)


