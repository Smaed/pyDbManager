#!/usr/bin/env python
# -*- coding: utf-8 -*-


class setValues(object):
    
    def __init__(self):
        self.var = {'width'   :800,   'height' :600,
                    'treeSide':'left','toolBar':'top'}

    def _config(self):
        pass

    def _args(self):
        pass

    def setVars(self):
        return self.var

defVars = setValues().setVars()

def main():
    
    return 0
        
if __name__ == '__main__':
    main()

