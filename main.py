#!/usr/bin/env python
# coding=utf-8


from InfoExtractor import regex_info_extractor
from docParser import DocToText
import NER

def main():
	text = DocToText("test.doc")

	x = NER.chunk_NER(text)
	print x
	
	info = regex_info_extractor(text)

	# print info


if __name__ == '__main__':
	main()