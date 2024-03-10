#!/usr/bin/env bash
# sets up web servers for the deployment of web_static.

#install nginx if not available
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi

# Create necessary folder and files 
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Add sample content to file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"  | sudo tee /data/web_static/releases/test/index.html > /dev/null

#Creating symbolic link
# Define the source and target directories
source_dir="/data/web_static/releases/test"
target_link="/data/web_static/current"

# Check if the symbolic link already exists
if [ -L "$target_link" ]; then
    # If it exists, delete it
    sudo rm -rf "$target_link"
fi

# Create the symbolic link
sudo ln -s "$source_dir" "$target_link"

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-available/
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-enabled/

echo "
server {
	listen 80 default_server;
	listen [::]:80 default_server;


	root /var/www/html;
	#project task
  #error page redirection
	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /var/www/html;
		internal;
		}

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}
	#rewrite ^/redirect_me https://www.youtube.com permanent;

	#redirect_me
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=3lFkDc6dFoY;
		}

	# custom headers

}" > /etc/nginx/sites-available/default

# Setting up custom error page if not exists
file_path="/var/www/html/custom_404.html"
if [ -f "$file_path" ]; then
  echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html > /dev/null
else
  sudo touch /var/www/html/custom_404.html
  echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html > /dev/null
fi


config="/etc/nginx/sites-available/default"

sudo sed -i "/# custom headers/a \ \tadd_header X-Served-By $HOSTNAME;" "$config"
sudo sed -i '/server_name _;/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config
sudo service nginx restart
