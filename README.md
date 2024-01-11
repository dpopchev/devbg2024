# devbg2024

Notes and code for my [devbg talk](https://dev.bg/event/python-metaprogramming-or-what-i-should-have-known-from-the-start/).

## Installation

### Requirements

- pandoc
- some tex libs, texlive with texlive-extratex should be fine

### Install

```
git clone --depth 1 https://github.com/dpopchev/devbg2024.git
cd devbg2024
make development
make check
make presentation
```

## Agenda

- Software engineering background: NATO conference 68 and UNIX vs agile
- Test vs Behaviour driven development
- OOP vs FP
- Metaclasses (career development vs reduction)

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
