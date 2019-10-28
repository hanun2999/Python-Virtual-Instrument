from instrument import instrument

a = (clf.predict(temp))[0][0]

if a == 1:
    trombone.action(1)
elif a == 0:
    trombone.action(2)



trombone = instrument("tromboneSounds.txt")

trombone.action(3)

trombone.action(1)

trombone.action(3)

trombone.action(2)

trombone.action(3)
