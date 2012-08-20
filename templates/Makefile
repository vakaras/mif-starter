WAF=<< TOOLS_DIR >>/env/bin/python bin/waf

all: bin/waf build/c4che
	$(WAF)

bin:
	mkdir bin

bin/waf: bin
	cp << TOOLS_DIR >>/bin/waf bin/waf

build/c4che:
	$(WAF) configure
