FROM node:lts-alpine

WORKDIR /app

RUN npm install -g npm@8.5.2

COPY package.json .
COPY package-lock.json .
RUN npm install
RUN chmod -R 777 node_modules
COPY . .

CMD ["npm", "run", "dev"]