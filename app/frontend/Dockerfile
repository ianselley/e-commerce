FROM node:lts-alpine

WORKDIR /app

COPY package.json .
RUN npm install
COPY . .
RUN touch vite.config.js

CMD ["npm", "run", "dev"]