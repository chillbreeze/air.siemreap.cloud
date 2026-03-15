#!/bin/bash
# Run this from the blog/ directory whenever you add or edit a post
set -e
echo "Building blog..."
pelican content -s pelicanconf.py
echo "Done. Files are in ./output/"
