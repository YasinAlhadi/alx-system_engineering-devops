# fix 500 internal server error

exec {'edit line':
  command  => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  provider => shell,
}
