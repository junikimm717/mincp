CXX=g++-14
CXXFLAGS=-std=c++11 -Wall -Wextra -pedantic -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
FFLAGS=-std=c++11 -O2 -Wall -Wextra # for fast flags
PROG=PROB_NAME

header:
	$(CXX) $(CXXFLAGS) bits/stdc++.h
	$(CXX) $(CXXFLAGS) ext/pb_ds/assoc_container.hpp
.PHONY: header

noheader:
	rm -rf bits/stdc++.h.gch
	rm -rf ext/pb_ds/assoc_container.hpp.gch
.PHONY: noheader

clean: noheader
	rm *.in *.out *.res
.PHONY: clean

