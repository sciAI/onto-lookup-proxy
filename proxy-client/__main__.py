from flask import Flask, request
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
<pre id="output"></pre>
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
    return page


@app.route("/start", methods=['POST'])
def start():
    echo = ''

    #client = MongoClient('localhost', 27017)
    api = swagger_client.ResourceApi()

    #db = client['proxy-db']
    #db_terms = db.terms
    repositories = api.repositories()
    for repository in repositories:
        repo = repository.get('@id')

        ontologies = api.ontologies(repository=repo)
        for ontology in ontologies:
            onto = ontology.get('http://omv.ontoware.org/2005/05/ontology#acronym')

            concepts = api.concepts(repository=repo, ontology=onto)
    #        for concept in concepts:
    #            compact = jsonld.compact(concept, concept_context)
    #            db_term = db_terms.insert(compact, check_keys=False)

    return 'The asynchronous process is started, check proxy-db-async database'


@app.route("/insert", methods=['POST'])
def insert():
    echo = ''

    client = MongoClient('localhost', 27017)

    db = client['proxy-db-async']
    db_terms = db.terms

    compact = jsonld.compact(request.json, concept_context)
    db_term = db_terms.insert(compact, check_keys=False)

    return 'OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
