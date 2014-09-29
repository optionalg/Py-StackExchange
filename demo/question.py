#!/usr/bin/env python
from __future__ import print_function

# Same directory hack
import sys
sys.path.append('.')
sys.path.append('..')

import stackexchange
site = stackexchange.Site(stackexchange.StackOverflow)
site.be_inclusive()

id = int(raw_input("Enter a question ID: "))
question = site.question(id)

print('--- %s ---' % question.title)
print(question.body)
print()
print('%d answers.' % len(question.answers))
