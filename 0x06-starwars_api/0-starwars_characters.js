#!/usr/bin/node

const request = require('request');
const process = require('process');

async function getMovieCharacters (movieId) {
  const baseUrl = 'https://swapi.dev/api';
  const movieUrl = `${baseUrl}/films/${movieId}/`;

  try {
    const movieData = await new Promise((resolve, reject) => {
      request(movieUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          resolve(JSON.parse(body));
        } else {
          console.error(`Failed to fetch movie data for movie ID ${movieId}`);
        }
      });
    });
    const characterPromises = movieData.characters.map((characterURL) => {
      return new Promise((resolve, reject) => {
        request(characterURL, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            console.error(`Failed to fetch character for ${characterURL}`);
          }
        });
      });
    });
    const characterNames = await Promise.all(characterPromises);
    for (const char of characterNames) {
      console.log(char);
    }
  } catch (error) {
    console.error(error);
  }
}
if (process.argv.length !== 3) {
  console.log('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}
const movieId = process.argv[2];
getMovieCharacters(movieId);
