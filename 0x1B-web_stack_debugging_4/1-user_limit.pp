#configuration that make user open a file without any error message.

exec {'soft-limit':
  command  => 'sudo sed -i "s/nofile 5/nofile 10000/" /etc/security/limits.conf',
  provider => shell,
  before   => Exec['hard-limit'],
}

exec {'hard-limit':
  command  => 'sudo sed -i "s/nofile 4/nofile 30000/" /etc/security/limits.conf',
  provider => shell,
}
