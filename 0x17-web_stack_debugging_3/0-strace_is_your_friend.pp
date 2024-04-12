# Web stack debugging

exec { 'strace apache2':
  command => 'strace apache2'
}

package { 'php-common':
  ensure => installed,
  name   => 'php-common',
}

package { 'libapache2-mod-php':
  ensure => installed,
  name   => 'libapache2-mod-php',
}

package { 'php-cli':
  ensure => installed,
  name   => 'php-cli',
}

package { 'php-mysql':
  ensure => installed,
  name   => 'php-mysql',
}

package { 'php-curl':
  ensure => installed,
  name   => 'php-curl',
}

service { 'apache2':
  ensure => stopped,
  name   => 'apache2',
}

package { 'mysql-server':
  ensure => installed,
  name   => 'mysql-server'
}

service { 'mysqld':
  ensure => running,
  name   => 'mysqld',
  enable => true,
}

exec { 'chown -R www-data':
  command => 'sudo chown -R www-data:www-data www/'
  path    => '/var'
}

service { 'apache2':
  ensure  => running,
  name    => 'apache2',
  enable  => true,
  restart => 'sudo service restart'
}
