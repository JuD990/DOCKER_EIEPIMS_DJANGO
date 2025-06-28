FROM node:22

WORKDIR /app

# Install correct npm version before app dependencies
RUN npm install -g npm@11.4.2

# Copy package files first to cache `npm install`
COPY package*.json ./

RUN npm install
RUN npm fund
RUN npm audit fix --force
RUN npm audit

# Copy rest of the frontend files
COPY . .

CMD ["npm", "start"]
