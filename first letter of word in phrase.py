def get_fisrtLetter(phrase):
  words = phrase.split()
  letter = ''
  for word in words:
    letter += word[0].upper()
  return letter
print(get_firstLetter('I like Coffe')
      # shoud return: ILC
print(get_firstLetter('I just saved your cat from drowing')
      # shoud return: IJSYCFD
