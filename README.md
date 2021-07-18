# learnMicroservices

In this repo, I'll try to to fully grasp microservices development and deployment through a series of scenarios.

The objectives are :
 - Try most common microservices communcation technologies : RestAPI, gRPC.
 - Deploy microservices to a Python production environment with Docker then Kubernetes (and maybe something else after).
 - Deploy different types of databases in Docker then Kubernetes.
 - Include unit tests and integration tests to these microservices and middleware.

## Stage 1 :

 - Microservices communication : RestAPI
 - Database : CSV file
 - Deployed as Docker containers with Docker-compose.

### Architecture

Let's start with something simple.
The simplest architecture that came to mind was this :

 - A web server that requests informations from a DB server and prints them back to the client.
 - A DB server that provides an API through *pokedex* endpoint.

```
	┌──────────┐       ┌────────────┐          ┌───────────┐
	│          ├───────►            ├──────────►           │
	│ Client   │       │ Web Server │          │ DB Server │
	│ Browser  ◄───────┤            ◄──────────┤           │
	│          │       └────────────┘          └───────────┘
	└──────────┘
```

### Web server

 - Minimalistic, It requests info from DB server and do a little html formatting.
 - Built in Flask.

### DB server

I'll start with simple csv files that contains all *existing* pokemons in the [Pokémon Pokédex](https://pokemondb.net/pokedex).

For a start I'll implement only 2 GET methods :

To request all pokedex :

> GET /api/pokedex/

To request a pokemon info :

> GET /api/pokedex/[POKEMON NAME]

# TODO