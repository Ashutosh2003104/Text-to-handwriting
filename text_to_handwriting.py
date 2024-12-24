import pywhatkit as pw
txt = """Create the imgs directory in the same location as your script (c:\Image_editor\).
Add some images (.jpg, .png) to the directory.
Run your script again."""
pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" end ")