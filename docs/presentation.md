---
topic: TopicMetaclasses
title: Metaclasses
subtitle: what I should have known from the start
author: Dimitar Popchev
theme: Frankfurt
date: \today
fontsize: 8pt
section-titles: false
toc: true
---

# Agenda

## Metaclasses

###
*Metaclasses are deeper magic than 99 of users should ever worry about.
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
- Refactoring to patterns

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

# Gilded Rose Kata

## Introduction

- `Gilded Rose` is a small inn ran by Allison
- Trade finest goods on the side
- Inventory system was implemented by a guy named Leeroy

## Software Crisis

### Formulation

*The basic problem is that certain classes of systems are placing demands on us
which are beyond our capabilities and our theories and methods of design and
production at this time...\
...We should not expect the production of such systems to be easy.*\
\hfill Kenneth Kolence, pg 71

## Advices

### NATO Conference 68

Define a subset of the system which is small enough to bring to an operational
state...then build on that subsystem. This strategy requires that the system be
designed in modules which can be realized, tested, and modified independently.

### UNIX Philosophy

Write programs that do one thing and do it well. Write programs to work
together. Write programs to handle text streams, because that is an universal
interface.

### Agile manifesto

Deliver working software frequently, from a couple of weeks to a couple of
months, with a preference to the shorter timescale.

## Requirements

### What they have

- System tracking the inventory of items
- Item sell in time measured in decreasing number of days
- Item quality measuring how valuable it is
- At end of each day the system lowers both remaining time and quality


### What they want

- Control quality change rate
- Quality maximum and minimums

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

```jsx
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

## Math

The well known Pythagorean theorem $x^2 + y^2 = z^2$ was  proved to be invalid for other exponents.
Meaning the next equation has no integer solutions:
$$x^n + y^n = z^n$$

Can AI, help find near misses for this equation?
