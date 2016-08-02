#!/usr/bin/env python
# coding=utf-8


from InfoExtractor import InfoExtractor
from docParser import DocToText

def main():
	text = DocToText("test.doc")
	
	#text = ' This is a healthy cat who is dancing'
	info = InfoExtractor(text)
	print info


if __name__ == '__main__':
	main()