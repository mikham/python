#def calc_circle_area(radius):
 #area = (float(radius)**2) *3.1415926
 #print ('Circle area is '+str(area))

#radius = input('What is the radius of circle? ')
#calc_circle_area(radius)


def calc_numb_vowels(text):
    counter = 0
    for i in text:
        if i in ['a', 'e','i','o','u','ê', 'é','à','í','á', 'â', 'ó','ô','ú', 'A','E','I','O','U']:
            counter +=1
    return counter

messenger = str(input('Type a text:'))
function = calc_numb_vowels(messenger)
print (function)


