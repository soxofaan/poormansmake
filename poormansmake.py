#!/usr/bin/env python

'''
Poor Man's Make
---------------

A simple, small, low dependency framework to create make-like build scripts in Python.
'''


import sys
import logging


_logger = logging.getLogger('poormansmake')

# Dictionary of available targets. Populated from calls to `target` function decorator.
_targets = {}


def target(f):
    '''
    Decorator for target functions.
    '''
    def wrapped(*args, **kwargs):
        # Check if this target already has run.
        if not hasattr(wrapped, '_result'):
            _logger.info('Starting target %r' % f.__name__)
            wrapped._result = f(*args, **kwargs)
            _logger.info('Done with target %r' % f.__name__)
        else:
            _logger.info('Target %r already fulfilled' % f.__name__)
        return wrapped._result
    _targets[f.__name__] = wrapped
    return wrapped


def main(targets=sys.argv[1:]):
    '''
    Main entry point function.
    '''
    # Basic logging setup
    logging.basicConfig(level=logging.INFO)

    # Default to target 'default'
    if len(targets) == 0:
        targets = ['default']

    # Run requested target functions.
    for target in targets:
        if target in _targets:
            _targets[target]()
        else:
            _logger.error('Unknown target %r' % target)

    _logger.info('All done')


##############################################################################
### Targets

@target
def default():
    print 'Available targets:'
    for name in _targets.keys():
        print '  -', name





##############################################################################
### Trigger main function.

if __name__ == '__main__':
    main()
