# Smart Proxy

Both server (a.k.a [proxy](https://git.xpansa.com/csc/harvester-demo/tree/master/proxy-server)) and client (a.k.a [harverter](https://git.xpansa.com/csc/harvester-demo/tree/master/proxy-client)) are automatically generated by [swagger codegen](https://editor.swagger.io/) based on OpenAPI descriptions.

## Structure

There are several subprojects committed into this repository:

- `codegen`
  - `openapi` contains OpenAPI descriptors for proxy server/client and repositories (see below);
  - `scripts` contains scripts to generate source code based on OpenAPI descriptors from `openapi` folder;
- `proxy-client` contains source code for the harvester (all generated by `codegen` except controllers) that gathers data from repositories via the proxy server
- `proxy-server` contains source code for the proxy server (all generated by `codegen` except controllers)
  - `swagger_server`/`controllers`/`repositories` contains libraries to easily retrieve data from external repositories (all automatically generated)
- `repositories` is actually a `swagger_server`/`controllers`/`repositories` directory moved on top for convenience

## How it works?

Normally, once user starts the `harvester`...

- sends 'repository' request to the proxy server and receives list of repositories supported by the proxy server
- sends 'ontology' requests to the proxy server in order to receive list of ontologies supported by each repository
  - proxy server requests data from repository
  - proxy server automatically (if there are 'pages' in response) iterates through the pages to gather all possible data
  - proxy server transform data in accordance with the mapping (provided in `Meta`/`ontology` object, see below)
  - send data in required format back to the `harvester`
- sends 'concepts' requests to the proxy server in order to receive list of terms/classes/concepts contained within each ontology in each repository
  - proxy server requests data from repository
  - proxy server automatically (if there are 'pages' in response) iterates through the pages to gather all possible data
  - proxy server transform data in accordance with the mapping (provided in `Meta`/`concept` object, see below)
  - send data in required format (it could be a `jsonld`) back to the `harvester`
- inserts data 'as-is' into `mongodb` collection: `terms`

## Data

List of OpenAPI [descriptors](https://git.xpansa.com/csc/harvester-demo/tree/master/codegen/openapi) used for smart proxy project:
- `smart_proxy.yaml` describes API for the proxy server
- `ebi_ac_uk_ols.yaml` describes API for the EMBL-EBI Ontology Lookup Service (and includes mappings for data transfiguration)

### Mapping

Note mapping for response data is included into OpenAPI descriptors, see `Meta` objects:

```yaml
meta:
  type: "object"
  properties:
    ontology_xpath:
      type: "string"
      default: "embedded.ontologies"
    ontology:
      type: "object"
      properties:
        "@id":
          type: "string"
          default: "config.id"
        "dct:title":
          type: "string"
          default: "config.title"
        ...
    concept_xpath:
      type: "string"
      default: "embedded.terms"
    concept:
      type: "object"
      properties:
        "@id":
          type: "string"
          default: "iri"
        "skos:prefLabel":
          type: "string"
          default: "label"
        ...
```
where `default` property is a path to particular property within repository response (or path to array of ontologies/terms for `_xpath` properties).

Structure of properties is actually defined in OpenAPI [descriptor](https://git.xpansa.com/csc/harvester-demo/tree/master/codegen/openapi/smart_proxy.yaml) for the proxy server:

```yaml
definitions:
  repository:
    properties:
      - "@id"
      - "@type"
      - "dcat:landingPage"
      - "dct:title"
  ontology:
    properties:
      - "schema:includedInDataCatalog"
      - "@id"
      - "@type"
      - "dct:title"
      - "dct:description"
      - "omv:acronym"
      - "owl:versionInfo"
      - "dct:modified"
  concept:
    properties:
      - "rdfs:isDefinedBy"
      - "@id"
      - "skos:prefLabel"
      - "skos:definition"
      - "skos:note"
      - "skos:altLabel"
```

## Demo:

Server:
- get sample repositories: http://176.31.200.199/repositories
- get sample ontologies: http://176.31.200.199/repositories/ols/ontologies
- get sample concepts: http://176.31.200.199/repositories/ols/ontologies/aero/concepts
- search across repositories: http://176.31.200.199/search?query=ipomoea%20batatas

Client:
- start processing: http://176.31.200.202/
- check results: see `terms` collection within `proxy-db` database (mongo)

### Repositories:

The following repositories are supported:
- EMBL-EBI OLS
  - http://176.31.200.199/repositories/ols/ontologies
  - http://176.31.200.199/repositories/ols/ontologies/aero/concepts
- NCBO BioPortal (apikey=e7f84ef1-1530-4a02-85c6-6f907ab44ce8)
  - http://176.31.200.199/repositories/bioportal/ontologies
  - http://176.31.200.199/repositories/bioportal/ontologies/ICO/concepts
- ANDS Services
  - (to be defined)

### Technical data

All flask servers are located within `/var/www/proxy-*` directories and running 'behind' `apache2` server. To add new repository, please generate it via [swagger codegen](https://editor.swagger.io/), rename `swagger-client` (use any repository codename, eg.: `ols`, `bioportal`) and put it into `/var/www/proxy-server/swagger_server/controllers/repositories/` directory; then restart the server: `/etc/init.d/apache2 restart`
