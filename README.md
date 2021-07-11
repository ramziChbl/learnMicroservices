# learnMicroservices

In this repo, I'll try to to fully grasp microservices development and deployment through a series of scenarios.

The objectives are :
 - Try most common microservices communcation technologies : RestAPI, gRPC.
 - Deploy microservices to a Python production environment with Docker than Kubernetes and maybe something else after.
 - Deploy different types of databases in Docker than Kubernetes.
 - Include unit tests and integration tests to my microservices and middleware.

## Stage 1 :

 - Microservices communication : RestAPI
 - Database : CSV file

### Architecture

I want to start with something simple.
The simplest architecture that came to mind was this :

 - A web server that requests informations from a DB server and prints them back to the client.
 - A DB server that provides an API through *pokemon* endpoint.

```
	┌──────────┐       ┌────────────┐          ┌───────────┐
	│          ├───────►            ├──────────►           │
	│ Client   │       │ Web Server │          │ DB Server │
	│ Browser  ◄───────┤            ◄──────────┤           │
	│          │       └────────────┘          └───────────┘
	└──────────┘
```

### Web server

Minimalistic, It requests info from DB server and do a little html formatting.
I'll use Flask.

### DB server

I'll start with simple csv files that contains the [Pokémon Pokédex](https://pokemondb.net/pokedex).

Each Pokémon generation is saved in a csv file.

8 Generations == 8 files

For a start I'll implement only GET method :

> GET /api/pokedex/generation/pokemonNumber


# TODO