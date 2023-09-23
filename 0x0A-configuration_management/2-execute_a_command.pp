# now i am happy process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
