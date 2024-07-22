FROM nginx:latest

# Install curl
RUN apt-get update && apt-get install -y curl

# Copy your custom Nginx configuration file
COPY nginx-setup.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80




# # Dockerfile for Nginx

# FROM nginx:alpine

# # Copy the Nginx configuration file
# COPY nginx.conf /etc/nginx/nginx.conf

# # Copy the built React app from the frontend build stage
# COPY --from=frontend /client/build /usr/share/nginx/html

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]