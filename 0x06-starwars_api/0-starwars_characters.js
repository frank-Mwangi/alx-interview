#!/usr/bin/node

const request = require("request");
const process = require("process");

function getMovieCharacters(movieId) {
  const baseUrl = "https://swapi.dev/api";
  const movieUrl = `${baseUrl}/films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } else {
            console.error(`Failed to fetch character for ${characterUrl}`);
          }
        });
      });
    } else {
      console.error(`Failed to fetch movie data for movie ID ${movieId}`);
    }
  });
}
if (process.argv.length !== 3) {
  console.log("Usage: node 0-starwars_characters.js <Movie ID");
  process.exit(1);
}

const movieId = process.argv[2];

getMovieCharacters(movieId);
