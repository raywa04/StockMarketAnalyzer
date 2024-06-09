# Use the official Node.js image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and yarn.lock files
COPY package.json yarn.lock ./

# Install the dependencies
RUN yarn install

# Copy the current directory contents into the container
COPY . .

# Build the app
RUN yarn build

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the application
CMD ["yarn", "start"]
