# This script installs Nginx using Puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

file {'/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file {'/etc/nginx/sites-available/default':
  ensure => 'file',
  source => '/path/to/default.conf',
}

file {'/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

exec {'restart':
  command => 'sudo service nginx restart',
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}



