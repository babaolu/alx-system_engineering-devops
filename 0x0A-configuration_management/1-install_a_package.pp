# Installing flask from pip3 using puppet

package { 'python3':
  ensure => installed,
  name   => 'python3',
}

package { 'Werkzeug':
  ensure   => '2.3.7',
  name     => 'Werkzeug',
  require  => Package['python3'],
  provider => 'pip3'
}

package { 'flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  require  => Package['Werkzeug'],
  provider => 'pip3',
}
