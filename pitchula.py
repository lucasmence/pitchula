import reader
import sys

INDEX_ARGUMENT_IMAGE = 1
INDEX_ARGUMENT_AUDIO = 2

readerClass = reader.Reader()
readerClass.start(sys.argv[INDEX_ARGUMENT_IMAGE],sys.argv[INDEX_ARGUMENT_AUDIO])
del readerClass