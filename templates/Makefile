WAF=<< TOOLS_DIR >>/env/bin/python bin/waf -v

all: bin/waf build/c4che
	$(WAF)

bin:
	mkdir bin

bin/waf: bin
	cp << TOOLS_DIR >>/bin/waf bin/waf

show:
	xdg-open build/document.pdf 1> /dev/null 2> /dev/null

build/c4che:
	$(WAF) configure
