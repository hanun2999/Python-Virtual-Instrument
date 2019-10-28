from instrument import instrument

t = instrument()

t.queue_sound(493, 1)
t.queue_sound(440, 1)
t.queue_sound(392, 1)

t.queue_sound(493, 1)
t.queue_sound(440, 1)
t.queue_sound(392, 1)

t.queue_sound(392, 0.5)
t.queue_sound(392, 0.5)
t.queue_sound(392, 0.5)
t.queue_sound(392, 0.5)

t.queue_sound(440, 0.5)
t.queue_sound(440, 0.5)
t.queue_sound(440, 0.5)
t.queue_sound(440, 0.5)

t.queue_sound(493, 1)
t.queue_sound(440, 1)
t.queue_sound(392, 1)

t.queue_play()
