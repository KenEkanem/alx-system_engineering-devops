# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Configure custom Nginx site
file { '/etc/nginx/sites-available/default':
  content => template('nginx/custom-config.erb'),
  notify => service['nginx'],
}

# Set up index.html with Hello World!
file { '/var/www/html/index.html':
  content => 'Hello World!',
  notify => service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

