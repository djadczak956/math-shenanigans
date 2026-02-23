# Notes about Math Shenanigans
My purpose here to is construct mathematical concepts in code as a demonstration of my understanding (and because it is plenty interesting).

## Interval
My intention with ```interval.py``` is to represent mathematical intervals in python. I also attempt to implement certain operations, like checking if an element is contained within an interval, or generating a random element contained within an interval (W.I.P. currently I think).

## Integer Rings w/ Modulus
I wanted to have Rings already built for use with the Musical Tones w/ Ring Theory project. I think that this is also something that I could play with. This can be found in ```int_mod_ring.py```. 

## Musical Tones w/ Ring Theory
I found a paper (cite here) that connects the 12 musical tones in western music to ring theory. Essentially, you can define addition and multiplication of musical tones by representing each musical tone as integers in the set of integers modulo 12. This can be be found in ```music_tone_ring.py```.
- This uses a venv called ```music_rings```.