# Kills killmenow
exec { 'kill killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
}
