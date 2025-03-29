# Stage 1: Build the Angular app
FROM node:18 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the Angular app source code
COPY . .

# Build the Angular app (production mode)
RUN npm run build

# Stage 2: Serve the app using Nginx
FROM nginx:1.23

# Copy the build output from Stage 1 to Nginx HTML directory
COPY --from=build /app/dist/gen-aiui /usr/share/nginx/html

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the default HTTP port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
