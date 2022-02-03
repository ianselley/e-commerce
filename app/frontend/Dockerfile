FROM node:lts-alpine

RUN mkdir app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.15 -g
RUN npm install @vue/cli-plugin-e2e-cypress --save-dev

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]