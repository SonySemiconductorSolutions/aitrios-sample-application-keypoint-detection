# choice https://github.com/microsoft/vscode-dev-containers/tree/main/containers/typescript-node
ARG VARIANT=18-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/typescript-node:${VARIANT}

WORKDIR /app
COPY . /app

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev"]