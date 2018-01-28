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
<div id="output"></div>
</body>
</html>
"""

@app.route("/")
def index():
    return page

@app.route("/start", methods=['POST'])
def start():
    echo = ''

    context = {
        "iri": "http://schema.org/iri",
        "description": "http://schema.org/description",
        "label": "http://schema.org/label",
        "short": "http://schema.org/short_form",
        "synonyms": "http://schema.org/synonyms",
        "repository": {"@id": "http://schema.org/repository", "@type": "@id"},
        "ontology": {"@id": "http://schema.org/ontology", "@type": "@id"}
    }

    client = MongoClient('localhost', 27017)
    api = swagger_client.ResourceApi()

    db = client['proxy-db']
    db_terms = db.terms
    repositories = api.repositories()
    for repository in repositories:
        repo = repository.name

        ontologies = api.ontologies(repository=repo)
        for ontology in ontologies:
            onto = ontology.acronym

            concepts = api.concepts(repository=repo, ontology=onto)
            for concept in concepts:
                compact = jsonld.compact(concept, context)
                db_term = db_terms.insert(compact, check_keys=False)

    return '{0} records processed'.format(db_terms.count())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
