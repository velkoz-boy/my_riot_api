FROM node:15.14.0-alpine3.10
USER root

RUN apk update
RUN npm install -g npm @vue/cli

WORKDIR /code/app

ADD . /code/app

EXPOSE 8080

#プロジェクトファイルが存在する仮定でのコード
# 初回自は以下をコメントアウトして、vue createしたものを用意しないといけない
RUN npm install
ENTRYPOINT ["npm", "run", "serve"]
