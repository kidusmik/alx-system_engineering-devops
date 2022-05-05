# change all limits
exec { 'Change all limit':
  command  => 'sudo sed -i "s/holberton\sall.*/holberton\tall\tnofile\t100000/" /etc/security/limits.conf',
  provider => shell,
}
