FROM node:12-alpine

RUN mkdir app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.15 -g

COPY package.json .
RUN apk --no-cache --virtual build-dependencies add \
    python3 \
    make \
    g++ 
RUN npm install

CMD ["npm", "run", "serve"]