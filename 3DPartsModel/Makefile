BLENDER := ~/.local/bin/blender
EXPORT_SCRIPT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))export_stl.py

%.py.stl: %.py
	$(BLENDER) --background --python $(EXPORT_SCRIPT) -- $< $@

# Find all .py files recursively (excluding base.py and export_stl.py)
SOURCES := $(shell find . -name '*.py' ! -name 'base.py' ! -name 'export_stl.py')
STLS := $(addsuffix .stl,$(SOURCES))

all: $(STLS)

clean:
	find . -name '*.stl' -delete

.PHONY: all clean
