# Install Nginx
class { 'nginx': }

# Create a custom Nginx configuration file to add the custom header
file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => present,
  content => "add_header X-Served-By ${hostname};",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}

