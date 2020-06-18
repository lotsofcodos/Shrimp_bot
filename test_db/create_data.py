
import shelve


with shelve.open('test_store') as store:
  while True:
      name=input('Enter name')
      if name == 'end':
        break
      age= input('Enter age')
      location = input('Enter location')

      record = {
        'Name': name,
        'Age': age,
        'Location': location
      }

      store[name] = record