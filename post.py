import sys, os
from datetime import date

postname = sys.argv[1]
today = date.today()
filename = f"{today}-{postname}.md"
postsPath = os.path.join(os.getcwd(), '_posts', filename)

template = f"""---
title: 
date: {today}
cover: 
categories:
---
"""

postFile = open(postsPath, "w")
postFile.write(template)
postFile.close()
