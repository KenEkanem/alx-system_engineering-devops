class nginx {
package { 'nginx':
ensure => installed,
}

service { 'nginx':
ensure => running,
require => Package['nginx'],
}
}

class nginx::site {
file_line { 'redirect':
ensure => 'present',
path => '/etc/nginx/sites-available/default',
after => 'listen 80 default_server;',
line => 'rewrite ^/redirect_me https://fusedtc.tech permanent;',
}

file { '/var/www/html/index.html':
content => 'Hello World!',
}
}

include nginx
include nginx::site
