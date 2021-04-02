# Create a single line script that returns the number of httpd processes that are running on the current machine
ps -e | grep httpd | grep -cv grep

# From the current folder (/tmp), provide some bash commands that will rename all the *.txt files in mig33/inner/ to *.dat
for fn in ./mig33/inner.folder/*.txt; do mv "$fn" "${fn/.txt}.dat"; done