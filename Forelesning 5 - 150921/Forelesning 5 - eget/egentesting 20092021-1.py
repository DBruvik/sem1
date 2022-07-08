#This program assists a technician in the process of checking
#a substances temperature

#Named constant to represent the maximum temperature
MAXTEMP=102.5

#Get the substances temperature
temperature = float(input('Enter the substances celsius temperature: '))

#As long as necessary, instruct the user to adjust the thermostat
while temperature > MAXTEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature again and enter it.')
    temperature=float(input('Enter the new celsius temperature: '))

#Remind the user to check the temperature again in 15 min
print ('The temperature is acceptable.')
print ('Check it again in 15 minutes.')
