#!/bin/bash
touch app/model/$*.py
touch app/payload/$*.py
touch app/router/$*.py
touch app/repository/$*.py
echo "Done"
exec bash