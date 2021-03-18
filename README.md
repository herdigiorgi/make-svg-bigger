# Make SVG Bigger

![](computer_guy.svg)

> I feel like somehow making an SVG 5 gigs would actually be a remarkable coding achievement... haha. Probably would involve a stupid amount of recursion. - [Twitter](https://twitter.com/Zamzee27/status/1372192811106234377?s=20)

With this python script you can make a SVG bigger, just because.

```bash
poetry shell
poetry install

# 40 mb
big_svg python big_svg.py --input-name="computer_guy.svg" --output-name="out.svg" --size "40mb"

# 5 gb
big_svg python big_svg.py --input-name="computer_guy.svg" --output-name="out.svg" --size "5gb"
```
