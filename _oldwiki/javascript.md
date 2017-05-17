---
title:   "Javascript"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}

# sort this

<https://github.com/hemanth/functional-programming-jargon>

<https://www.reddit.com/r/javascript/comments/5hfq6n/100_minutes_of_free_functional_programming/>, <https://egghead.io/courses/professor-frisby-introduces-function-composition>


# misc

- q: `var` vs `let` --- a: just use `let`, never use `var`
- q: key = 'whatever'; { [key] : 'value'}
- q: return multiple values --- a: `f = () => { ... return [a, b] };  const [a, b] = f()` TODO: vs {a, b} = f() 
- q: print a json object --- a: `JSON.stringify(obj)`, TODO: vs toString vs serialize

тонкости модульной системы ECMAScript <https://habrahabr.ru/post/267639/>

- q: onKeyPress vs onKeyUp --- a: event sequence: down, press, press, press, ..., up

- q: `readOnly` vs `disabled` state of html input --- a: <http://stackoverflow.com/questions/7730695/whats-the-difference-between-disabled-disabled-and-readonly-readonly-for-ht>

- q: stack and queue in js -- a: <http://stackoverflow.com/questions/1590247/how-do-you-implement-a-stack-and-a-queue-in-javascript/1590262#1590262> 

# react 

- q: key property type --- a: string or number --- <https://facebook.github.io/react/docs/glossary.html#formal-type-definitions>

- q: in `immutable.js`: `.set()` vs `.update()` --- `.update()` gets a function as a param: `m.update('b', inc) #=> {a: 1, b: 3, c: 3})`
