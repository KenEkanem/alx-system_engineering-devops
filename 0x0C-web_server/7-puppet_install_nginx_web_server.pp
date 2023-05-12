# This script installs Nginx using puppet and sets up a custom 301 redirect

# Install Nginx
package {'nginx':
  ensure => 'present',
}

# Set up custom index.html file
file {'/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Set up custom Nginx configuration file
file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => template('nginx/custom-config.erb'),
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
}

# Enable custom site and disable default site
file {'/etc/nginx/sites-enabled/default':
  ensure  => 'absent',
  require => File['/etc/nginx/sites-available/default'],
}

file {'/etc/nginx/sites-enabled/custom':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/custom',
  require => File['/etc/nginx/sites-available/custom'],
}

# Restart Nginx service
service {'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [File['/etc/nginx/sites-available/custom'], File['/var/www/html/index.html']],
}

