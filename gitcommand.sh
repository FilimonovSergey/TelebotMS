#!/bin/sh
compass compile -e production --force
git init
git add .
git commit
git push -u https://github.com/FilimonovSergey/TelebotMS