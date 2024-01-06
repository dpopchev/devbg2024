---
topic: TopicMetaclasses
title: Metaclasses
subtitle: what I should have known from the start
author: Dimitar Popchev
theme: Frankfurt
date: \today
section-titles: false
toc: true
---

# Agenda

## Metaclasses

### Tim Peters

*Metaclasses are deeper magic than 99% of users should ever worry about. If you
wonder whether you need them, you don’t (the people who actually need them know
with certainty that they need them, and don’t need an explanation about why).*

### Data model uses recommendation

- *Common uses for sets...*, an entry
- *Uses for metaclasses*, an subsubsection

## Topics

- Software engineering
- Development process
- Programming paradigms
- Refactoring to patterns

## Resources

- [dpopchev/devbg2024 repo at github](https://github.com/dpopchev/devbg2024)
- [Gilded Rose Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)

# What's out there?

![Verticles](img/Untitled.png)


## How do computers make decisions?

- Conditional statements are used to perform different actions based on different conditions.
- In many programming languages, decisions (also called conditionals) take the form of an if-then construct. They start with a condition, which is then evaluated as either True or False.

## How do computers make decisions?

![Flow chart](img/Untitled 1.png){ width=250px }

## Let's Build that

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

## Build a basic greetings bot

![Flow chart](img/Untitled 2.png)

## Benefits of AI Playground

- Streamlines a lot of back end operations, so that the you can just learn what AI is — and can get immediate results!
- User friendly!
- Designed to suit students needs.
- Students can see and publish new projects and thus learn from each other.

# How does learning AI help?

- Logical reasoning and Sequencing
- Critical thinking
- Problem solving
- Mental Mathematics
    - The above skills are implicit skills that students learn along with AI. And this helps them in academics, life, etc.

# Extra

The well known Pythagorean theorem $x^2 + y^2 = z^2$ was  proved to be invalid for other exponents.
Meaning the next equation has no integer solutions:
$$x^n + y^n = z^n$$

Can AI, help find near misses for this equation?
