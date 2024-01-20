# Gilded Rose Kata

Programming paradigm kata based on famous [Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main).
The ideas were presented in [devbg talk](https://dev.bg/event/python-metaprogramming-or-what-i-should-have-known-from-the-start/) about `Metaprogramming`.

## Installation

### Requirements

- pandoc
- texlive with texlive-extratex should be fine

### Install

```bash
git clone --depth 1 https://github.com/dpopchev/gilded-rose-kata.git
cd devbg2024
```

#### Project

Build project into dedicated virtual environment python.

```bash
make development
make check
```

Expect failing tests. The project is a kata itself to practice refactoring to:

- object oriented programming
- functional programming
- metaprogramming

#### Presentation

Build the presentation

```bash
make presentation
```

## Agenda

- Software engineering
- Test/Behaviour driven development
- Object oriented vs Functional vs Procedural programming
- Career development vs reduction using metaclasses

## Usage

### Live presentation rebuild

While making the presentation I found useful to trigger build of the
presentation on changes under `docs`.

```bash
ls docs/* | entr sh -c 'echo compile: $(date +%H:%M:%S) && make presentation && echo compile: end && pkill -HUP mupdf && echo REFRESHED'
```

## Acknowledgement

- [Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main)
- [Goblin](https://www.deviantart.com/futurerender/art/Orc-Selfie-12-Bedroom-956964946)
- [Descriptors howto](https://docs.python.org/3/howto/descriptor.html)
- [Metaprogramming in python](https://developer.ibm.com/tutorials/ba-metaprogramming-python/)
- [A primer on python metaclasses](https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/)

## License

[MIT](LICENSE)
