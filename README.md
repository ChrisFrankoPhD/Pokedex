# Pokedex

Python command line program for searching the original 151 pokedex using https://pokeapi.co/

## Dependencies

- climage
- requests
- colorama

## Usage

- "sprite1.jpg" is an empty jpg file, python overwrites this file with the sprite image of the chosen pokemon, since climage needs a local file to turn into the command-line printout. The dummy file is not needed, but is there to prompt users so they are not concerned when a random file is created during use.

- Includes search functionality, so that you can enter a search query and the program will return a list of results that the user can reference the spelling of pokenames and such
    - However, the search functionality also adds a significant delay on loading, as we need to call the API for the list of all pokemon (restricted to original 151) before we start

## Credit

- This app makes use of the well-structured and free PokeAPI (https://pokeapi.co/)