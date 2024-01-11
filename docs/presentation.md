---
topic: Metaprogramming
title: Metaprogramming
subtitle: what I should have known from the start
author: Dimitar Popchev
institute: GlobalFoundries
theme: Frankfurt
date: \today
fontsize: 8pt
fontfamilyoptions: default
section-titles: false
toc: false
aspectratio: 169
header-includes:
  - \AtBeginSection[] { \begin{frame}<beamer>{} \tableofcontents[currentsection] \end{frame} }
---

# Preface

## Metaclasses

###
*Metaclasses are deeper magic than 99% of users should ever worry about.
If you wonder whether you need them, you don’t.*\
\hfill --Time Peters

### Data model 'uses for'

- *Common uses for sets...*, an entry
- *Uses for metaclasses*, an subsubsection

## Set as datatype

### perlfaq: How can I remove duplicate elements from a list or array?

```perl
my @unique = keys { map { $_, 1 } @data };
```

### perlfaq: How do I sort an array by (anything)?

```perl
# Schwartzian Transform
my @sorted = map  { $_->[0] }
    sort { $a->[1] cmp $b->[1] }
    map  { [ $_, uc( (/\d+\s*(\S+)/)[0]) ] } @data;
```

## Topics

- Software engineering
- Development process
- Programming paradigms
- Refactoring

## Resources

###

- [`dpopchev/devbg2024`](https://github.com/dpopchev/devbg2024) repo at github
- [Gilded Rose Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)

###

- David Beazley
- Scott Wlaschin
- Kevlin Henney
- Mark Seemann
- Brandon Rhodes
- Martin Fowler
- Dave Farley
- Raymond Hettinger
- ...

# Prologue

## Gilded Rose

- `Gilded Rose` is a small inn ran by Allison
- Trade finest goods on the side
- Inventory system was implemented by a no-nonsense type named Leeroy
\onslide<2->{\item He moved on to new adventures}
\onslide<2->{\item The goblin helped with the implementation}
\onslide<3->{\item The system needs a small update}


## The system

```python
...
if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    if item.quality > 0:
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = item.quality - 1
else:
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
if item.name != "Sulfuras, Hand of Ragnaros":
    item.sell_in = item.sell_in - 1
if item.sell_in < 0:
    if item.name != "Aged Brie":
        if item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
...
```

## Software Crisis

### Formulation

*The basic problem is that certain classes of systems are placing demands on us
which are beyond our capabilities and our theories and methods of design and
production at this time...\
...We should not expect the production of such systems to be easy.*\
\hfill --Kenneth Kolence, pg 71

## Advices

\onslide<1->{
\begin{block}{NATO Conference 68}
Define a subset of the system which is small enough to bring to an operational
state...then build on that subsystem. This strategy requires that the system be
designed in modules which can be realized, tested, and modified independently.
\end{block}
}

\onslide<2->{
\begin{block}{UNIX Philosophy}
Write programs that do one thing and do it well. Write programs to work
together. Write programs to handle text streams, because that is an universal
interface.
\end{block}
}

\onslide<3->{
\begin{block}{Agile manifesto}
Deliver working software frequently, from a couple of weeks to a couple of
months, with a preference to the shorter timescale.
\end{block}
}

# The What

## System is doing

- All items have a `SellIn` value which denotes number of days within to sell it
- All items have a `Quality` value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item


# The How

# The Why

# Epilogue

# THE REST

## What they have

- System tracking the inventory of items
- Item sell in time measured in decreasing number of days
- Item quality measuring how valuable it is
- System lowers both remaining time and quality everyday

### What they want

- Control quality change rate
- Quality maximum and minimums

# Refactoring

## Lookup

```python:src/devbg2024/gilded_rose.py
# src/devbg2024/gilded_rose.py
class GildedRose(object):
    def __init__(self, items):
        self.items = items
    def update_quality(self):
        ...
class Item:
    def __init__(self, name, sell_in, quality):
        ...
```

# Sample slides

## SAMPLE SLIDES

SAMPLE SLIDES MARK

## Overalys

\only<1,3>{
This text appears on the first and third versions of the slide, but not the second.
INSIDE HERE YOU USE ANY LATEX
INSTEAD OF only you can use onslide etc
}

This uses beamer's highlighting command to \alert<2>{draw attention here}, but only on the second slide.

\note<2>{

Notes can also have overlay specs.
}

## Include image

![Flow chart](img/Untitled 1.png){ width=250px }


## Code

```{#code1 .jsx}
Bot.send("Are you going out to play?")
async function respond(inputText){
    if (inputText == "yes"){
        Bot.send("Wear a hat");
    }
    else {
        Bot.send("ok");
    }

 }
```

What we learned. - Bot.send() method - if else statements.
\
We should be able to refer [code](#code1)

## Math

The well known Pythagorean theorem $x^2 + y^2 = z^2$ was  proved to be invalid for other exponents.
Meaning the next equation has no integer solutions:
$$x^n + y^n = z^n$$

Can AI, help find near misses for this equation?
