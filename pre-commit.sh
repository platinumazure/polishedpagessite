#!/bin/sh

# N.B. This should be set up as a pre-commit hook.
# In a Bash-like environment, simply run the following command to do so:
# > cd [project root]
# > ln -s ../../pre-commit.sh .git/hooks/pre-commit

# Stash unstaged changes
git stash -q --keep-index

# Test prospective commit
python src/polishedpagessite/manage.py test polishedpages
RESULT=$?

# Pop the stash to reinsert unstaged changes into working tree
git stash pop -q

[ $RESULT -ne 0 ] && exit 1
exit 0
