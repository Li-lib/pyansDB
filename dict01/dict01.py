print( "Sixth test - .pop()" )
switch.pop('version') # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

print( "Seventh test - ADD a new value" )
switch['adminlogin'] = 'karl08'
print( switch.keys() )
print( switch.values() )

print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerty'
print( switch.keys() )
print( switch.values() )

