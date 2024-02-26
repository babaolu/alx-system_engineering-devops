# Appending to config file using puppet
$file_content = file('/etc/ssh/ssh_config', 'content')
$new_content = "${file_content}\n\nHost ubuntu@52.5.101.209
    HostName 52.5.101.209
    User ubuntu
    IdentityFile ~/.ssh/school"

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => $new_content,
}
