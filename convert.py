import glob, string
from shutil import copyfile
from array import array

# Find each var named search_text, and insert prefix_name at the start of the value.
# Expects var name and value to be in double quotes, and to be separated by a single whitespace (tab or space)
#
# Example: quake_replace("blah.map", "e1m1", "target"):
#   "target"\t"t5"\n
# becomes
#   "target"\t"e1m1_t5"\n
def quake_replace(filepath, prefix_name, search_text):
  search_text = '"' + search_text + '"'

  with open(filepath) as f:
    text = f.read()

  with open(filepath, 'w') as f:
    while True:
      index = text.find(search_text)
      if index == -1: 
        f.write(text)
        break

      index_target = index + len(search_text)

      # expect next char to be whitespace and then double quote
      if not (text[index_target] == ' ' or text[index_target] == '\t') or text[index_target+1] != '"':
        print "error:", search_text, "wasn't followed by tab and whitespace"
        print "file:", filepath, "variable:", search_text, "text:"
        print text[index:text.find('\n', index)]
        break

      # write the string up to the place we want to insert
      f.write(text[:index_target+2])

      # write the filename before the extension
      f.write(prefix_name + '_')
      
      # update the remaining filetext
      text = text[index_target+2:]


filenames = glob.glob('*.MAP')

for filename in filenames:
  if filename.startswith('B_'): continue

  output_filename =  'convert/' + filename.lower() 
  prefix = string.split(filename.lower(), '.')[0]

  copyfile(filename, output_filename) 
  quake_replace(output_filename, prefix, 'target')
  quake_replace(output_filename, prefix, 'targetname')
  quake_replace(output_filename, prefix, 'killtarget')

