from flask import Flask
from pyld import jsonld
from pymongo import MongoClient
from . import swagger_client

import json
import time


app = Flask(__name__)

page = """
<!DOCTYPE HTML>
<html>
<head>
<title>proxy client</title>
</head>
<body>
<form action="/start" method="POST">
<input type="submit" value="Start"/>
</form>
<hr/>
<div>Sample <b>Repository</b> output:<pre id="repositories"></pre></div>
<div>Sample <b>Ontology</b> output:<pre id="ontologies"></pre></div>
<div>Sample <b>Concept</b> output:<pre id="concepts"></pre></div>
<pre id="output"></pre>
<script>
document.getElementById("repositories").innerHTML = JSON.stringify(%s, undefined, 2);
document.getElementById("ontologies").innerHTML = JSON.stringify(%s, undefined, 2);
document.getElementById("concepts").innerHTML = JSON.stringify(%s, undefined, 2);
</script>
</body>
</html>
"""

repository_context = {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
}

ontology_context = {
    "omv": "http://omv.ontoware.org/2005/05/ontology#",
    "dct": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "owl": "http://www.w3.org/2002/07/owl#",
}

concept_context = {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
}

@app.route("/")
def index():
    api = swagger_client.ResourceApi()

    _repo = ''
    _onto = ''
    _term = ''

    repositories = api.repositories()
    for repository in repositories:
        repo = repository.get('@id')

        ontologies = api.ontologies(repository=repo)
        for ontology in ontologies:
            onto = ontology.get('http://omv.ontoware.org/2005/05/ontology#acronym')

            concepts = api.concepts(repository=repo, ontology=onto)
            for concept in concepts:
                term = concept.get('http://www.w3.org/2004/02/skos/core#note')

                return page % (
                    jsonld.compact(repository, repository_context),
                    jsonld.compact(ontology, ontology_context),
                    jsonld.compact(concept, concept_context)
                )

    return page % ('', '', '')

@app.route("/start", methods=['POST'])
def start():
    echo = ''

    client = MongoClient('localhost', 27017)
    api = swagger_client.ResourceApi()

    db = client['proxy-db']
    db_terms = db.terms
    repositories = api.repositories()
    for repository in repositories:
        repo = repository.get('@id')

        ontologies = api.ontologies(repository=repo)
        for ontology in ontologies:
            onto = ontology.get('http://omv.ontoware.org/2005/05/ontology#acronym')

            concepts = api.concepts(repository=repo, ontology=onto)
            for concept in concepts:
                compact = jsonld.compact(concept, concept_context)
                db_term = db_terms.insert(compact, check_keys=False)

    return '{0} records processed'.format(db_terms.count())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
