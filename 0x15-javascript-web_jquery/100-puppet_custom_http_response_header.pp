# creating a custom HTTP header response with Puppet

exec { 'update':
  command => 'apt update',
  path    => '/usr/bin/'
}
->
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
header_line { 'Header using sed':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}