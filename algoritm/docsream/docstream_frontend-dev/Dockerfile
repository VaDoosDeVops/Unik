FROM node:lts-alpine as build

WORKDIR /app
COPY . . 

RUN yarn install && \
      yarn build
RUN ls -la

#FROM node:lts-alpine as release

#WORKDIR /app
#RUN mkdir .nuxt .output node_modules

#COPY --from=build app/.nuxt/ ./.nuxt/
#COPY --from=build app/.output/ ./.output/
#COPY --from=build app/node_modules/ ./node_modules/
#COPY --from=build app/package.json .
#COPY --from=build app/vue.config.js .

EXPOSE 3000
ENTRYPOINT [ "yarn", "serve" ]
