for file in *.py
do
  pyinstaller --onefile "$file"
done
