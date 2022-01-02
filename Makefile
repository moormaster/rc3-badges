all: 2020/badges.html 2021/badges.html

clean:
	rm 2020/badges.html
	rm 2021/badges.html

2020/badges.html:	2020/badges.json 2020/template.html.j2
	./make_html.py -b 2020/badges.json -t 2020/template.html.j2 -o 2020/badges.html

2021/badges.html:	2021/badges.json 2021/template.html.j2
	./make_html.py -b 2021/badges.json -t 2021/template.html.j2 -o 2021/badges.html

