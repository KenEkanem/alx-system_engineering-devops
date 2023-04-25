# Installing flask from pip3 with Puppet
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
