# scrip that it configures a brand new Ubuntu machine

exec {'/usr/bin/env apt-get -y update':}
package {'nginx':
  ensure => installed,
}
file {'/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World',
}
file_line {'add header':
ensure => present,
path   => '/etc/nginx/sites-available/default',
line   => "add_header X-Served-by ${hostname};",
after  => 'server_name_;',
}
service {'nginx':
  ensure => running,
}
