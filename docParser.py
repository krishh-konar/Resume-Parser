''' Takes a Word document and converts it into a single python string '''

import os
import string

def DocToText(filename):
    #Input, Output, Error
    (fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
    fi.close()
    retval = fo.read()
    erroroutput = fe.read()
    fo.close()
    fe.close()
    
    if not erroroutput:
        return clean(retval)
    else:
        raise OSError("Executing the command caused an error: %s" % erroroutput)

def clean(text):
    text = text.replace('\t',' ')
    text = text.replace('  ',' ')
    text = text.replace('   ', ' ')
    text = text.replace('\n','. ')
    return text