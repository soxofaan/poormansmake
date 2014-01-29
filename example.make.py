#!/usr/bin/env python

from poormansmake import target, main

@target
def clean():
    print 'Cleaning the cat box.'

@target
def deps():
    print 'Making sure all dependencies are met.'

@target
def release():
    clean()
    deps()
    print 'Creating release.'

if __name__ == '__main__':
    main()
