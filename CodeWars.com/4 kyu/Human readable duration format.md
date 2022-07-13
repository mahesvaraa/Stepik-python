# Human readable duration format

https://www.codewars.com/kata/52742f58faf5485cae000b9a

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is
expressed as a combination of years, days, hours, minutes and seconds.

**It is much easier to understand with an example:**

```python
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

**Detailed rules**

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not
correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it
should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute
and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more
significant unit of time.

# Solution

```python
def format_duration(q):
    if q == 0:
        return 'now'
    years = divmod(q, 31536000)
    days = divmod(years[1], 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    
    res = [['', str(years[0]) + ' year' + ['s, ', ', '][years[0] == 1]][bool(years[0])],
           ['', str(days[0]) + ' day' + ['s, ', ', '][days[0] == 1]][bool(days[0])],
           ['', str(hours[0]) + ' hour' + ['s, ', ', '][hours[0] == 1]][bool(hours[0])],
           ['', str(minutes[0]) + ' minute' + ['s, ', ', '][minutes[0] == 1]][bool(minutes[0])],
           ['', str(minutes[1]) + ' second' + ['s ', ' '][minutes[1] == 1]][bool(minutes[1])]]
    res = [i for i in res if i]
    if len(res) > 1:
        res[-2] = res[-2].replace(',', '')
        res.insert(-1, 'and ')
    return ''.join(res).rstrip(', ')
```