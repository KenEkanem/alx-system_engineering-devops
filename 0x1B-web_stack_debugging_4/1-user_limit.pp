# This script creates the "holberton" user
user { 'holberton':
  ensure     => 'present',
  home       => '/home/holberton',
  managehome => true,
  shell      => '/bin/bash',
}

# Allow the "holberton" user to log in
file { '/etc/ssh/sshd_config':
  ensure  => 'file',
  notify  => Service['ssh'],
}

case $::osfamily {
  'Debian': {
    $service_name = 'ssh'
  }
  'RedHat': {
    $service_name = 'sshd'
  }
  default: {
    fail("Unsupported operating system family: ${::osfamily}")
  }
}

service { 'ssh':
  ensure => 'running',
  enable => true,
  name   => $service_name,
}

# Additional configuration steps if required
